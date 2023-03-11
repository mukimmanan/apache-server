from pyspark.sql import SparkSession
from pprint import pprint

spark = SparkSession.builder.master("local[*]") \
    .config("spark.ui.port", 6067) \
    .config("spark.sql.shuffle.partitions", 100) \
    .appName('KDD RDD Analysis') \
    .getOrCreate()

rdd = spark.read.text("../datasets/kddcup.data.gz").rdd.flatMap(list)
rdd = rdd.repartition(numPartitions=10)

pprint(rdd.takeSample(False, 10, 23))
print("Number of elements =", rdd.count())

normal = rdd.filter(lambda x: "normal" in x)
print("Number of normal connections =", normal.count())

labels = rdd.map(lambda x: x.split(",")[-1].replace(".", "") if x.split(",")[-1] is not None else None).distinct()
print("Available labels =", labels.collect())

labels_connection_count = rdd.map(lambda x: (x.split(",")[-1].replace(".", ""), 1))
labels_connection_count = labels_connection_count.reduceByKey(lambda x, y: x + y)
print("Connections per label =", labels_connection_count.collect())

root_shells = rdd.filter(lambda x: x.split(",")[13] == '1')
root_shells = root_shells.filter(lambda x: True if int(x.split(",")[4]) * 500 < int(x.split(",")[5]) else False)
print("Root shell where src bytes > dst bytes * 500", root_shells.collect())

split = rdd.map(lambda x: x.split(","))

normal = split.filter(lambda x: "normal" in x[-1] and x[21] != '1').map(lambda x: (x[1], 1))
normal = normal.reduceByKey(lambda x, y: x + y)
print("Normal connections =", normal.collect())

vulnerable = split.filter(lambda x: "normal" not in x[-1] and x[21] != '1').map(lambda x: (x[1], 1))
vulnerable = vulnerable.reduceByKey(lambda x, y: x + y)
print("Vulnerable connections =", vulnerable.collect())
