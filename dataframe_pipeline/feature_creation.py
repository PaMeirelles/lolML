import pandas as pd

def date_breaker(df):
    df['date'] = pd.to_datetime(df['date'])

    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['day'] = df['date'].dt.day
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    return df

def elo_diff(df):
    roles = ["top", "jng", "mid", "bot", "sup"]
    for role in roles:
        df[f"seq_elo_diff_{role}"] = df[f"avg_seq_elo_{role}_1"] - df[f"avg_seq_elo_{role}_2"]
        df[f"elo_diff_{role}"] = df[f"avg_elo_{role}_1"] - df[f"avg_elo_{role}_2"]
    return df