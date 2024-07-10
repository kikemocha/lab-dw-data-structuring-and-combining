# Your code here
import pandas as pd
import numpy as np

def clean_data(df):
    df.rename(columns={'ST':'state'}, inplace=True)
    def change_name(name):
        name = name.lower()
        name = name.replace(' ','_')
        return name
    df.columns = pd.Series(df.columns).apply(lambda x : change_name(x))
    gender_mapping = {'Male':'M','Femal':'F','female':'F'}
    country_mapping = {'AZ':'Arizona','WA':'Washington','Cali':'California'}
    car_mapping = {'Sports Car':'Luxury', 'Luxury SUV':'Luxury', 'Luxury Car':'Luxury'}
    def mapping(value, value_map):
        if pd.isna(value):
            return np.nan
        elif value in value_map:
            return value_map[value]
        else:
            return value
    
    df['gender'] = df['gender'].apply(lambda x : mapping(x,gender_mapping))
    df['state'] = df['state'].apply(lambda x : mapping(x,country_mapping))
    df['vehicle_class'] = df['vehicle_class'].apply(lambda x : mapping(x,car_mapping))
    df['education'] = df['education'].apply(lambda x : 'Bachelor' if x == 'Bachelors' else x)
    df['customer_lifetime_value'] = df['customer_lifetime_value'].apply(lambda x : np.nan if pd.isna(x) else float(x.replace('%','')))
    df['number_of_open_complaints'] = df['number_of_open_complaints'].apply(lambda x : np.nan if pd.isna(x) else x.split('/')[1])
    
    df = df.dropna(how='all', axis=0)
    df = df.dropna(how='all', axis=1)
    
    df['customer_lifetime_value'].fillna( df['customer_lifetime_value'].median() ,inplace = True)
    df['gender'].fillna( df['gender'].mode()[0] ,inplace = True)

    df.drop_duplicates(subset=['income','customer_lifetime_value','monthly_premium_auto','policy_type','vehicle_class','total_claim_amount'], inplace=True)
    return df
