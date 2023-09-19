import pandas as pd

df = pd.read_csv("data/useful/merged_data.csv")
grouped = df.groupby("playerid")
group_sizes = grouped.size().reset_index(name='num_matches')

print(group_sizes)
group_sizes.to_csv("data/useful/num_matches.csv", index=False)