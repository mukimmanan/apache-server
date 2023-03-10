from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local").appName("Spark SQL").config("spark.sql.warehouse.dir", "hdfs://namenode:9000/user/hive/warehouse/").enableHiveSupport().getOrCreate()

spark.sql("SELECT * FROM hr.employees limit 10").show()

window_sql = """
    SELECT employee_id, department_id, salary,
    count(1) OVER (PARTITION BY department_id) AS employee_count,
    rank() OVER (ORDER BY salary DESC) AS rank,
    lead(employee_id, 1, 'NA') OVER (PARTITION BY department_id ORDER BY salary DESC) AS lead_emp_id,
    lag(employee_id) OVER (PARTITION BY department_id ORDER BY salary DESC) AS lag_emp_id,
    lead(salary) OVER (PARTITION BY department_id ORDER BY salary DESC) AS lead_emp_salary
    FROM hr.employees
    ORDER BY employee_id;
"""

spark.sql(window_sql).show()

window_sql = """
    SELECT employee_id, department_id, salary, 
    sum(salary) OVER (PARTITION BY department_id) AS dept_total,
    salary / sum(salary) OVER (PARTITION BY department_id) AS pct 
    FROM hr.employees
    ORDER BY department_id;
"""

spark.sql(window_sql).show()