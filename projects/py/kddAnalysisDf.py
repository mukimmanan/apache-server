from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[*]") \
    .config("spark.ui.port", 6067) \
    .config("spark.sql.shuffle.partitions", 10) \
    .appName('KDD DF Analysis') \
    .getOrCreate()

data = spark.read.csv("../datasets/kddcup.data.gz", header=False)
data = data.withColumnRenamed("_c1", "protocol")\
    .withColumnRenamed("_c2", "service")\
    .withColumnRenamed("_c3", "flag")\
    .withColumnRenamed("_c4", "src_bytes")\
    .withColumnRenamed("_c5", "dst_bytes")\
    .withColumnRenamed("_c8", "urgent")\
    .withColumnRenamed("_c10", "num_failed_logins")\
    .withColumnRenamed("_c13", "root_shell")\
    .withColumnRenamed("_c21", "guest_login")\
    .withColumnRenamed("_c41", "label")\
    .select("protocol", "service", "flag", "dst_bytes", "src_bytes", "urgent", "num_failed_logins",
            "root_shell", "guest_login", "label")

data.printSchema()
data.show()

data.createOrReplaceTempView("kddcup")
connections_per_label = data.groupBy("label").count().withColumnRenamed("count", "num connections")
connections_per_label.show()

