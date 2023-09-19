import pandas as pd

def expand_roles(features):
    roles = ["top", "mid", "jng", "bot", "sup"]
    return [f"{feature}_{role}" for role in roles for feature in features]

def expand_teams(features):
    teams = [1, 2]
    return [f"{feature}_{team}" for team in teams for feature in features]

def expand_roles_and_teams(features):
    return expand_teams(expand_roles(features))

def remove_features(df, features):
    columns = df.columns
    to_keep = list(set(columns) - set(features))
    return df[to_keep]

# Wrappers
def remove_until_vif_less_than_10(df):
    to_remove = expand_roles_and_teams(
    ["avg_minionkills",
     "avg_ckpm",
     "avg_damagetochampions",
     "avg_wardsplaced",
     "avg_team kpm",
     "avg_earned gpm",
     "avg_teamkills",
     "avg_totalgold",
     "avg_earnedgold",
     "avg_teamdeaths"]) + expand_teams(["avg_cspm_sup"])
    return remove_features(df, to_remove)

def remove_variance_smaller_than_003(df):
    to_remove = expand_roles_and_teams(
        ["avg_gamelength"]
    ) + [
        'avg_monsterkills_top_2',
        'avg_kills_jng_2',
        'avg_damagetakenperminute_top_2',
        'avg_assists_top_1',
        'avg_monsterkills_mid_2',
        'avg_monsterkills_bot_2',
        'avg_damagetakenperminute_bot_2',
        'avg_monsterkills_mid_1',
        'avg_monsterkills_sup_2',
        'avg_monsterkills_top_1',
        'avg_monsterkills_bot_1',
        'avg_wpm_top_2',
        'avg_monsterkills_sup_1',
        'avg_wpm_top_1',
        'avg_damagetakenperminute_sup_2',
        'avg_damagetakenperminute_sup_1',
        'avg_damagetakenperminute_bot_1'
    ]
    return remove_features(df, to_remove)
