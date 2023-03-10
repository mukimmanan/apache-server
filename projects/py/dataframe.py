from pyspark.sql import SparkSession

spark = SparkSession.builder.master("yarn") \
    .appName('Practising DataFrames') \
    .getOrCreate()

data = spark.read.csv("hdfs://namenode:9000/user/manan/CompleteDataset.csv", header=True, inferSchema=True)
print("Number of Partitions =", data.rdd.getNumPartitions())
