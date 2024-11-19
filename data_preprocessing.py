import pandas as pd

def load_and_preprocess_data(file_path):
    df = pd.read_csv(file_path)
    df = df[df['JAHR'] <= 2021]
    df = df[['MONATSZAHL', 'AUSPRAEGUNG', 'JAHR', 'MONAT', 'WERT']]
    df.columns = ['Category', 'Accident-type', 'Year', 'Month', 'Value']
    
    df['Date'] = pd.to_datetime(df['Month'], format='%Y%m', errors='coerce')
    df = df.dropna(subset=['Date'])
    df = df.drop(columns=['Year', 'Month'])
    df.set_index('Date', inplace=True)
    df.sort_index(inplace=True)
    
    return df

def filter_by_category(df, category='Alkoholunfälle', accident_type='insgesamt'):
    alkohol_dt = df[(df['Category'] == category) & (df['Accident-type'] == accident_type)]
    alkohol_dt = alkohol_dt[['Value']]
    alkohol_dt = alkohol_dt.sort_index()
    return alkohol_dt