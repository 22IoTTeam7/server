import joblib
from flask import Flask, request, json
import numpy as np

floor2 = joblib.load('floor2Model.pkl')
floor4 = joblib.load('floor4Model.pkl')
floor5 = joblib.load('floor5Model.pkl')

app = Flask(__name__)


@app.route('/')
def t():
    test = "Test"
    response = app.response_class(
        response=json.dumps(test),
        status=200
    )
    return response


@app.route('/location/floor2', methods=['GET', 'POST'])
def location():
    content2 = request.get_json()
    req_data = np.array([content2['AP1'], content2['AP2'], content2['AP3'], content2['AP4'], content2['AP5'],
                         content2['AP6'], content2['AP7'], content2['AP8'], content2['AP9'], content2['AP10'],
                         content2['AP11'], content2['AP12'], content2['AP13'], content2['AP14'], content2['AP15'],
                         content2['AP16'], content2['AP17'], content2['AP18'], content2['AP19'], content2['AP20'],
                         content2['AP21'], content2['AP22'], content2['AP23'], content2['AP24'], content2['AP25'],
                         content2['AP26'], content2['AP27'], content2['AP28'], content2['AP29'], content2['AP30'],
                         content2['AP31'], content2['AP32'], content2['AP33']
                         ])
    floor = content2['Floor']

    if floor == 2:
        return floor2.predict(req_data)


@app.route('/location/floor4', methods=['GET', 'POST'])
def location():
    content4 = request.get_json()
    req_data = np.array([content4['AP1'], content4['AP2'], content4['AP3'], content4['AP4'], content4['AP5'],
                         content4['AP6'], content4['AP7'], content4['AP8'], content4['AP9'], content4['AP10'],
                         content4['AP11'], content4['AP12'], content4['AP13'], content4['AP14'], content4['AP15'],
                         content4['AP16'], content4['AP17'], content4['AP18'], content4['AP19'], content4['AP20'],
                         content4['AP21'], content4['AP22'], content4['AP23'], content4['AP24'], content4['AP25'],
                         content4['AP26'], content4['AP27'], content4['AP28'], content4['AP29'], content4['AP30'],
                         content4['AP31'], content4['AP32'], content4['AP33'], content4['AP34'], content4['AP35'],
                         content4['AP36'], content4['AP37'], content4['AP38'], content4['AP39'], content4['AP40'],
                         content4['AP41'],  content4['AP42'], content4['AP43'], content4['AP44']
                         ])
    floor = content4['Floor']

    if floor == 4:
        return floor4.predict(req_data)


@app.route('/location/floor5', methods=['GET', 'POST'])
def location():
    content5 = request.get_json()
    req_data = np.array([content5['AP1'], content5['AP2'], content5['AP3'], content5['AP4'], content5['AP5'],
                         content5['AP6'], content5['AP7'], content5['AP8'], content5['AP9'], content5['AP10'],
                         content5['AP11'], content5['AP12'], content5['AP13'], content5['AP14'], content5['AP15'],
                         content5['AP16'], content5['AP17'], content5['AP18'], content5['AP19'], content5['AP20'],
                         content5['AP21'], content5['AP22'], content5['AP23'], content5['AP24'], content5['AP25'],
                         content5['AP26'], content5['AP27'], content5['AP28'], content5['AP29'], content5['AP30'],
                         content5['AP31'], content5['AP32'], content5['AP33'], content5['AP34'], content5['AP35'],
                         content5['AP36'], content5['AP37'], content5['AP38'], content5['AP39'], content5['AP40'],
                         content5['AP41'], content5['AP42'], content5['AP43'], content5['AP44'], content5['AP45'],
                         content5['AP46'], content5['AP47'], content5['AP48'], content5['AP49']
                         ])
    floor = content5['Floor']

    if floor == 5:
        return floor5.predict(req_data)


if __name__ == '__main__':
    app.run()
