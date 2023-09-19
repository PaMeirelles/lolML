import pandas as pd

df = pd.read_csv("data/useful/merged_data.csv")

df = df[["playerid", "playername"]]
df = df.drop_duplicates()

print(df)
df.to_csv("data/useful/alias.csv", index=False)
