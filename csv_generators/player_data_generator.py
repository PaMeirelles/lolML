import pandas as pd

def add_num_games(df):
    num_games = pd.read_csv("data/useful/num_matches.csv")
    df = pd.merge(df, num_games, on="playerid", how="inner")
    return df

df = pd.read_csv("data/useful/merged_data.csv")
player_data = [
    "kills",
    "deaths",
    "assists",
    "wpm",
    "cspm",
    "teamkills",
    "teamdeaths",
    "team kpm",
    "ckpm",
    "damagetochampions",
    "dpm",
    "damagetakenperminute",
    "wardsplaced",
    "controlwardsbought",
    "totalgold",
    "earnedgold",
    "earned gpm",
    "minionkills",
    "monsterkills",
    "gamelength"
    ]

df = df[['playerid'] + df.select_dtypes(include='number').columns.tolist()]
df = df.drop(columns=["result"])
df = df.groupby('playerid').mean().reset_index()
df = add_num_games(df)

seq_elo = pd.read_csv("data/useful/sequential_elos.csv")
seq_elo.rename(columns={"elo": "seq_elo"}, inplace=True)


df = pd.merge(df, seq_elo, on="playerid", how="inner")

elo = pd.read_csv("data/useful/elos.csv")

df = pd.merge(df, elo, on="playerid", how="inner")
print(df)

df.to_csv("data/useful/player_data.csv", index=False)
