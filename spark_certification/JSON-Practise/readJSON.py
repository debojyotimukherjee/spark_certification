from pyspark.sql import SparkSession
spark = SparkSession\
        .builder\
        .getOrCreate()

dfJson = spark.read.json("airflow_mysql.json",multiLine=True)
dfJson.printSchema()

dfJson.createOrReplaceTempView("dfJson")

spark.sql("select Outputs from dfJson").show()