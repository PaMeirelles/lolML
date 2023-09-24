from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import mutual_info_classif
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from tqdm import tqdm
from dataframe_pipeline.pipeline_storage import with_elo_and_fill_na

df = with_elo_and_fill_na()

print(df.shape)

X = df.drop(columns=['result'])
y = df['result']

X_train, X_test, y_train, y_test = train_test_split(X,
                                                   y,
                                                   test_size=0.2,
                                                   random_state=42,)
f1_score_list = []

# Initialize classifier
gbc = LogisticRegression()

# Open file for writing scores
for k in tqdm(range(640, 599, -4)):
    selector = SelectKBest(mutual_info_classif, k=k)
    selector.fit(X_train, y_train)

    sel_X_train_v2 = selector.transform(X_train)
    sel_X_test_v2 = selector.transform(X_test)

    gbc.fit(sel_X_train_v2, y_train)

    kbest_preds = gbc.predict(sel_X_test_v2)

    f1_score_kbest = round(f1_score(y_test, kbest_preds), 5)

    f1_score_list.append(f1_score_kbest)

    with open('f1_scores.txt', 'a') as f:
        f.write(f"Iteration {k}: F1 Score = {f1_score_kbest}\n")

    # Print F1 score to console with flush=True to ensure immediate output
    print(k, f1_score_kbest, flush=True)
