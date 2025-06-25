import os
import warnings
import pandas as pd
import numpy as np
from itertools import product
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import tensorflow as tf
from tensorflow import keras
import mlflow
import mlflow.tensorflow

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

    # 특성/타겟 분리 및 스케일링
    X = data.drop("quality", axis=1)
    y = data["quality"]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.25, random_state=42)

    # 하이퍼파라미터 조합
    epochs_list = [10]
    batch_size_list = [32]
    hidden_units_list = [[64, 32]] # [128, 64, 32]
    activation_list = ['relu', 'sigmoid', 'tanh']
    optimizer_list = ['adam', 'sgd', 'rmsprop']
    learning_rate_list = [0.001, 0.0005]
    loss_fn_list = ['mse', 'mae']
    dropout_rate_list = [0.2, 0.3]
    validation_split_list = [0.2]
    kernel_initializer_list = ['he_uniform', 'glorot_uniform']

    # MLflow 설정
    mlflow.set_tracking_uri("file:///workspace/.mlflow")
    mlflow.set_experiment("DeepLearning_HyperParam")

    for (epochs, batch_size, hidden_units, activation, optimizer_name, learning_rate, loss_fn,
         dropout_rate, validation_split, kernel_initializer) in product(
        epochs_list,
        batch_size_list,
        hidden_units_list,
        activation_list,
        optimizer_list,
        learning_rate_list,
        loss_fn_list,
        dropout_rate_list,
        validation_split_list,
        kernel_initializer_list
    ):
        with mlflow.start_run():
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
            model.add(keras.layers.Dense(1))

            optimizer = keras.optimizers.get({'class_name': optimizer_name, 'config': {'learning_rate': learning_rate}})
            model.compile(optimizer=optimizer, loss=loss_fn, metrics=['mae'])

            model.fit(X_train, y_train,
                      validation_split=validation_split,
                      epochs=epochs,
                      batch_size=batch_size,
                      verbose=0)

            y_pred = model.predict(X_test).flatten()
            rmse, mae, r2 = eval_metrics(y_test, y_pred)

            print(f"{hidden_units}, Dropout={dropout_rate}, Epochs={epochs}, Batch={batch_size} => RMSE={rmse:.4f}, MAE={mae:.4f}, R2={r2:.4f}")
            print(f"Optimizer: {optimizer_name}, Learning Rate: {learning_rate}, Loss Function: {loss_fn}, Activation: {activation}, Kernel Initializer: {kernel_initializer}")

            # 파라미터 로그
            mlflow.log_param("epochs", epochs)
            mlflow.log_param("batch_size", batch_size)
            mlflow.log_param("hidden_units", hidden_units)
            mlflow.log_param("activation", activation)
            mlflow.log_param("optimizer", optimizer_name)
            mlflow.log_param("learning_rate", learning_rate)
            mlflow.log_param("loss_fn", loss_fn)
            mlflow.log_param("dropout_rate", dropout_rate)
            mlflow.log_param("validation_split", validation_split)
            mlflow.log_param("kernel_initializer", kernel_initializer)

            # 메트릭 로그
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2)

            mlflow.tensorflow.log_model(model, artifact_path="model")