from pyspark import SparkConf, SparkContext
from random import random
import matplotlib.pyplot as plt

def sample(_):
    x, y = random(), random()
    inside = x*x + y*y < 1
    return (x, y, inside)

conf = (
    SparkConf()
    .setAppName("PiApp")
    .set("spark.driver.host", "host.docker.internal")         # Worker가 Driver에 접근할 주소
    .set("spark.driver.bindAddress", "0.0.0.0")               # Driver가 내부적으로 바인딩할 주소
    .setMaster("spark://127.0.0.1:7077")
)

sc = SparkContext(conf=conf)
NUM_SAMPLES = 50000  # 시각화용이면 10000~50000이 적당

# 점 생성
rdd = sc.parallelize(range(NUM_SAMPLES)).map(sample)
data = rdd.collect()

# Pi 계산산
count_inside = sum(1 for x, y, inside in data if inside)
pi_estimate = 4.0 * count_inside / NUM_SAMPLES

# 점 분류
inside_x, inside_y = [], []
outside_x, outside_y = [], []

for x, y, inside in data:
    if inside:
        inside_x.append(x)
        inside_y.append(y)
    else:
        outside_x.append(x)
        outside_y.append(y)

# 시각화
fig, ax = plt.subplots(figsize=(6, 6))
ax.scatter(inside_x, inside_y, color='red', s=1, label='Inside Circle')
ax.scatter(outside_x, outside_y, color='blue', s=1, label='Outside Circle')

# 1/4 원 (반지름 1) 가이드
circle = plt.Circle((0, 0), 1, color='gray', fill=False, linestyle='--')
ax.add_artist(circle)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.set_title(f'Monte Carlo π Estimation\nEstimated π ≈ {pi_estimate:.6f}')
ax.legend()

# 이미지 저장
plt.savefig("pi_estimate_plot.png", dpi=200)
print("✅ 그림 저장 완료: pi_estimate_plot.png")

sc.stop()