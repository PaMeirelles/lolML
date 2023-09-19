from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import mutual_info_classif
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from tqdm import tqdm


df = pd.read_csv("data/model_specific/afterVIF.csv")

print(df.shape)

X = df.drop(['result'], axis=1)
y = df['result']

X_train, X_test, y_train, y_test = train_test_split(X,
                                                   y,
                                                   test_size=0.3,
                                                   shuffle=True,
                                                   stratify=y,)
f1_score_list = []
selector = SelectKBest(mutual_info_classif, k=96)
selector.fit(X_train, y_train)

selected_feature_mask = selector.get_support()

selected_features = X_train.columns[selected_feature_mask]

print(selected_features)
# Initialize classifier
gbc = LogisticRegression()
for k in tqdm(range(1, 99)):
    selector = SelectKBest(mutual_info_classif, k=k)
    selector.fit(X_train, y_train)
    
    sel_X_train_v2 = selector.transform(X_train)
    sel_X_test_v2 = selector.transform(X_test)
    
    gbc.fit(sel_X_train_v2, y_train)
    kbest_preds = gbc.predict(sel_X_test_v2)
    
    f1_score_kbest = round(f1_score(y_test, kbest_preds, average='weighted'), 3)
    
    f1_score_list.append(f1_score_kbest)
    print(k, f1_score_kbest, flush=True)  # Add flush=True
