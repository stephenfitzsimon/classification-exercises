import pandas as pd

# train test split from sklearn
from sklearn.model_selection import train_test_split
# imputer from sklearn
from sklearn.impute import SimpleImputer

def prep_iris(df):
    df.drop(columns = ['species_id', 'measurement_id', 'Unnamed: 0'], inplace = True)
    df.rename(columns = {'species_name':'species'}, inplace=True)
    dummy_df = pd.get_dummies(df[['species']], dummy_na=False, drop_first=True)
    df = pd.concat([df, dummy_df], axis = 1)
    return df

def split_iris_data(df):
    df = prep_iris(df)
    train, test = train_test_split(df, train_size = 0.8, stratify = df.species)
    train, validate = train_test_split(train, train_size = 0.7, stratify = train.species)
    return train, test, validate

def prep_titanic(df):
    '''
    cleans the titanic data 
    '''
    df.drop_duplicates(inplace=True)
    col_to_drop = ['Unnamed: 0','embarked', 'class', 'passenger_id', 'deck']
    df = df.drop(columns=col_to_drop)
    df['embark_town'] = df.embark_town.fillna(value='Southampton')
    dummy_df = pd.get_dummies(df[['sex', 'embark_town']], dummy_na = False, drop_first = [True, True])
    df = pd.concat([df, dummy_df], axis = 1)
    return df.drop(columns=['sex', 'embark_town'])

def prep_telco(df):
    df.drop(columns = ['internet_service_type_id', 'contract_type_id', 'payment_type_id', 'Unnamed: 0'], inplace=True)
    cat_cols = list(df.select_dtypes('object').iloc[:,1:].columns)
    cat_cols.remove('total_charges') #this data column will need to be changed to floatdummy_df = pd.get_dummies(telco[cat_cols], dummy_na = False, drop_first = True)
    dummy_df = pd.get_dummies(df[cat_cols], dummy_na = False, drop_first = True)
    df = pd.concat([df, dummy_df], axis = 1)
    #drop the empty total_charges rows
    df = df[df.total_charges != ' ']
    df.total_charges = df.total_charges.astype(float)
    return df

def split_telco_data(df):
    df = prep_telco(df)
    train, test = train_test_split(df, train_size = 0.8, stratify = df.churn)
    train, validate = train_test_split(train, train_size = 0.7, stratify = train.churn)
    return train, test, validate