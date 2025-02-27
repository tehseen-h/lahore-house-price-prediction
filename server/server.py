from flask import Flask, request, jsonify, render_template
import pickle
import json
import numpy as np

app = Flask(__name__)

import os

# Get the base directory (where server.py resides)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load the model
try:
    model_path = os.path.join(BASE_DIR, '../model/Lahore_Real_Estate_Price_Prediction_model.pickle')
    with open(model_path, 'rb') as f:
        lr_clf = pickle.load(f)
except FileNotFoundError:
    raise FileNotFoundError("The model file path is incorrect. Please check 'Lahore_Real_Estate_Price_Prediction_model.picle' in the 'model' directory.")

# Load the columns
try:
    columns_path = os.path.join(BASE_DIR, '../model/columns.json')
    with open(columns_path, 'r') as f:
        data_columns = json.load(f)['data_columns']
except FileNotFoundError:
    raise FileNotFoundError("The columns file path is incorrect. Please check 'columns.json' in the 'model' directory.")

# Extract locations without 'Location_' prefix
locations = [col.split("Location_")[1] for col in data_columns if "Location_" in col]


@app.route('/')
def home():
    return render_template("index.html", locations=locations)


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Retrieve and validate input values
        area_value = request.form.get('area_value')
        area_unit = request.form.get('area_unit')
        location = request.form.get('location')
        baths = request.form.get('baths')
        beds = request.form.get('beds')
        types = request.form.get('type')

        # Check if all fields are filled
        if not all([area_value, area_unit, location, baths, beds, types]):
            return render_template('index.html',
                                   prediction_text="Please fill in all the fields.",
                                   locations=locations)

        area_value = float(area_value)

        # Check for negative area input
        if area_value <= 0:
            return render_template('index.html',
                                   prediction_text="Area must be a positive number.",
                                   locations=locations)

        # Convert Marla/Kanal to Square Feet
        if area_unit == "Marla":
            sqft = area_value * 225  # 1 Marla = 225 square feet
        elif area_unit == "Kanal":
            sqft = area_value * 4500  # 1 Kanal = 4500 square feet
        else:
            return render_template('index.html',
                                   prediction_text="Invalid area unit. Please select Marla or Kanal.",
                                   locations=locations)

        # Prepare input array for prediction
        location_column = f"Location_{location}"
        loc_index = -1
        if location_column in data_columns:
            loc_index = data_columns.index(location_column)

        # Initialize input array with zeros
        x = np.zeros(len(data_columns))
        x[0] = int(baths)   # Bath(s)
        x[1] = int(beds)    # Bedroom(s)
        x[2] = sqft         # Square foot input

        if loc_index >= 0:
            x[loc_index] = 1  # Set location column to 1

        x[-1] = int(types)  # Type (Flat or House)

        # Predict the price
        prediction = lr_clf.predict([x])[0]
        price = round(prediction, 2)

        # Check if prediction is negative
        if price < 0:
            return render_template('index.html',
                                   prediction_text="All requirements are not satisfied. Please try again.",
                                   locations=locations)

        # Return the prediction result
        return render_template('index.html',
                               prediction_text=f'Estimated Price: {price} PKR',
                               locations=locations)
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
