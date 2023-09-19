import pandas as pd

df = pd.read_csv("data/useful/grouped_data.csv")
new_data = []

roles = ["top", "jng", "mid", "bot", "sup"]

for index, row in df.iterrows():
    for i in range(5):
        for j in range(i, 5):
            p1 = row[f"{roles[i]}_1"]
            p2 = row[f"{roles[j]}_2"]
            mt = {"player_1": p1, "player_2": p2, "result": row["result"]}
            new_data.append(mt)

new_df = pd.DataFrame.from_dict(new_data)
print(new_df)
new_df.to_csv("data/useful/confrontation_dataset.csv", index=False)