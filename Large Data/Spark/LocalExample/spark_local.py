from pyspark import SparkContext
from random import random

# SparkContext 생성
sc = SparkContext("local", "Pi Approximation")

NUM_SAMPLES = 1000000  # 샘플 개수

# 샘플 함수 정의
def sample(_):
    x, y = random(), random()
    return 1 if x*x + y*y < 1 else 0

# RDD 구성 및 연산
count = sc.parallelize(range(0, NUM_SAMPLES)) \
          .map(sample) \
          .reduce(lambda a, b: a + b)

# 결과 출력
print("Pi is roughly %f" % (4.0 * count / NUM_SAMPLES))

# SparkContext 종료
sc.stop()