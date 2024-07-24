# Customer Segmentation and Insights Dashboard

## Project Overview
Involves analyzing an e-commerce dataset to segment customers and visualize insights using an interactive dashboard.
Provides actionable insights into customer behavior and spending patterns.

## Dataset
The dataset used is the "Online Retail" dataset from the UCI Machine Learning Repository.

## Project Structure
- `data/`: Contains the raw and preprocessed data files.
- `notebooks/`: Contains the Jupyter notebook with data analysis and visualization.
- `scripts/`: Contains scripts for data preprocessing and customer segmentation.
- `app/`: Contains the Dash app for interactive visualization.
- `README.md`: Project documentation.

## Setup and Installation
1. Clone the repository.
2. Install the required packages:
   ```bash
   pip install numpy pandas seaborn matplotlib scikit-learn dash plotly
3. Run the data preprocessing script:
   ```bash
   python scripts/data_preprocessing.py
   ```
4. Perform customer segmentation:
   ```bash
   python scripts/customer_segmentation.py
   ```
5. Launch the interactive dashboard:
   ```bash
   python app/app.py
   ```

## Key Insights
1. Customers are segmented into different clusters based on their spending, frequency, and recency.
2. Visualizations provide insights into spending patterns and customer behavior by cluster.