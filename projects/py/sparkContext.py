from pyspark.sql import SparkSession
from pyspark.sql.types import StringType, StructField, IntegerType, StructType, NumericType


spark = SparkSession.builder.config("spark.sql.warehouse.dir", "hdfs://namenode:9000/user/hive/warehouse/").enableHiveSupport().appName("Learning Pyspark").master("local").getOrCreate()

schema = StructType([
    StructField("order_id", IntegerType(), nullable=False),
    StructField("order_date", StringType(), True),
    StructField("user_id", IntegerType(), nullable=False),
    StructField("order_status", StringType(), True)
])

# data = spark.read.csv(
#     "hdfs://namenode:9000/user/hive/warehouse/retails.db/retails/orders/",
#     sep=",",
#     header=False,
#     schema=schema,
#     # schema="order_id int,order_date string,customer_id int,order_status string"
# )

# data = spark.read.format("csv").option("sep", ",").schema(schema).load("hdfs://namenode:9000/user/hive/warehouse/retails.db/retails/orders/")

orders = spark.read.csv("hdfs://namenode:9000/user/hive/warehouse/retail.db/orders/", sep=",", header=False, schema="""
    order_id INT,
    order_date STRING,
    order_customer_id INT,
    order_status STRING
""")

orders.show()