import os
import sys
import warnings
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import mlflow
import mlflow.sklearn

# 경고 무시
warnings.filterwarnings("ignore")

# 고정된 랜덤 시드
np.random.seed(40)

# 평가 지표 계산 함수 정의
def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2

if __name__ == "__main__":
    # 데이터 로드
    wine_path = os.path.join("./", "wine_data_homework.csv")
    data = pd.read_csv(wine_path)

    # MLflow 설정
    mlflow.set_tracking_uri("file:///D:/Sagi_JJU D/MlFlow/.mlflow")
    mlflow.set_experiment(experiment_name="MLOPS-Final-2512")

    # 학습/테스트 데이터 분리
    train, test = train_test_split(data, test_size=0.25)

    train_x = train.drop(["quality"], axis=1)
    test_x = test.drop(["quality"], axis=1)
    train_y = train["quality"]
    test_y = test["quality"]

    # 하이퍼파라미터 설정
    alpha = 0.5
    l1_ratio = 0.5

    # MLflow 실험 시작
    with mlflow.start_run():
        lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)
        lr.fit(train_x, train_y)

        predicted_qualities = lr.predict(test_x)

        rmse, mae, r2 = eval_metrics(test_y, predicted_qualities)

        print(f"ElasticNet model (alpha={alpha}, l1_ratio={l1_ratio}):")
        print(f"  RMSE: {rmse}")
        print(f"  MAE: {mae}")
        print(f"  R2: {r2}")

        # 파라미터 및 메트릭 로그
        mlflow.log_param("alpha", alpha)
        mlflow.log_param("l1_ratio", l1_ratio)

        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("mae", mae)
        mlflow.log_metric("r2", r2)

        # 모델 로그
        mlflow.sklearn.log_model(lr, "model")