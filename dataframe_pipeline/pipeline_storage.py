import pandas as pd
from dataframe_pipeline.na_dealers import *
from dataframe_pipeline.normalize import *
from dataframe_pipeline.feature_remover import *
from dataframe_pipeline.feature_creation import *
from dataframe_pipeline.aggregator import *

def pipeline(start_from, *functions):
    df = pd.read_csv(start_from)
    for func in functions:
        df = func(df)
    return df

# Wrappers
def after_vif():
    return pipeline("data/useful/grouped_with_player_data.csv", keep_columns_above_5_percent, standard_scaling, remove_until_vif_less_than_10)

def after_variance():
    return pipeline("data/useful/grouped_with_player_data.csv", keep_columns_above_5_percent, standard_scaling, remove_until_vif_less_than_10, remove_variance_smaller_than_003)

def apenas_basico():
    return pipeline("data/useful/grouped_with_player_data.csv", keep_columns_above_5_percent, standard_scaling)

def apenas_basico_recarregando():
    return pipeline("data/useful/grouped_data.csv", incorporate_player_data, keep_columns_above_5_percent, standard_scaling)

def with_elo_recarregando():
    return pipeline("data/useful/grouped_data.csv", incorporate_player_data, keep_columns_above_5_percent, elo_diff, standard_scaling)

def with_elo_and_fill_na():
    return pipeline("data/useful/grouped_data.csv", incorporate_player_data, fill_with_median, elo_diff, standard_scaling)

def with_elo_and_fill_na_no_reload():
    return pipeline("data/useful/grouped_with_player_data.csv", fill_with_median, elo_diff, standard_scaling)

def for_vif():
    return pipeline("data/useful/grouped_with_player_data.csv", fill_with_median, elo_diff, preserve_variance_scaling)    
