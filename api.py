import pandas as pd
from sklearn import metrics
from flask import Flask , request

# comparer test2_pred et test2 Seriousmachin chouette 


app = Flask(__name__)
@app.route('/pred', methods=['POST'])
def hello():
    file_pred = request.files['file']
    df = pd.read_csv(file_pred,index_col=0)
    y_pred = df['pred'].values

    test = pd.read_csv('test2.csv',index_col=0)
    target = 'SeriousDlqin2yrs'
    y_test = test[target].values

    roc_auc = metrics.roc_auc_score(y_test,y_pred)


    return str(roc_auc)