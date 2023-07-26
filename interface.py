from flask import Flask, request, render_template, jsonify
from utils import Shopping
import config

app = Flask(__name__)

@app.route('/shopping_spendings')
def home1():
    return render_template('index.html')

@app.route('/home')
def home():
    print("Testing Home Page API")
    return render_template('test.html')

@app.route('/predict_spendings', methods=['GET', 'POST'])
def predict_spendings():
    print("Received request with method:", request.method)

    if request.method == 'GET':
        data = request.args
        print("Data :", data)

        CustomerID = data.get('CustomerID')
        print("CustomerID received:", CustomerID)

        if CustomerID is None:
            return jsonify({"error": "CustomerID is missing"}), 400

        try:
            CustomerID = int(CustomerID)
        except ValueError:
            return jsonify({"error": "Invalid CustomerID"}), 400

        Gender = data.get('Gender')
        Age = data.get('Age')
        Annual_Income = data.get('Annual_Income')

        if Gender is None or Age is None or Annual_Income is None:
            return jsonify({"error": "Gender, Age, or Annual_Income is missing"}), 400

        try:
            Age = int(Age)
            Annual_Income = float(Annual_Income)
        except ValueError:
            return jsonify({"error": "Invalid Age or Annual_Income"}), 400

        Obj = Shopping(CustomerID, Gender, Age, Annual_Income)
        predict_spendings = Obj.predict_spendings()
        return render_template('index.html', prediction=predict_spendings)

    elif request.method == 'POST':
        data = request.form
        print("Data :", data)

        CustomerID = data.get('CustomerID')
        print("CustomerID received:", CustomerID)

        if CustomerID is None:
            return jsonify({"error": "CustomerID is missing"}), 400

        try:
            CustomerID = int(CustomerID)
        except ValueError:
            return jsonify({"error": "Invalid CustomerID"}), 400

        Gender = data.get('Gender')
        Age = data.get('Age')
        Annual_Income = data.get('Annual_Income')

        if Gender is None or Age is None or Annual_Income is None:
            return jsonify({"error": "Gender, Age, or Annual_Income is missing"}), 400

        try:
            Age = int(Age)
            Annual_Income = float(Annual_Income)
        except ValueError:
            return jsonify({"error": "Invalid Age or Annual_Income"}), 400

        Obj = Shopping(CustomerID, Gender, Age, Annual_Income)
        predict_spendings = Obj.predict_spendings()
        return render_template('index.html', prediction=predict_spendings)

    return jsonify({"Message": "Unsuccessful"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=config.PORT_NUMBER)
