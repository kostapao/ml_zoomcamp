from flask import Flask
from flask import jsonify
from flask import request
import pickle

app = Flask('churn')


with open('dv.bin', 'rb') as dv_file_in:
    dv = pickle.load(dv_file_in)

with open('model1.bin', 'rb') as model_file_in:
    model = pickle.load(model_file_in)

def predict_single(customer, dv, model):
    X = dv.transform(customer)
    y_pred = model.predict_proba(X)[:, 1]
    return y_pred
    

@app.route("/predict", methods = ['POST'])
def predict():
    customer = request.get_json()
    prediction = predict_single(customer,dv,model)
    response = {
        'churn_probability':float(prediction),
        'churn':bool(prediction > 0.5)

    }
    return jsonify(response)



if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 9696)
    