import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from dataframe_pipeline.pipeline_storage import after_variance, after_vif, apenas_basico, apenas_basico_recarregando, with_elo_and_fill_na, with_elo_recarregando

# Load data
df = with_elo_and_fill_na()
print(df)

# Assuming 'result' is the target variable and it's binary (0 or 1)
X = df.drop(columns=['result'])  # Features
y = df['result']  # Target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Get coefficients
coefficients = model.coef_[0]

# Create a DataFrame to store coefficients and corresponding feature names
coef_df = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': coefficients
})

# Predict
y_pred = model.predict(X_test)

# Calculate evaluation metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f"\nAccuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1-Score: {f1}")
