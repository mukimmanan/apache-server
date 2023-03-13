package demo.kafka;

import org.apache.kafka.clients.producer.Callback;
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.clients.producer.RecordMetadata;
import org.apache.kafka.common.serialization.StringSerializer;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.Properties;


public class ProducerDemo {

    private static final Logger log = LoggerFactory.getLogger(ProducerDemo.class.getSimpleName());
    public static void main(String[] args) {
        Properties properties = new Properties();

        properties.setProperty("bootstrap.servers", "localhost:9093");
        properties.setProperty("key.serializer", StringSerializer.class.getName());
        properties.setProperty("value.serializer", StringSerializer.class.getName());
        properties.setProperty("batch.size", "10000");

        KafkaProducer<String, String> producer = new KafkaProducer<>(properties);

        for (int i = 1000000000; i < 1000000001; i ++) {
            ProducerRecord<String, String> producerRecord = new ProducerRecord<>("demo_java", i + "");

            producer.send(producerRecord, (metadata, exception) -> {
                if (exception == null) {
                    log.info("Received new metadata \n" +
                            "Topic: " + metadata.topic() + "\n" +
                            "Parition: " + metadata.partition());
                }

            });
        }

        // Tells the producer to send all data and block until done --synchronous.
//        producer.flush();
        producer.close();
    }
}
