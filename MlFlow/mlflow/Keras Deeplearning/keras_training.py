import os
import warnings
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import tensorflow as tf
from tensorflow import keras

# 경고 무시
warnings.filterwarnings("ignore")

# 시드 고정
np.random.seed(40)
tf.random.set_seed(40)

# 지표 계산 함수
def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2

if __name__ == "__main__":
    # 데이터 로딩 및 정규화
    original = pd.read_csv("wine_data_cleaned.csv")
    original = original.drop(columns=[original.columns[0]])
    data = (original - original.min()) / (original.max() - original.min())
    data['quality'] = original['quality']

    # 특성과 타겟 분리 및 스케일링
    X = data.drop("quality", axis=1)
    y = data["quality"]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.25, random_state=42)

    # 하이퍼파라미터 설정
    epochs = 1000
    batch_size = 8
    hidden_units = [64]
    activation = 'tanh'
    optimizer_name = 'adam'
    learning_rate = 0.001
    loss_fn = 'mse'
    dropout_rate = 0.3
    validation_split = 0.2
    kernel_initializer = 'glorot_uniform'

    # 모델 정의
    model = keras.models.Sequential()
    for idx, units in enumerate(hidden_units):
        if idx == 0:
            model.add(keras.layers.Dense(units, activation=activation,
                                         kernel_initializer=kernel_initializer,
                                         input_shape=(X_train.shape[1],)))
        else:
            model.add(keras.layers.Dense(units, activation=activation,
                                         kernel_initializer=kernel_initializer))
        model.add(keras.layers.Dropout(dropout_rate))
    model.add(keras.layers.Dense(1))  # 회귀용 출력층

    optimizer = keras.optimizers.get({'class_name': optimizer_name, 'config': {'learning_rate': learning_rate}})
    model.compile(optimizer=optimizer, loss=loss_fn, metrics=['mae'])

    # 모델 학습
    model.fit(X_train, y_train,
              validation_split=validation_split,
              epochs=epochs,
              batch_size=batch_size,
              verbose=1)

    # 예측 및 평가
    y_pred = model.predict(X_test).flatten()
    rmse, mae, r2 = eval_metrics(y_test, y_pred)

    print(f"평가 지표:\n RMSE={rmse:.4f}, MAE={mae:.4f}, R2={r2:.4f}")

    model.save("trained_model_1000epoch.h5")
