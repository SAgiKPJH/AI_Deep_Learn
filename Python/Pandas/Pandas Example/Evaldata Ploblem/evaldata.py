import pandas as pd

path = 'Python/Pandas/Pandas Example/Evaldata Ploblem/evaldata.csv'
evaldata = pd.read_csv(path)
evaldata.head()

# 메서드 정의
## 원하는 평가자(evaluator) 별 원하는 데이터(get_value) Min_Max 계산
def min_max_evaluator(df, get_value, evaluator):
    group = df.groupby(df[evaluator])
    min = group[get_value].min()
    max = group[get_value].max()
    return (df[get_value] - min[df[evaluator]].values)/(max[df[evaluator]].values - min[df[evaluator]].values)

## 원하는 평가자(evaluator) 별 원하는 데이터(get_value) Standardization 계산
def standardization_evaluator(df, get_value, evaluator):
    group = df.groupby(df[evaluator])
    mean = group[get_value].mean()
    std = group[get_value].std()
    return (df[get_value] - mean[df[evaluator]].values)/ std[df[evaluator]].values

# score1, score2, score3 데이터 정규화 진행
evaldata['score1_min_max'] = min_max_evaluator(evaldata, 'score1', 'evaluator')
evaldata['score2_min_max'] = min_max_evaluator(evaldata, 'score2', 'evaluator')
evaldata['score3_min_max'] = min_max_evaluator(evaldata, 'score3', 'evaluator')
evaldata['score_sum_mix_max'] = (evaldata['score1_min_max'] + evaldata['score2_min_max'] + evaldata['score3_min_max']) / 3

evaldata['score1_standardization'] = standardization_evaluator(evaldata, 'score1', 'evaluator')
evaldata['score2_standardization'] = standardization_evaluator(evaldata, 'score2', 'evaluator')
evaldata['score3_standardization'] = standardization_evaluator(evaldata, 'score3', 'evaluator')
evaldata['score_sum_standardization'] = (evaldata['score1_standardization'] + evaldata['score2_standardization'] + evaldata['score3_standardization']) / 3

# Project 별 정규화 평균 값 획득
projects_min_max = evaldata['score_sum_mix_max'].groupby(evaldata['project']).mean()
projects_standardization = evaldata['score_sum_standardization'].groupby(evaldata['project']).mean()

# Top 5 선정
top5_min_max = projects_min_max.sort_values(ascending=False).head(5)
top5_standardization = projects_standardization.sort_values(ascending=False).head(5)

print("score1, score2, score3 각자 평가자별 점수 비율 반영된 top5 선정 입니다")
print(f"\nTop5 Min-Max\n{top5_min_max}")
print(f"\nTop5 Standardization\n{top5_standardization}")