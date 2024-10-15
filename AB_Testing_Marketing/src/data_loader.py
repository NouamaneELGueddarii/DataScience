import pandas as pd

def load_data(file_path):
    """
    Load the CSV data file and perform initial cleaning.
    
    Parameters:
    - file_path: str, path to the CSV file
    
    Returns:
    - DataFrame containing cleaned data
    """
    df = pd.read_csv(file_path)
    # Convert 'converted' to binary (0 or 1)
    df['converted'] = df['converted'].astype(int)
    # Drop unnecessary columns
    if 'Unnamed: 0' in df.columns:
        df_cleaned = df.drop(columns=['Unnamed: 0'])
        return df_cleaned
    return df
