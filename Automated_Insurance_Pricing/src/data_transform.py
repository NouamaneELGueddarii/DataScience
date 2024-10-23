import pandas as pd
import numpy as np


def load_data(filepath):
    """Load the dataset from a CSV file."""
    return pd.read_csv(filepath)

def transform_data(df):
    """Apply all transformations to the dataset."""
    # Log-transform the 'charges' column
    df['log_charge'] = df['charges'].apply(lambda x: np.log(x))
    
    # One-hot encode categorical variables (like region, smoker, etc.)
    df = pd.get_dummies(df, columns=['age', 'bmi', 'children', 'smoker', 'region', 'sex'], drop_first=True)
    
    # Remove unnecessary columns or handle missing values if necessary
    df.dropna(inplace=True)
    
    return df

def save_transformed_data(df, output_filepath):
    """Save the transformed dataset."""
    df.to_csv(output_filepath, index=False)
