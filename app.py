from flask import Flask, request, jsonify
from model import train_sarimax_model
import pandas as pd
from data_preprocessing import load_and_preprocess_data, filter_by_category

# Load and preprocess data
file_path = "data/monatszahlen2405_verkehrsunfaelle_export_31_05_24_r.csv"
df = load_and_preprocess_data(file_path)

# Filter for alcohol-related accidents
alkohol_dt = filter_by_category(df)

# Create a Flask app
app = Flask(__name__)

# Define the endpoint to get the prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the data from the POST request
        data = request.get_json()
        year = data['year']
        month = data['month']
        
        # Prepare the datetime index for the input
        input_date = pd.to_datetime(f"{year}-{month}-01")
        
        train_data = alkohol_dt[:input_date]  # Train up to the input date
        model = train_sarimax_model(train_data['Value'])
        
        # Forecast using the SARIMAX model
        forecast = model.get_forecast(steps=1)
        prediction = forecast.predicted_mean.iloc[0]
        
        # Return the prediction in the specified format
        return jsonify({"prediction": prediction})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)