# file for Flask related homework
from flask import Flask
from flask import request
from flask import jsonify
import pickle 
import sklearn
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestClassifier
import numpy as np

with open('dv.bin', 'rb') as f:
    dv = pickle.load(f)
    
with open('rfc.bin', 'rb') as f:
    model = pickle.load(f)
    
app = Flask('week7midterm')

@app.route('/predict', methods=['POST'])
def predict():
    sample = request.get_json()
    X = dv.transform([sample])
    y_pred = np.round(model.predict(X)[0], 3)
    y_res =  bool(y_pred >= 0.5)
    output = f"Person has {'presence' if (y_res) else 'absence'} of metabolic syndrome"
    result = {
        'probability': float(y_pred),
        'result': output
    }
    return result

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=9696)