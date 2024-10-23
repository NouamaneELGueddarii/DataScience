import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

def load_transformed_data(filepath):
    """Load the transformed data for training."""
    return pd.read_csv(filepath)

def train_model(df):
    """Train the model using the transformed data."""
    # Prepare features and target variable
    X = df.drop(columns=['charges', 'log_charge'])  # Drop unnecessary columns
    y = df['log_charge']
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train the model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Save the model
    joblib.dump(model, 'model/saved_model.pkl')
    
    return model, X_test, y_test

if __name__ == "__main__":
    # Load the transformed data
    df = load_transformed_data('/path/to/transformed_data.csv')
    
    # Train the model and save it
    model, X_test, y_test = train_model(df)
    
    print("Model training complete.")
