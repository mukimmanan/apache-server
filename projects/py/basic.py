from pyspark import SparkContext

# Creating the spark context
spark_context = SparkContext("local", "Basic App")

orders = spark_context.textFile("hdfs://namenode:9000/user/hive/warehouse/retails.db/retails/orders/", minPartitions=5)

ordersMap = orders.map(lambda order: (int(order.split(",")[0])))
print("Count of Orders =", ordersMap.count())
 