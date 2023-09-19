import os
import pandas as pd
from tqdm import tqdm
import matplotlib.pyplot as plt

def clean_csv(file_path):
    try:
        df = pd.read_csv(file_path)

        df = df.dropna()

        df.to_csv(file_path, index=False)

        print(f"Cleaning successful. Cleaned data written to {file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

def print_na_column(file_path):
    df = pd.read_csv(file_path)
    na_columns = df.columns[df.isna().any()].tolist()
    print("Columns with NaN values:", na_columns)

def plot_na_values(csv_file):
    df = pd.read_csv(csv_file)

    na_counts = df.isna().sum()

    plt.figure(figsize=(15, 8))
    ax = na_counts.plot(kind='bar', color='skyblue')
    plt.title('Number of NA Values in Each Feature')
    plt.xlabel('Features')
    plt.ylabel('Number of NA Values')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    plt.show()


def create_elos_for_human():
    # Load datasets
    elos = pd.read_csv('data/useful/sequential_elos.csv')
    alias = pd.read_csv('data/useful/alias.csv')

    # Merge the two datasets on 'playerid'
    elos_for_human = pd.merge(elos, alias, on='playerid', how='inner')

    # Select only the columns you want
    elos_for_human = elos_for_human[['playername', 'elo']]

    # Order by 'elo' column in descending order
    elos_for_human = elos_for_human.sort_values(by='elo', ascending=False).reset_index(drop=True)

    # Save the resulting DataFrame to a new CSV file
    elos_for_human.to_csv('data/useful/elos_for_human.csv', index=False)



create_elos_for_human()

