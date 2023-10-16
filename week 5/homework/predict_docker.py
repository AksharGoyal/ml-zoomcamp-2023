# file for Flask related homework
from flask import Flask
from flask import request
from flask import jsonify
import pickle 

with open('dv.bin', 'rb') as f:
    dv = pickle.load(f)
    
with open('model2.bin', 'rb') as f:
    model = pickle.load(f)
    
app = Flask('hw5q4')

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    y_res =  (y_pred >= 0.5)
    
    result = {
        'probability': float(y_pred),
        'result': bool(y_res)
    }
    return result

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=9696)