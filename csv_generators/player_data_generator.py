import pandas as pd

def add_num_games(df):
    num_games = pd.read_csv("data/useful/num_matches.csv")
    df = pd.merge(df, num_games, on="playerid", how="inner")
    return df

df = pd.read_csv("data/useful/merged_data.csv")

leagues_df = df.drop(columns=["result"])
leagues_df = df.groupby('playerid')['league'].agg(lambda x:x.value_counts().idxmax()).reset_index()
leagues_df = pd.get_dummies(data=leagues_df, columns=["league"])
print(leagues_df)

df = df[['playerid'] + df.select_dtypes(include='number').columns.tolist()]
df = df.drop(columns=["result"])
df = df.groupby('playerid').mean().reset_index()
df = add_num_games(df)

seq_elo = pd.read_csv("data/useful/sequential_elos.csv")
seq_elo.rename(columns={"elo": "seq_elo"}, inplace=True)


df = pd.merge(df, seq_elo, on="playerid", how="inner")

elo = pd.read_csv("data/useful/elos.csv")

df = pd.merge(df, elo, on="playerid", how="inner")

df = pd.merge(df, leagues_df, on="playerid", how="inner")

print(df)

df.to_csv("data/useful/player_data.csv", index=False)
