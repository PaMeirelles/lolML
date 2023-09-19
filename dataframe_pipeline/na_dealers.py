def keep_columns_with_low_missing_values(df, max_missing_percentage):
    missing_percentage = (df.isna().sum() / len(df)) * 100

    low_missing_value_columns = missing_percentage[missing_percentage < max_missing_percentage].index.tolist()

    return df[low_missing_value_columns]

def remove_na(df):
    return df.dropna()

def fill_with_median(df):
    for column in df.columns:
        non_na_values = df[column].dropna()
        if non_na_values.empty:
            df.drop(column, axis=1, inplace=True)
        else:
            non_na_median = non_na_values.median()
            df[column].fillna(non_na_median, inplace=True)
    return df

# Wrappers
def keep_columns_above_5_percent(df):
    return remove_na(keep_columns_with_low_missing_values(df, 5))

def keep_columns_above_20_percent(df):
    return remove_na(keep_columns_with_low_missing_values(df, 20))