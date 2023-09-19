import pandas as pd
from sklearn.preprocessing import StandardScaler

def standard_scaling(df):
    scaler = StandardScaler()
    columns_to_normalize = df.columns
    normalized_data = scaler.fit_transform(df[columns_to_normalize])
    df = pd.DataFrame(normalized_data, columns=columns_to_normalize)
    df['result'] = (df['result'] > 0).astype(int)
    return df

def preserve_variance_scaling(df):
    columns_to_normalize = df.columns
    mean = df[columns_to_normalize].mean()
    std_dev = df[columns_to_normalize].std()
    normalized_data = (df[columns_to_normalize] - mean) / std_dev
    df = pd.DataFrame(normalized_data, columns=columns_to_normalize)
    df['result'] = (df['result'] > 0).astype(int)
    return df