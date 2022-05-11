from env import get_db_url
import os
import pandas as pd

# Make a function named get_titanic_data that returns the titanic data 
# from the codeup data science database as a pandas data frame. Obtain 
# your data from the Codeup Data Science Database. 
def get_titanic_data():
    filename = 'titanic.csv'

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        query = '''SELECT * FROM passengers;'''
        df = pd.read_sql(query, get_db_url('titanic_db'))
        df.to_csv(filename)
        return df

# Make a function named get_iris_data that returns the data from the iris_db
# on the codeup data science database as a pandas data frame. The returned 
# data frame should include the actual name of the species in addition to 
# the species_ids. Obtain your data from the Codeup Data Science Database. 
def get_iris_data():
    filename = 'iris.csv'

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        query = '''SELECT m.*, s.species_name FROM measurements AS m JOIN species AS s USING (species_id);'''
        df = pd.read_sql(query, get_db_url('iris_db'))
        df.to_csv(filename)
        return df

# Make a function named get_telco_data that returns the data from the telco_churn
# database in SQL. In your SQL, be sure to join all 4 tables together, so that 
# the resulting dataframe contains all the contract, payment, and internet service
# options. Obtain your data from the Codeup Data Science Database. 
def get_telco_data():
    filename = 'telco.csv'
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        query = '''
            SELECT c.*, ct.contract_type, pt.payment_type, iso.internet_service_type
            FROM customers AS c
            JOIN contract_types AS ct USING (contract_type_id)
            JOIN payment_types AS pt USING (payment_type_id)
            JOIN internet_service_types AS iso USING (internet_service_type_id);
        '''
        df = pd.read_sql(query, get_db_url('telco_churn'))
        df.to_csv(filename)
        return df