"""ANOMALY DETECTION SETUP"""
import pandas as pd
import numpy as np
import os
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from joblib import dump, load

def get_columns(n):
    f = []
    for x in range(1, n+1):
        f.append("F"+str(x))
    f.append("L")
    return f
    
#Create empty data frame
def create_empty_df(n):
    d = ([0.] * n)
    d.append(0)
    dfx = pd.DataFrame([d], columns = get_columns(n))
    dfx.drop(dfx.index[0], inplace = True)
    return dfx
    
#Create data frame with one row
def create_df(vals: list, label: int = 0):
    if not isinstance(vals, list):
        raise TypeError
    dfx = pd.DataFrame([vals + [label]], columns = get_columns(len(vals)))
    return dfx

def run(raw_data):
    length = 5
    filename = 'model.joblib'
    
    df_epis = create_empty_df(length)
    for id in raw_data.id.unique():
        print("Convert data for: ", id)
        df2 = raw_data.loc[raw_data['id'] == id]
        epi = []
        ano = []
        for index, row in df2.iterrows():
            epi.append(row['value'])
            ano.append(row['label'])
            if len(epi) == length:
                l_anomaly = 0
                for i in range(len(ano)):
                    if ano[i] == 1:
                        l_anomaly = 1
                        break
                df_row = create_df(epi,l_anomaly) 
                df_epis = pd.concat([df_epis, df_row], ignore_index=True)
                del(epi[0]) 
                del(ano[0])      

    """EXTRACT FEATURE COLUMNS"""
    feature_cols = list(df_epis.columns[:-1])
    target_col = df_epis.columns[-1]
    X_all = df_epis[feature_cols]
    Y_all = df_epis[target_col]

    X_train, X_test, y_train, y_test = train_test_split(X_all, Y_all, test_size = 0.33, random_state = 42)

    my_random_seed = 42
    model = DecisionTreeClassifier(random_state = my_random_seed)
    model.fit(X_train.values, y_train.values)

    with open(filename, 'wb') as file:
        dump(model, file)

    class AnomalyDetection(object):
        def __init__(self):
            self.model_file = os.environ.get('MODEL_FILE', filename)
            self.clf = load(open(self.model_file, 'rb'))

        def predict(self, X, feature_names):
            prediction = self.clf.predict(X)
            return prediction
        
    anomaly_detector = AnomalyDetection()
    predictions = anomaly_detector.predict(X_test, feature_names=feature_cols)
    return predictions
    