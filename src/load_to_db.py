import os
import pandas as pd
from sqlalchemy import create_engine

DATA_DIR = "data/processed"
DB_PATH = "data/document_pipeline.db"

def main():
    csv_files = [f for f in os.listdir(DATA_DIR) if f.endswith(".csv")]

    if not csv_files:
        print("No CSV files found")
        return

    csv_file = csv_files[0]
    csv_path = os.path.join(DATA_DIR, csv_file)

    print(f"Loading {csv_path} into database")

    df = pd.read_csv(csv_path)

    engine = create_engine(f"sqlite:///{DB_PATH}")

    table_name = "document_lines"

    df.to_sql(table_name, engine, if_exists="replace", index=False)

    print(f"Data loaded into SQLite database at {DB_PATH}")
    print(f"Table name: {table_name}")
    print(df.head())

if __name__ == "__main__":
    main()

