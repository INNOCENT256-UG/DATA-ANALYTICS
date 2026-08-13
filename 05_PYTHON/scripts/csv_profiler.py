from pathlib import Path

import pandas as pd


def profile_csv(file_path: str) -> None:
    """Display a basic data-quality profile for a CSV file."""

    path = Path(file_path)

    if not path.exists():
        print(f"Error: File not found: {path}")
        return

    if path.suffix.lower() != ".csv":
        print("Error: The file must be a CSV.")
        return

    try:
        df = pd.read_csv(path)
    except Exception as error:
        print(f"Error reading CSV: {error}")
        return

    print("\n=== CSV PROFILE ===")
    print(f"File: {path.name}")
    print(f"Rows: {df.shape[0]:,}")
    print(f"Columns: {df.shape[1]:,}")

    print("\n=== COLUMNS ===")
    print(df.columns.tolist())

    print("\n=== DATA TYPES ===")
    print(df.dtypes)

    print("\n=== MISSING VALUES ===")
    print(df.isna().sum())

    print("\n=== DUPLICATE ROWS ===")
    print(df.duplicated().sum())

    print("\n=== UNIQUE VALUES ===")
    print(df.nunique())

    print("\n=== NUMERIC SUMMARY ===")
    print(df.describe())


if __name__ == "__main__":
    file_path = input("Enter CSV file path: ").strip()
    profile_csv(file_path)