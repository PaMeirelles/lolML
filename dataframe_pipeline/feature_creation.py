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
    
    new_columns = []
    for role in roles:
        seq_elo_diff_col = f"seq_elo_diff_{role}"
        elo_diff_col = f"elo_diff_{role}"
        
        seq_elo_diff_values = df[f"avg_seq_elo_{role}_1"] - df[f"avg_seq_elo_{role}_2"]
        elo_diff_values = df[f"avg_elo_{role}_1"] - df[f"avg_elo_{role}_2"]
        
        new_columns.extend([(seq_elo_diff_col, seq_elo_diff_values), (elo_diff_col, elo_diff_values)])
    
    new_df = pd.concat([df] + [pd.DataFrame({col: values for col, values in new_columns})], axis=1)
    return new_df