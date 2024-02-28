import pandas as pd
import os

if __name__ == "__main__":

    # Get the directory path of the current script
    current_dir = os.path.dirname(__file__)
    parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))\

    ##Get file directory of unjoined datasets
    file_path = os.path.join(parent_dir, 'Datasets')
    excel_files = [file for file in os.listdir(file_path) if file.endswith('.xls')]

    # Initialize an empty list to store DataFrames
    dfs = []

    # Loop through each Excel file and read it into a DataFrame
    for file in excel_files:
        xls = os.path.join(file_path, file)
        df = pd.read_excel(xls)
        dfs.append(df)

    # Concatenate all DataFrames into a single DataFrame
    combined_df = pd.concat(dfs, ignore_index=True)

    print(combined_df)

    combined_df.to_csv('../Datasets/Contributors 2011-2022.csv', index=False)

