import numpy as np
import pandas as pd
import pickle
from flask import Flask
from flask import request
from sklearn.metrics import accuracy_score

plckd_model = pickle.load(open('churn_model.pkl', 'rb'))

X_test = pd.read_csv('X_test.csv')
preds = np.loadtxt('preds.csv')

new_preds = plckd_model.predict(X_test)

eq_arrays = (preds == new_preds).all()
print(eq_arrays)

app = Flask(__name__)


@app.route('/prediction')
def predict():
    is_male = float(request.args.get("is_male"))
    num_inters = float(request.args.get("num_inters"))
    late = float(request.args.get("late"))
    age = float(request.args.get("age"))
    years_contract = float(request.args.get("years_contract"))

    data = [is_male, num_inters, late, age, years_contract]

    data = np.array(data).reshape(-1, len(data))
    prediction = plckd_model.predict(data)

    if prediction == 0:
        return 'The client will not churn.'

    if prediction == 1:
        return 'The client will churn.'


if __name__ == '__main__':
    app.run(port=4444, debug=True)
