# data_reader.py
import os
import pandas as pd

def read_precipitation_data(folder_path):
    """
    Read precipitation data from CSV files in the specified folder.

    Parameters:
        folder_path (str): Path to the folder containing the CSV files.

    Returns:
        dict: A dictionary where keys are years and values are DataFrames containing the precipitation data for each year.
    """
    precipitation_data = {}

    # List all files in the folder
    files = os.listdir(folder_path)

    # Filter out the CSV files
    csv_files = [file for file in files if file.endswith('.csv')]

    # Read precipitation data for each CSV file
    for csv_file in csv_files:
        file_path = os.path.join(folder_path, csv_file)
        try:
            # Extract year from filename
            year = int(csv_file[:4])

            # Read only the "date" and "prec" columns
            df = pd.read_csv(file_path, usecols=["date", "prec"])

            # Store data in the dictionary
            precipitation_data[year] = df
        except Exception as e:
            print(f"An error occurred while processing {csv_file}: {e}")

    return precipitation_data
