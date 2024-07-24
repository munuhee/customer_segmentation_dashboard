import pandas as pd
from sklearn.cluster import KMeans
from pathlib import Path

def perform_clustering(df, n_clusters=4):
    kmeans = KMeans(n_clusters=n_clusters, random_state=0)
    df['Cluster'] = kmeans.fit_predict(
        df[['TotalSpend', 'Frequency', 'Recency']]
    )
    return df

if __name__ == "__main__":
    current_dir = Path(__file__).resolve().parent
    df = pd.read_csv(
        current_dir.parent / 'data' / 'customer_data_preprocessed.csv', index_col=0
    )
    df_clustered = perform_clustering(df, n_clusters=4)
    df_clustered.to_csv(
        current_dir.parent / 'data' / 'customer_data_clustered.csv', index=True
    )
    print("Clustering complete.")
