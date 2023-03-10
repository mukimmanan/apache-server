from pyspark import SparkContext

# Creating the spark context
spark_context = SparkContext("local", "Simple Application")

# Creating the RDD
orders = spark_context.textFile("hdfs://namenode:9000/user/hive/warehouse/retails.db/retails/orders/", minPartitions=5)

status_count = orders.flatMap(
    lambda line: line.split(",")[3].split("T")
).map(
    lambda status: (status, 1)
).reduceByKey(lambda x, y: x + y)

for i in status_count.take(10):
    print(i)