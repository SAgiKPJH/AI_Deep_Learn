import os
from pyspark import SparkConf, SparkContext
from random import random

def sample(_):
    x, y = random(), random()
    return 1 if x*x + y*y < 1 else 0

if __name__ == "__main__":
    try:
        conf = (
            SparkConf()
            .setAppName("PiApp")
            .set("spark.driver.host", "host.docker.internal")         # Worker가 Driver에 접근할 주소
            .set("spark.driver.bindAddress", "0.0.0.0")               # Driver가 내부적으로 바인딩할 주소
            .setMaster("spark://127.0.0.1:7077")
        )
        
        sc = SparkContext(conf=conf)
        NUM_SAMPLES = 1000000

        count = sc.parallelize(range(NUM_SAMPLES)).map(sample).reduce(lambda a, b: a + b)
        print("Pi is roughly %f" % (4.0 * count / NUM_SAMPLES))
    except Exception as e:
        print("❌ Spark 작업 실패:", e)
    finally:
        sc.stop()