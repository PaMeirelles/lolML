import pandas as pd
from math import exp
from tqdm import tqdm

starting_elo = 1500
k_func = lambda iter:20 * exp(-iter/24) + 0.1
upper_capper = lambda num_matches: starting_elo + num_matches * 40
lower_capper = lambda num_matches: starting_elo - num_matches * 40
save_every = 3
save_into = "data/useful/sequential_elos.csv"

def expected_result(elo_a, elo_b):
    return 1 / (1 + 10 ** ((elo_b - elo_a) / 400))

def simulate(n, df, shuffled, elos={}): 
    counter = 0
    
    num_match_map = pd.read_csv("data/useful/num_matches.csv").set_index('playerid')['num_matches'].to_dict()
    if n < 0:
        infinite = True
    else:
        infinite = False

    with tqdm(total=n) as pbar:
        while infinite or counter != n:
            if shuffled:
                df = df.sample(frac=1, random_state=counter).reset_index(drop=True)
            for _, row in df.iterrows():
                p1 = row["player_1"]
                p2 = row["player_2"]
                r = row["result"]

                if p1 not in elos:
                    elos[p1] = starting_elo
                if p2 not in elos:
                    elos[p2] = starting_elo

                k = k_func(counter)
                ea = expected_result(elos[p1], elos[p2])

                elos[p1] += (r - ea) * k
                elos[p2] -= (r - ea) * k

                elos[p1] = min(elos[p1], upper_capper(num_match_map[p1]))
                elos[p1] = max(elos[p1], lower_capper(num_match_map[p1]))
            
                elos[p2] = min(elos[p2], upper_capper(num_match_map[p2]))
                elos[p2] = max(elos[p2], lower_capper(num_match_map[p2]))

            if counter % save_every == 0:  # Changed condition
                elos_df = pd.DataFrame.from_dict(elos, orient='index', columns=['elo'])
                elos_df.reset_index(inplace=True)
                elos_df.columns = ['playerid', 'elo']  # Assuming you have player names in 'player_1' and 'player_2'
                elos_df.to_csv(save_into, index=False)

            pbar.update(1)
            counter += 1

df = pd.read_csv("data/useful/confrontation_dataset.csv").dropna()
elos_df = pd.read_csv("data/useful/sequential_elos.csv")
simulate(120, df, True, elos_df.set_index("playerid")["elo"].to_dict())