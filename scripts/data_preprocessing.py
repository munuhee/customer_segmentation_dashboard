import pandas as pd
from sklearn.preprocessing import StandardScaler
from pathlib import Path

def load_data(filepath):
    if not filepath.is_file():
        raise FileNotFoundError(
            f"The file at {filepath} does not exist."
        )
    return pd.read_csv(filepath)

def preprocess_data(df):
    # Drop duplicates and missing values
    df.drop_duplicates(inplace=True)
    df.dropna(subset=['CustomerID'], inplace=True)

    # Convert date to datetime and calculate recency
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    max_date = df['InvoiceDate'].max()
    df['Recency'] = (max_date - df['InvoiceDate']).dt.days

    # Remove transactions with negative or zero amounts
    df = df[df['UnitPrice'] > 0]

    # Aggregate data to get total spend and frequency
    df_agg = df.groupby('CustomerID').agg({
        'InvoiceNo': 'nunique',
        'Quantity': 'sum',
        'Recency': 'mean'
    }).rename(columns={'InvoiceNo': 'Frequency', 'Quantity': 'TotalSpend'})

    # Standardize features
    scaler = StandardScaler()
    df_agg[['TotalSpend', 'Frequency', 'Recency']] = scaler.fit_transform(df_agg[['TotalSpend', 'Frequency', 'Recency']])

    return df_agg

if __name__ == "__main__":
    current_dir = Path(__file__).resolve().parent
    filepath = current_dir.parent / 'data' / 'online_retail.csv'

    print(f"Current Directory: {current_dir}")
    print(f"Loading data from {filepath}...")

    try:
        df = load_data(filepath)
        df_agg = preprocess_data(df)
        df_agg.to_csv(current_dir.parent / 'data' / 'customer_data_preprocessed.csv', index=True)
        print("Data preprocessing complete.")
    except Exception as e:
        print(f"An error occurred: {e}")
