package org.example;

import com.launchdarkly.eventsource.EventHandler;
import com.launchdarkly.eventsource.MessageEvent;
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class MediaHubEventsHandler implements EventHandler {
    private final KafkaProducer<String, String> producer;
    private final String topic;

    private final Logger log = LoggerFactory.getLogger(MediaHubEventsHandler.class.getSimpleName());

    public MediaHubEventsHandler(KafkaProducer<String, String> producer, String topic) {
        this.topic = topic;
        this.producer = producer;
    }

    @Override
    public void onOpen() {
        log.info("Connection is now open.");
    }

    @Override
    public void onClosed() {
        producer.close();
    }

    @Override
    public void onMessage(String event, MessageEvent messageEvent) throws Exception {
        log.info(messageEvent.getData());
        producer.send(new ProducerRecord<>(this.topic, messageEvent.getData()));
    }

    @Override
    public void onComment(String comment) {
        log.error("Comment -> " + comment);
    }

    @Override
    public void onError(Throwable t) {
        log.error("Error in Stream Reading", t);
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
    }
}
