from pyspark import SparkContext
from random import random

sc = SparkContext("spark://master-node:7077", "PiApp")
NUM_SAMPLES = 1000000

def sample(_):
    x, y = random(), random()
    return 1 if x*x + y*y < 1 else 0

count = sc.parallelize(range(NUM_SAMPLES)).map(sample).reduce(lambda a, b: a + b)
print("Pi is roughly %f" % (4.0 * count / NUM_SAMPLES))
sc.stop()