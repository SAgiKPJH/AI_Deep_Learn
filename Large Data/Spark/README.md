# Spark Example

### 폴더 구조

- `Server/` : 도커로 Spark 클러스터(마스터/워커) 실행 및 서버 예제
- `LocalExample/` : 로컬 환경에서 PySpark 실행 예제

## 1. Spark 설치

### Java 설치 및 환경 설정
```bash
# Windows
# 1. Java JDK 설치 (https://adoptium.net/)
# 2. 환경 변수 설정
#    - JAVA_HOME: JDK 설치 경로 (예: C:\Program Files\Java\jdk-11)
#    - Path에 %JAVA_HOME%\bin 추가

# Linux/Mac
sudo apt-get update
sudo apt-get install openjdk-11-jdk
```

### Python 패키지 설치
```bash
pip install pyspark findspark jupyter matplotlib pandas
```
- 가상 환경 설정
```bash
# 가상환경 생성
python -m venv spark-env

# 가상환경 활성화
# Windows
spark-env\Scripts\activate
# Linux/Mac
source spark-env/bin/activate
```

## 2. 로컬에서 PySpark 실행 예제

```bash
python LocalExample/spark_local.py
```
- 로컬 모드에서 파이(π) 근사값을 계산하는 예제입니다.

## 3. 도커로 Spark 클러스터 실행

```bash
docker-compose -f Server/spark.yml up -d --scale spark-worker=4
```
- 마스터 UI: http://localhost:8080  
- 워커 2개가 자동으로 연결

## 4. 클러스터에서 PySpark 코드 실행

```bash
python Server/spark_server.py
```
- `SparkContext("spark://master-node:7077", "PiApp")`에서 master-node는 도커 네트워크 내 컨테이너명(spark-master)로 맞춰야 합니다.
- 클러스터 환경에서 파이(π) 근사값을 계산합니다.

### 참고 패키지

| 패키지                    | 용도                                     |
| ---------------------- | -------------------------------------- |
| `findspark`            | 로컬 Jupyter 환경에서 PySpark 설정을 쉽게 해주는 도우미 |
| `jupyter`              | 노트북 기반 개발용                             |
| `matplotlib`, `pandas` | 분석 결과 시각화 및 DataFrame 조작               |
