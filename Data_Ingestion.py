

import pandas as pd
from sqlalchemy import create_engine
import argparse
import os


def main(params):
    file_name= params.file_name
    hostname= params.hostname
    user = params.user
    password = params.password
    port = params.port
    DB_name = params.DB_name
    table= params.table
    url= params.url

    df = pd.read_csv(f'{file_name}]' , low_memory=False)

    os.system(f'wget {url} -O {file_name}')

    df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'] )
    df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'] )

    engine = create_engine('postgresql://{user}:{password}@{hostname}:{port}/{DB_name}')

    # Create table 

    df.head(0).to_sql(name='yellow_taxi_data',con=engine , if_exists='replace')

    df_iter = pd.read_csv('yellow_tripdata_2021-01.csv' , iterator=True , chunksize=100000)

    count = 0
    while True:
        df= next(df_iter)
        df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'] )
        df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'] )
        df.to_sql(name='yellow_taxi_data',con=engine , if_exists='append')
        print(f'Batch ->{count+1} Inserted')
        count=count+1



if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Process some integers.')

    # file_name , hostname, user , password , port , DB_name , table
    parser.add_argument('file_name',help='an integer for the accumulator')
    parser.add_argument('hostname',help='an integer for the accumulator')
    parser.add_argument('user',help='an integer for the accumulator')
    parser.add_argument('password',help='an integer for the accumulator')
    parser.add_argument('port',help='an integer for the accumulator')
    parser.add_argument('DB_name',help='an integer for the accumulator')
    parser.add_argument('table',help='an integer for the accumulator')
    parser.add_argument('url',help='an integer for the accumulator')

    args = parser.parse_args()
    main(args)
