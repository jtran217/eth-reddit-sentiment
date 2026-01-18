# This script main responsibility is to simply filter the date to match the etherium post csv range. Also added utx timestamp to make matching easier down the road
import pandas as pd
df = pd.read_csv('data/raw/eth_usd_dataset.csv')
df['Date'] = pd.to_datetime(df['Date'])

start_date = '2020-01-19'
end_date = '2022-01-30'

filter_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
filter_df = filter_df.copy()
filter_df['timestamp'] = filter_df["Date"].astype('int64') // 10**9
filter_df.to_csv('data/processed/filtered_eth_usd_data',index=False)