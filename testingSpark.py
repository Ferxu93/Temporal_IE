import pyspark
from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark import SparkConf
import os
import findspark

spark_home = os.environ.get('SPARK_HOME', None)

sc = SparkContext.getOrCreate()

test = sc.parallelize([8, 20, 40, 34], 5).glom().collect()
print(test)




