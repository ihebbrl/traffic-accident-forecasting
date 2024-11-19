from sklearn.metrics import mean_squared_error
from statsmodels.tsa.statespace.sarimax import SARIMAX

def train_sarimax_model(train_data):
    model = SARIMAX(train_data, seasonal_order=(1, 1, 1, 12))
    model_fit = model.fit()
    return model_fit

def forecast_validation_period(model_fit, validation_data_length):
    forecast_validation = model_fit.get_forecast(steps=validation_data_length)
    forecast_values_validation = forecast_validation.predicted_mean
    return forecast_values_validation

def forecast_test_period(model_fit):
    forecast_test = model_fit.get_forecast(steps=1)
    forecast_value_test = forecast_test.predicted_mean.iloc[0]
    return forecast_value_test

def calculate_mse(actual_value_test, forecast_value_test):
    mse = mean_squared_error([actual_value_test], [forecast_value_test])
    return mse