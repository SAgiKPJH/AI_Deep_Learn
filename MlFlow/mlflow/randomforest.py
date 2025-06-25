import os
import warnings
import pandas as pd
import numpy as np
from itertools import product 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.ensemble import RandomForestRegressor
import mlflow
import mlflow.sklearn

# 경고 무시
warnings.filterwarnings("ignore")

# 랜덤 시드 고정
np.random.seed(40)

# 지표 계산 함수
def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2

if __name__ == "__main__":
    # 데이터 로딩
    original = pd.read_csv("wine_data_cleaned.csv")
    original = original.drop(columns=[original.columns[0]])
    data = (original - original.min()) / (original.max() - original.min())
    data['quality'] = original['quality']

    # 특성과 타겟 분리
    X = data.drop("quality", axis=1)
    y = data["quality"]

    # 표준화
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # 데이터 분할
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.25, random_state=42)

    # 테스트할 하이퍼파라미터 조합
    n_estimators_list = [50, 100, 200]
    max_depth_list = [None, 10, 20]
    min_samples_split_list = [2, 5]
    min_samples_leaf_list = [1, 2, 4]
    max_features_list = ['sqrt', 'log2']
    boostrap_list = [True, False]
    criterion_list = ['squared_error', 'absolute_error']

    # MLflow 설정
    mlflow.set_tracking_uri("file:///D:/Sagi_JJU D/MlFlow/.mlflow")
    mlflow.set_experiment("MLOPS-RF")

    for n_estimators, max_depth, min_split, min_leaf, max_feat, boostrap, criterion in product(
        n_estimators_list,
        max_depth_list,
        min_samples_split_list,
        min_samples_leaf_list,
        max_features_list,
        boostrap_list,
        criterion_list
    ):
        with mlflow.start_run():
            model = RandomForestRegressor(
                n_estimators=n_estimators,
                max_depth=max_depth,
                min_samples_split=min_split,
                min_samples_leaf=min_leaf,
                max_features=max_feat,
                random_state=42,
                bootstrap=boostrap,
                criterion=criterion
            )
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            rmse, mae, r2 = eval_metrics(y_test, y_pred)

            print(f"n_estimators={n_estimators}, max_depth={max_depth}")
            print(f"  RMSE: {rmse:.4f}, MAE: {mae:.4f}, R2: {r2:.4f}")

            # 로그 기록
            mlflow.log_param("n_estimators", n_estimators)
            mlflow.log_param("max_depth", max_depth)
            mlflow.log_param("min_samples_split", min_split)
            mlflow.log_param("min_samples_leaf", min_leaf)
            mlflow.log_param("max_features", max_feat)
            mlflow.log_param("bootstrap", boostrap)
            mlflow.log_param("criterion", criterion)
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2)

            mlflow.sklearn.log_model(model, artifact_path="model")