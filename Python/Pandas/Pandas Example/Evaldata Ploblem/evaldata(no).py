import pandas as pd

path = 'Python/Pandas/Pandas Example/Evaldata Ploblem/evaldata.csv'
evaldata = pd.read_csv(path)
evaldata.head()

def min_max(df):
    return (df - df.min())/(df.max() - df.min())
def standardization(df):
    return (df - df.mean()) / df.std()

evaldata['score_sum'] = evaldata.score1 + evaldata.score2 + evaldata.score3
evaldata['min-max'] = min_max(evaldata['score_sum'])
evaldata['standardization'] = standardization(evaldata['score_sum'])

top5_min_max = evaldata.sort_values(by=['min-max', 'index'], ascending=[False, True])[['index', 'project']].head(5)
top5_standardization = evaldata.sort_values(by=['standardization', 'index'], ascending=[False, True])[['index', 'project']].head(5)

print("점수는 동일해도 index가 낮은 순으로 top5 선정")
print(f"\nTop5 Min-Max\n{top5_min_max}")
print(f"\nTop5 Standardization\n{top5_standardization}")