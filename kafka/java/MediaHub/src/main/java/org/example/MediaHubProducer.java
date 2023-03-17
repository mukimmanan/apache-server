package org.example;

import com.launchdarkly.eventsource.EventHandler;
import com.launchdarkly.eventsource.EventSource;
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.common.serialization.StringSerializer;

import java.net.URI;
import java.util.Properties;

public class MediaHubProducer {

    public static void main(String[] args) {
        Properties properties = new Properties();

        properties.setProperty("bootstrap.servers", "localhost:9093");
        properties.setProperty("key.serializer", StringSerializer.class.getName());
        properties.setProperty("value.serializer", StringSerializer.class.getName());
        properties.setProperty("batch.size", Integer.toString(32 * 1024));
        properties.setProperty(ProducerConfig.ACKS_CONFIG, "all");
        properties.setProperty(ProducerConfig.RETRY_BACKOFF_MS_CONFIG, "1000"); // Time to wait before next retry
        properties.setProperty(ProducerConfig.DELIVERY_TIMEOUT_MS_CONFIG, "120000");
        properties.setProperty(ProducerConfig.MAX_IN_FLIGHT_REQUESTS_PER_CONNECTION, "5"); // The maximum number of unacknowledged requests the client will send on a single connection before blocking.
        properties.setProperty(ProducerConfig.RETRIES_CONFIG, "10");
        properties.setProperty(ProducerConfig.ENABLE_IDEMPOTENCE_CONFIG, "true");
//        properties.setProperty(ProducerConfig.COMPRESSION_TYPE_CONFIG, "snappy"); // lz4
        properties.setProperty(ProducerConfig.LINGER_MS_CONFIG, "10000"); // how long to wait before sending a batch

        KafkaProducer<String, String> producer = new KafkaProducer<>(properties);
        EventHandler eventHandler = new MediaHubEventsHandler(producer, "mediahub");
        EventSource.Builder builder = new EventSource.Builder(eventHandler, URI.create("https://stream.wikimedia.org/v2/stream/recentchange"));
        EventSource source = builder.build();
        source.start();

        while (true) {

        }

    }

}
