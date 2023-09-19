import pandas as pd
from tqdm import tqdm

def incorporate_player_data(df):
    df_player_data = pd.read_csv('data/useful/player_data.csv')

    roles = ['top_1', 'jng_1', 'mid_1', 'bot_1', 'sup_1', 'top_2', 'jng_2', 'mid_2', 'bot_2', 'sup_2']

    df = df[["result"] + roles]

    for role in tqdm(roles, desc="Processing roles"):
        df = df.rename(columns={role: "playerid"})

        df = pd.merge(df, df_player_data, on="playerid")

        for col in df_player_data.columns:
            if col != 'playerid':
                df = df.rename(columns={col: f'avg_{col}_{role}'})

        df = df.rename(columns={"playerid": role})

    df = df.drop(columns=roles)
    return df