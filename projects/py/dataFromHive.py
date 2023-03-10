from pyspark.sql import SparkSession

spark = SparkSession.builder.enableHiveSupport().appName("Dataframes with Hive").master("local").getOrCreate()

# data = spark.sql("SELECT * from retails.orders")
data = spark.read.table("retails.orders")
data.show(10)