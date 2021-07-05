import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn import metrics

# Label = SeriousDlqin2yrs

train = pd.read_csv("train2.csv",index_col=0)
test = pd.read_csv("test2.csv",index_col=0)

target = 'SeriousDlqin2yrs'
y_train = train[target].values
X_train = train.drop(target,axis=1).values
y_test = test[target].values
X_test = test.drop(target,axis=1).values

# model

model = XGBClassifier()
model.fit(X_train,y_train)

y_pred = model.predict_proba(X_test)
y_pred = y_pred[:,1]

data = {'pred' : y_pred}
df = pd.DataFrame(data)
df.to_csv('test2-predictions.csv')


# print(metrics.roc_auc_score(y_test,y_pred))
# 0.8580
