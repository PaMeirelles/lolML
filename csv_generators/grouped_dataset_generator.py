import pandas as pd
from tqdm import tqdm

def get_grouped_by_match():
    df = pd.read_csv("data/useful/merged_data.csv")
    rows = []

    for _, grouped in tqdm(df.groupby("gameid"), total=len(df["gameid"].unique())):
        values = {}
        for col in ['gameid','url', 'league', 'year', 'split', 'playoffs', 'date']:
            values[col] = grouped[col].iloc[0]

        team_1 = grouped[grouped["side"] == "Blue"]
        team_2 = grouped[grouped["side"] == "Red"]

        for _, player_row in team_1.iterrows():
            position = player_row["position"]
            values[f"{position}_1"] = player_row["playerid"] 

        for _, player_row in team_2.iterrows():
            position = player_row["position"]
            values[f"{position}_2"] = player_row["playerid"]

        values["team_1"] = team_1["teamid"].iloc[0]
        values["team_2"] = team_2["teamid"].iloc[0]
        values["result"] = team_1["result"].iloc[0]
        rows.append(values)

    new_df = pd.DataFrame(rows) 
    new_df.to_csv("data/useful/grouped_data.csv")

get_grouped_by_match()