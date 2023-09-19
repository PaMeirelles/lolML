import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

d = pd.read_csv("data/model_specific/afterFS.csv")
d = d.drop(columns=["result"])
columns = d.columns

df = pd.read_csv("data/model_specific/not_scaled.csv")
df = df[columns]

scaler = MinMaxScaler()

scaled = scaler.fit_transform(df)
variances = scaled.var(axis=0)

# Create a DataFrame to hold columns and their variances
variance_df = pd.DataFrame({'Columns': columns, 'Variance': variances})

# Sort DataFrame by variances in descending order
variance_df = variance_df.sort_values(by='Variance', ascending=False)

print(variance_df.tail(50))

# Plot the ordered variances
plt.figure(figsize=(10, 6))
plt.bar(variance_df['Columns'], variance_df['Variance'])
plt.xlabel('Columns')
plt.ylabel('Variance')
plt.title('Variance of Scaled Features')
plt.xticks(rotation=90)
plt.tight_layout()

# If you're running this in a script or non-interactive environment, use plt.show()
plt.show()





