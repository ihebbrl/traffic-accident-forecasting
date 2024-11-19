import pandas as pd
import matplotlib.pyplot as plt
from data_preprocessing import load_and_preprocess_data, filter_by_category
from visualization import plot_category_accidents, plot_alkohol_accidents
from model import train_sarimax_model, forecast_validation_period, forecast_test_period, calculate_mse

# Load and preprocess data
file_path = "data/monatszahlen2405_verkehrsunfaelle_export_31_05_24_r.csv"
df = load_and_preprocess_data(file_path)

# Group by category and visualize
category_accidents = df.groupby('Category')['Value'].sum()
plot_category_accidents(category_accidents, save_path='images/category_accidents.png')

# Filter for alcohol-related accidents
alkohol_dt = filter_by_category(df)
january_points = alkohol_dt[alkohol_dt.index.month == 1]
plot_alkohol_accidents(alkohol_dt, january_points, save_path='images/alkohol_accidents.png')

# Split the data into train, validation, and test sets
train = alkohol_dt[:'2018-12-01']
validation = alkohol_dt['2019-01-01':'2020-12-01']
test = alkohol_dt['2021-01-01':'2021-01-01']

# Train the SARIMAX model
model_fit = train_sarimax_model(train['Value'])

# Forecast the validation period
forecast_values_validation = forecast_validation_period(model_fit, len(validation))

# Plot forecast vs actual values for validation (save plot)
plt.figure(figsize=(10, 6))
plt.plot(validation.index, validation['Value'], label='Actual (Validation)', color='green')
plt.plot(validation.index, forecast_values_validation, label='Forecast (Validation)', color='red')
plt.legend()
plt.savefig('images/forecast_validation.png')
plt.close()

# Forecast the test period (January 2021)
forecast_value_test = forecast_test_period(model_fit)
print(f"Forecasted value for January 2021: {forecast_value_test}")

# Actual value for January 2021
actual_value_test = test['Value'].iloc[0]
print(f"Actual value for January 2021: {actual_value_test}")

# Calculate MSE
mse = calculate_mse(actual_value_test, forecast_value_test)
print(f"Mean Squared Error (MSE) for Test Set: {mse}")