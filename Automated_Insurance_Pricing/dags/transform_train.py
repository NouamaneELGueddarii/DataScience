from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd
import joblib
import numpy as np
from sklearn.ensemble import RandomForestRegressor

def extract_data():
    df = pd.read_csv('../data/raw/insurance.csv')
    return df

def clean_data():
    df = extract_data()
    df.dropna(inplace=True)
    return df

def feature_engineering():
    df = clean_data()
    df['log_charge'] = df['charges'].apply(lambda x: np.log(x))
    df = pd.get_dummies(df, columns=['region', 'smoker', 'sex'], drop_first=True)
    return df

def validate_data():
    df = feature_engineering()
    assert (df['log_charge'] >= 0).all(), "Log charges have negative values!"
    return df

def save_transformed_data():
    df = validate_data()
    df.to_csv('../data/processed/transformed_data.csv', index=False)

def train_model():
    df = pd.read_csv('/path/to/transformed_data.csv')
    X = df.drop(columns=['charges', 'log_charge'])
    y = df['log_charge']
    model = RandomForestRegressor(n_estimators=100)
    model.fit(X, y)
    joblib.dump(model, '/path/to/model.pkl')

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

with DAG('data_transformation_pipeline', default_args=default_args, schedule_interval='@daily') as dag:
    
    extract_data_task = PythonOperator(
        task_id='extract_data',
        python_callable=extract_data
    )
    
    clean_data_task = PythonOperator(
        task_id='clean_data',
        python_callable=clean_data
    )
    
    feature_engineering_task = PythonOperator(
        task_id='feature_engineering',
        python_callable=feature_engineering
    )
    
    validate_data_task = PythonOperator(
        task_id='validate_data',
        python_callable=validate_data
    )
    
    save_transformed_data_task = PythonOperator(
        task_id='save_transformed_data',
        python_callable=save_transformed_data
    )
    
    train_model_task = PythonOperator(
        task_id='train_model',
        python_callable=train_model
    )

# Define task dependencies
extract_data_task >> clean_data_task >> feature_engineering_task >> validate_data_task >> save_transformed_data_task >> train_model_task
