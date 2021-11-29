from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_Locality_names', methods=['GET'])
def get_Locality_names():
    response = jsonify({
        'Locality': util.get_locality_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    Area = float(request.form['Area'])
    Locality = request.form['Locality']
    BHK = int(request.form['BHK'])
    Bathroom = int(request.form['Bathroom'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(Locality,Area,Bathroom,BHK)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()