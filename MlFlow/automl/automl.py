import mlflow 
mlflow.set_tracking_uri("file:///D:/Sagi_JJU D/MlFlow/.mlflow")

import pandas as pd
from pycaret.classification import *

# quality 컬럼을 기준으로 이진 분류로 변환
data = pd.read_csv("wine_data_cleaned.csv")
data = data.drop(columns=[data.columns[0]])
normal = (data - data.min()) / (data.max() - data.min())
normal['quality'] = data['quality']

# PyCaret 환경 설정 (setup)
clf = setup(
    normal,
    target='quality',
    session_id=123,
    normalize=False,
    log_experiment=True,
    experiment_name="PyCaret_AutoML_Cleaned"
)

# 모델 자동 비교
best_model = compare_models()