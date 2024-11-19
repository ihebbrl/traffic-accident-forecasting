# traffic-accident-forecasting
This project involves forecasting the number of alcohol-related traffic accidents for January 2021 using historical data from the **München Open Data Portal**. The dataset contains monthly statistics for various categories of traffic accidents. Specifically, the goal is to predict the total number of alcohol-related accidents (`Category: 'Alkoholunfälle'`, `Type: 'insgesamt'`) for **January 2021** based on data up to **December 2020**.

## Requirements

- **Python 3.x**
- Required libraries: 
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `statsmodels`
  - `scikit-learn`

You can install the necessary dependencies by running:

```bash
pip install -r requirements.txt
```

## Dataset

The dataset is available on the **München Open Data Portal** and can be downloaded from:

[Monatszahlen Verkehrsunfälle Dataset](https://www.muenchen.de/open-data/)

### Preprocessing Steps
1. **Filter Data**: The data should only include records until **December 2020** for model training purposes.
2. **Focus on Category**: Only the category `Alkoholunfälle` (alcohol-related accidents) with `Accident-type` as `insgesamt` (total accidents) is considered for forecasting.

## Steps

### 1. Data Preprocessing

- **Loading Data**: The dataset is loaded and cleaned, ensuring the relevant columns are extracted.
- **Handling Missing Data**: Any rows with missing values are dropped.
- **Date Formatting**: The 'Month' and 'Year' columns are used to create a datetime index for the time series.

### 2. Visualization

- A bar plot is generated to visualize the total number of accidents per category.
- A time series plot is generated for alcohol-related accidents (`Alkoholunfälle`).
- Red dots are used to highlight the accident counts for January (to be forecasted).

### 3. Forecasting Model

A **SARIMAX** (Seasonal AutoRegressive Integrated Moving Average with eXogenous regressors) model is used to predict the number of alcohol-related accidents for January 2021 based on historical data. The model is trained on data from **2010-2020**, and a forecast for **January 2021** is generated.

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/traffic-accident-forecasting.git
   cd traffic-accident-forecasting
   ```

2. Download the dataset from the [München Open Data Portal](https://www.muenchen.de/open-data/) and place it in the project directory.

3. Run the main script to preprocess the data, visualize the results, and generate forecasts:
   ```bash
   python main.py
   ```

4. The results will be saved as image files in the project directory (e.g., `category_accidents.png`, `alkohol_and_january_points.png`, `forecast_validation.png`).