from pyspark.sql import SparkSession
from pyspark.sql.types import StringType, StructField, IntegerType, StructType, ArrayType

# set spark.sql.warehouse.dir;

spark = SparkSession.builder.master("local").appName("Spark SQL").config("spark.sql.warehouse.dir", "hdfs://namenode:9000/user/hive/warehouse/").enableHiveSupport().getOrCreate()

# schema = StructType([
#     StructField("order_id", IntegerType(), nullable=False),
#     StructField("order_date", StringType(), True),
#     StructField("user_id", IntegerType(), nullable=False),
#     StructField("order_status", StringType(), True)
# ])

# data = spark.read.csv(
#     "hdfs://namenode:9000/user/hive/warehouse/retails.db/retails/orders/",
#     sep=",",
#     header=False,
#     schema=schema,
# )

# data.createOrReplaceTempView("orders")
# order_id = spark.sql("SELECT order_id from orders")
# order_id.show(10)


spark.sql("CREATE DATABASE IF NOT EXISTS retail")
spark.sql("USE retail")
spark.sql("show tables")

# spark.sql("DROP TABLE IF EXISTS orders")

orders = """
CREATE TABLE IF NOT EXISTS retail.orders (
  order_id INT NOT NULL,
  order_date TIMESTAMP NOT NULL,
  order_customer_id INT NOT NULL,
  order_status VARCHAR(45) NOT NULL
) ROW FORMAT DELIMITED FIELDS TERMINATED BY ",";
"""
spark.sql(orders)
# LOAD DATA LOCAL INPATH "/hive-data/retails/orders" into TABLE orders;

orders = spark.sql("SELECT * FROM retail.orders")
orders.show(10)

count = orders.count()
print("Total Records = ", count)

# spark.sql("DROP TABLE IF EXISTS order_items")
order_items = """
    CREATE TABLE IF NOT EXISTS retail.order_items (
  order_item_id INT NOT NULL,
  order_item_order_id INT NOT NULL,
  order_item_product_id INT NOT NULL,
  order_item_quantity INT NOT NULL,
  order_item_subtotal FLOAT NOT NULL,
  order_item_product_price FLOAT NOT NULL
) ROW FORMAT DELIMITED FIELDS TERMINATED BY ",";
"""

spark.sql(order_items)
order_items = spark.sql("SELECT * FROM retail.order_items")
order_items.show(10)

count = order_items.count()
print("Total Records = ", count)

# Projection
spark.sql("SELECT order_customer_id, date_format(CAST(order_date AS TIMESTAMP), 'yyyy-MM') AS order_month, order_status FROM retail.orders LIMIT 10;").show(20)

################################################
spark.sql("CREATE DATABASE IF NOT EXISTS sms")
spark.sql("USE sms")
spark.sql("show tables")

students = """
    CREATE TABLE IF NOT EXISTS sms.students (
        id INT,
        first_name STRING,
        last_name STRING,
        phone_numbers ARRAY<STRING>,
        address STRUCT<street:STRING, city:STRING, state:STRING, zip:STRING>
    ) STORED AS TEXTFILE
    ROW FORMAT
    DELIMITED FIELDS TERMINATED BY "\t"
    COLLECTION ITEMS TERMINATED BY "|"
"""
#  {"street": "Amrapali", "city": "raipur", "state": "chhattisgarh", "zip": "492001"}
spark.sql(students)
insert_student = """
    INSERT INTO sms.students VALUES (
        2,
        "Manan2",
        "Mukim2",
        {0},
        NULL
    )
""".format('ARRAY("1", "2")')
spark.sql(insert_student)
students = spark.sql("SELECT * FROM sms.students")
students.show()

# explode, explode_outer