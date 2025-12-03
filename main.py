import pandas as pd
import sqlite3
import os
import logging

logging.basicConfig(level=logging.INFO)

def load_csv(path):
    logging.info(f"== Loading CSV file from: {path} ==")
    df = pd.read_csv(path)
    logging.info(f"Data loaded successfully with {df.shape[0]} rows and {df.shape[1]} columns.\n")
    return df

def transform_data(df):
    logging.info("== Transforming data... ==")
    logging.info(f"Initial data shape: {df.shape}")

    # Standardize column names to lowercase
    logging.info("Standardizing column names to lowercase...")
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    logging.info("Column names standardized.")

    # Remove duplicates based on 'show_id'
    logging.info("Removing duplicates based on 'show_id'...")
    df = df.drop_duplicates(subset=['show_id']).reset_index(drop=True)
    logging.info(f"Duplicates removed. Data now has {df.shape[0]} rows.")

    # Handle missing values
    logging.info("Handling missing values...")
    df = df.dropna(subset=['show_id', 'title'])
    logging.info(f"Missing values handled. Data now has {df.shape[0]} rows.")

    # Convert 'date_added' to datetime
    logging.info("Converting 'date_added' to datetime format...")
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
    logging.info("'date_added' conversion complete.")

    logging.info(f"Final data shape after transformation: {df.shape}")
    logging.info("Data transformation complete.\n")
    return df

def create_connection(db_path):
    logging.info(f"== Creating SQLite connection to: {db_path} ==")
    conn = sqlite3.connect(db_path)
    logging.info("Connection created successfully.\n")
    return conn

def write_to_sqlite(df, conn, table_name):
    logging.info(f"== Writing DataFrame to SQLite table: {table_name} ==")
    df.to_sql(table_name, conn, if_exists='replace', index=False, dtype={
        'show_id': 'TEXT PRIMARY KEY',
    })
    logging.info(f"Data written to table '{table_name}' successfully.\n")


def main():
    # Define file paths
    csv_path = "data\\netflix1.csv"
    db_path = "db\\netflix1.db"
    
    # Load CSV data into DataFrame
    logging.info("Starting ETL process...\n")
    
    # checking csv file existence
    if not os.path.exists(csv_path):
        logging.info(f"Error: The file {csv_path} does not exist.")
        return
    
    df = load_csv(csv_path)

    # Transform data
    df = transform_data(df)

    # Create SQLite connection
    conn = create_connection(db_path)
    
    # Write DataFrame to SQLite database
    write_to_sqlite(df, conn, 'netflix_shows')
    
    # Close the connection
    conn.close()
    logging.info("Connection closed successfully.\n")

    logging.info("ETL process completed successfully.")
if __name__ == "__main__":
    main()