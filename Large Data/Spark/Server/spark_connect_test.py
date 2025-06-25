from pyspark import SparkContext, SparkConf

try:
    conf = SparkConf().setMaster("spark://127.0.0.1:7077").setAppName("TestApp")
    sc = SparkContext(conf=conf)
    print("✅ SparkContext 연결 성공!")
    sc.stop()
except Exception as e:
    print("❌ SparkContext 연결 실패:")
    print(e)