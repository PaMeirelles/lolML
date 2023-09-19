from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import mutual_info_classif
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from tqdm import tqdm
from dataframe_pipeline.pipeline_storage import with_elo_and_fill_na_no_reload

df = with_elo_and_fill_na_no_reload()

print(df.shape)

X = df.drop(['result'], axis=1)
y = df['result']

X_train, X_test, y_train, y_test = train_test_split(X,
                                                   y,
                                                   test_size=0.2,
                                                   random_state=42,
                                                   stratify=y,)
f1_score_list = []

# Initialize classifier
gbc = LogisticRegression()

# Open file for writing scores
with open('f1_scores.txt', 'w') as f:
    for k in tqdm(range(1, df.shape[1])):
        selector = SelectKBest(mutual_info_classif, k=k)
        selector.fit(X_train, y_train)

        sel_X_train_v2 = selector.transform(X_train)
        sel_X_test_v2 = selector.transform(X_test)

        gbc.fit(sel_X_train_v2, y_train)

        selected_feature_mask = selector.get_support()

        selected_features = X_train.columns[selected_feature_mask]

        kbest_preds = gbc.predict(sel_X_test_v2)

        f1_score_kbest = round(f1_score(y_test, kbest_preds, average='weighted'), 3)

        f1_score_list.append(f1_score_kbest)
        
        f.write(f"Iteration {k}: F1 Score = {f1_score_kbest}\n")

        # Print F1 score to console with flush=True to ensure immediate output
        print(k, f1_score_kbest, flush=True)

        # Write selected features to the file
        f.write("Selected Features:\n")
        for feature in selected_features:
            f.write(f"{feature}\n")

        # Print selected features to console
        print("Selected Features:")
        for feature in selected_features:
            print(feature)