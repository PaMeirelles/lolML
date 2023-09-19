import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant
from tqdm import tqdm
from dataframe_pipeline.pipeline_storage import for_vif

def remove_high_vif_features(df, threshold, removal_percent=0.05):
    # Prepare the data for VIF calculation
    X = add_constant(df)
    vif_data = pd.DataFrame()
    vif_data["feature"] = X.columns

    while True:
        # Calculate the VIF values
        vif_data['VIF'] = variance_inflation_factor(X.values, range(X.shape[1]))
        vif_data_sorted = vif_data.sort_values(by='VIF', ascending=False)
        
        # Check if all VIF values are higher than the threshold
        if (vif_data_sorted['VIF'] > threshold).all():
            break

        # Calculate the number of features to remove
        num_to_remove = int(len(vif_data_sorted) * removal_percent)
        if num_to_remove < 1:
            num_to_remove = 1

        # Get the features to remove
        features_to_remove = vif_data_sorted.iloc[:num_to_remove]['feature']

        # Remove the features from the DataFrame
        df = df.drop(columns=features_to_remove)

        # Prepare the data for VIF calculation again
        X = add_constant(df)
        vif_data = pd.DataFrame()
        vif_data["feature"] = X.columns

        print(f"Removed {num_to_remove} features with highest VIF values")

    return df

df = for_vif()


# Define the threshold value
threshold = 10

num_columns = len(df.columns)
num_columns_to_select = num_columns // 50

# Select the first 1/8 of columns
selected_columns = df.iloc[:, :num_columns_to_select]

df = df[[selected_columns]]

# Call the function
new_df = remove_high_vif_features(df, threshold)
