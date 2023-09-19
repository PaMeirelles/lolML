import pandas as pd

def get_pre_match_data():
    pre_match_columns = [
        "gameid",
        "url",
        "league",
        "year",
        "split",
        "playoffs",
        "date",
        "participantid",
        "side",
        "position",
        "playername",
        "playerid",
        "teamname",
        "teamid",]
    df = pd.read_csv("merged_data.csv")
    pre_match_df = df[pre_match_columns]
    pre_match_df.to_csv("pre_match_data.csv", index=False)