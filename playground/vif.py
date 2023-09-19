import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant
from tqdm import tqdm

# Load the DataFrame from the CSV file
file_path = "data/model_specific/afterVIF.csv"
df = pd.read_csv(file_path)

# Prepare the data for VIF calculation
X = add_constant(df)

# Calculate the VIF values
vif_data = pd.DataFrame()
vif_data["feature"] = X.columns

for i in tqdm(range(X.shape[1])):
    vif_data.loc[i, "VIF"] = variance_inflation_factor(X.values, i)

vif_data_sorted = vif_data.sort_values(by='VIF', ascending=False)

# Print the top 15
print("Top 15 VIF values:")
print(vif_data_sorted.head(15))

# Print the bottom 15
print("\nBottom 15 VIF values:")
print(vif_data_sorted.tail(15))
