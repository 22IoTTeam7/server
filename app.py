import joblib
from flask import Flask, request, json
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

'''floor2 = joblib.load('floor2Model')
floor4 = joblib.load('floor4Model')
floor5 = joblib.load('floor5Model')'''

app = Flask(__name__)


@app.route('/')
def t():
    test = "Test"
    response = app.response_class(
        response=json.dumps(test),
        status=200
    )
    return response

@app.route('/location', methods=['GET', 'POST'])
def location():
    content = request.get_json()
    req_data = np.array([content['AP1'], content['AP2'], content['AP3'], content['AP4'], content['AP5']])
    floor = content['Floor']

    if floor == 2:
        return floor2.predict(req_data)
    if floor == 4:
        return floor4.predict(req_data)
    if floor == 5:
        return floor5.predict(req_data)


if __name__ == '__main__':
    app.run()
