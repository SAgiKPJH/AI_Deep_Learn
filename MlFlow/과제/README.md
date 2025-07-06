# CMD
```py
python -m venv .venv
py -3.11 -m venv .venv
.venv/Scripts/Activate.ps1

pip install pycaret[full] mlflow==2.10.2 # PyCaret과 함께 필요한 모델 라이브러리(XGBoost, LightGBM, catboost 등)를 모두 설치
pip install pandas scikit-learn
pip install tensorflow
pip freeze > requirements.txt

# mlflow
mlflow ui --backend-store-uri file:///home/jyc/.mlflow
mlflow ui --backend-store-uri "file:///D:/Sagi_JJU D/Git_Fork/AI_Deep_Learn/MlFlow/.mlflow"
```

pip install pycaret[full] pandas scikit-learn tensorflow mlflow==2.10.2