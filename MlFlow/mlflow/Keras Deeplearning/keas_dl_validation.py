import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import (
    mean_squared_error, mean_absolute_error, r2_score,
    confusion_matrix, roc_curve, auc
)
from sklearn.preprocessing import StandardScaler

from tensorflow import keras

# 1. 모델 로드
model = keras.models.load_model("model/dl_model.h5")

# 2. 데이터 로딩
wine_origin = pd.read_csv('./wine_data_homework.csv')
wine_origin = wine_origin.drop(columns=[wine_origin.columns[0], 'fixed acidity', 'pH', 'free sulfur dioxide'])
wine_cleaned = pd.read_csv('./wine_data_cleaned.csv')
def split_data(original: pd.DataFrame):
    original = original.drop(columns=[original.columns[0]])
    data = (original - original.min()) / (original.max() - original.min())
    data['quality'] = original['quality']

    X = data.drop("quality", axis=1)
    y = data["quality"]
    return X, y
origin_x, origin_y = split_data(wine_origin)
cleaned_x, cleaned_y = split_data(wine_cleaned)

# 3. 스케일링 (모델 학습 시와 동일한 방식 적용 필요)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(cleaned_x)

y_pred = model.predict(X_scaled).flatten()
y_true = cleaned_y.values.flatten()

mse = mean_squared_error(y_true, y_pred)
mae = mean_absolute_error(y_true, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_true, y_pred)
print(f"MAE: {mae:.4f}")
print(f"MSE: {mse:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"R²: {r2:.4f}")

y_pred_class = np.clip(np.round(y_pred), 0, 9).astype(int)
y_true_class = np.clip(np.round(y_true), 0, 9).astype(int)
cm = confusion_matrix(y_true_class, y_pred_class, labels=np.arange(10))
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=np.arange(10), yticklabels=np.arange(10))
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix (Rounded Classes)")
plt.tight_layout()
plt.savefig("confusion_matrix.png")
plt.close()

# ROC Curve & AUC
y_true_bin = (y_pred_class == y_true_class).astype(int)
y_score_bin = y_pred_class
fpr, tpr, thresholds = roc_curve(y_true_bin, y_score_bin)
roc_auc = auc(fpr, tpr)

plt.figure(figsize=(6, 4))
plt.plot(fpr, tpr, label=f"ROC curve (AUC = {roc_auc:.2f})", color='blue')
plt.plot([0, 1], [0, 1], 'k--', label="Random Classifier")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend(loc="lower right")
plt.grid(True)
plt.tight_layout()
plt.savefig("roc_curve.png")
plt.close()