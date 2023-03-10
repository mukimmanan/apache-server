from pyspark.sql import SparkSession
from pyspark.sql.types import StringType, StructField, IntegerType, StructType, NumericType

# Creating a spark session
spark = SparkSession.builder.appName("Playing with Dataframes").master("local").getOrCreate()

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

data = spark.read.format("csv").option("sep", ",").schema(schema).load("hdfs://namenode:9000/user/hive/warehouse/retails.db/retails/orders/")

data.printSchema()

first = data.first()
print(first)
data.show(10)

order_id = data.select(
    data.order_id.cast("int")
)
order_id.show(10)