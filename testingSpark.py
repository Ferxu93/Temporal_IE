import pyspark
from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark import SparkConf
import os
import findspark
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import mpld3
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import *
import pyspark.sql.functions as F

spark_home = os.environ.get('SPARK_HOME', None)

sc = SparkContext.getOrCreate()

test = sc.parallelize([8, 20, 40, 34], 5).glom().collect()
print(test)




