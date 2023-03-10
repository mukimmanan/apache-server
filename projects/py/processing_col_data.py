from pyspark.sql import SparkSession
from pyspark.sql.types import StringType, StructField, IntegerType, StructType, NumericType
from pyspark.sql import functions


spark = SparkSession.builder.config("spark.sql.warehouse.dir", "hdfs://namenode:9000/user/hive/warehouse/").enableHiveSupport().appName("Processing Column Data").master("local").getOrCreate()

schema = StructType([
    StructField("order_id", IntegerType(), nullable=False),
    StructField("order_date", StringType(), True),
    StructField("user_id", IntegerType(), nullable=False),
    StructField("order_status", StringType(), True)
])

orders = spark.read.csv(
    "hdfs://namenode:9000/user/hive/warehouse/retail.db/orders/",
    sep=",",
    header=False,
    schema=schema,
)

orders.show()
orders.select("*", functions.date_format('order_date', "yyyyMM").alias("order_month")).show()
orders.filter(functions.date_format('order_date', "yyyyMM") == '201307').show()
