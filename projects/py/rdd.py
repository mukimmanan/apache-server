from pyspark.sql import SparkSession
import random
from operator import add

spark = SparkSession.builder.master("spark://spark-master:7077") \
    .appName('Practising RDD') \
    .getOrCreate()

random_list = random.sample(
    range(0, 100), 10
)

sc = spark.sparkContext
random_rdd = sc.parallelize(random_list, numSlices=4)

# print(random_rdd.take(10))
# print("Number of Partitions =", random_rdd.getNumPartitions())
# print("Show which data is in which partition =", random_rdd.glom().collect())
# print("Get data for 2 partitions =", random_rdd.glom().take(2))

rdd_map = random_rdd.map(lambda x: x[1] * 100)
rdd_filter = random_rdd.filter(lambda x: x % 3 == 0)

rdd_flatmap = random_rdd.flatMap(lambda x: [x + 2, x + 5])
rdd_reduce = rdd_flatmap.reduce(add)

# Descriptive Statistics
print("Max =", random_rdd.max())

# Map Partitions
rdd_map_partitions = random_rdd.mapPartitions(lambda x: sum(x))

# Union
rdd2 = sc.parallelize([1, 4, 3, 10, 23, 41, 232], numSlices=2)
rdd_union = random_rdd.union(rdd2)
