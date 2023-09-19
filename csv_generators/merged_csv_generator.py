import os
from tqdm import tqdm
import pandas as pd

def merge_csv_files(input_folder, output_file):
    csv_files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]

    dfs = []

    for file in tqdm(csv_files, desc='Merging CSV files'):
        file_path = os.path.join(input_folder, file)
        df = pd.read_csv(file_path)
        dfs.append(df)

    merged_data = pd.concat(dfs, ignore_index=True)

    merged_data.to_csv(output_file, index=False)

    print(f'Merged data saved to {output_file}')

merge_csv_files("data/raw_data", "data/useful/merged_data.csv")