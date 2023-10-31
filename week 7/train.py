import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score as acc
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction import DictVectorizer
import numpy as np

def clean_data(df: pd.DataFrame):
    cols = ['Age', 'Sex', 'Income', 'WaistCirc', 'BMI',
            'UrAlbCr', 'UricAcid', 'BloodGlucose', 'HDL', 'Triglycerides', 'MetabolicSyndrome']
    MeanIncome = df.Income.mean()
    df.loc[df.Income.isnull(), 'Income'] = np.round(MeanIncome,2)
    # df['AboveAverageIncome'] = df.Income.apply(lambda x: x > MeanIncome)
    df.loc[df.BMI.isnull(), 'BMI'] = np.round(df.BMI.mean(), 1)
    df.loc[df.WaistCirc.isnull(), 'WaistCirc'] = np.round(df.WaistCirc.mean(), 1)
    df = df[cols]
    return df

data = pd.read_csv('Metabolic Syndrome.csv')
data_clean = clean_data(data)
y_value = data_clean.pop('MetabolicSyndrome')

dv = DictVectorizer(sparse=True)

X_train, X_test, y_train, y_test = train_test_split(data_clean, y_value, train_size=0.6, random_state=42)

data_processed = dv.fit_transform(X_train.to_dict(orient='records'))
test_processed = dv.transform(X_test.to_dict(orient='records'))

rfc = RandomForestClassifier(max_depth=11, n_estimators=60, n_jobs=-1,
                       random_state=42)
rfc.fit(data_processed, y_train)

y_pred = rfc.predict(test_processed) >= 0.5
print(f"Accuracy: {acc(y_test, y_pred):.3f}")

with open('rfc.bin', 'wb') as f:
    pickle.dump(rfc, f)
with open('dv.bin', 'wb') as f:
    pickle.dump(dv, f)