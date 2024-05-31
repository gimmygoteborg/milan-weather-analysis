import os
import pandas as pd

def read_csv_files_from_folder(folder_path):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"The folder {folder_path} does not exist.")
        return

    # List all files in the folder
    files = os.listdir(folder_path)

    # Filter out the CSV files
    csv_files = [file for file in files if file.endswith('.csv')]

    # Read and print the contents of each CSV file
    for csv_file in csv_files:
        file_path = os.path.join(folder_path, csv_file)
        try:
            # Extract year from filename
            year = int(csv_file[:4])
            
            # Custom date parser
            date_parser = lambda x: pd.to_datetime(f"{year}-05-{x.split(' ')[1]}", format='%Y-%m-%d', errors='coerce')
            
            # Read only the "date" and "prec" columns
            df = pd.read_csv(file_path, usecols=["date", "prec"], parse_dates=["date"], date_parser=date_parser)
            
            # Filter dataframe based on year
            df_year = df[df['date'].dt.year == year]
            
            print(f"Contents of {csv_file} (date and prec columns) for year {year}:")
            print(df_year)
            print("\n")
        except Exception as e:
            print(f"An error occurred while reading {csv_file}: {e}")
