# This script main responsibility is to clean both data set
# eth_usd_data : filter date range to match etherium post range, add utx timestamp and standardize date to utc
# ethereum_2020_2022 : add column for utx -> Date time object called "Date"
import pandas as pd
import utility
df = pd.read_csv('data/raw/eth_usd_dataset.csv')
df['Date'] = pd.to_datetime(df['Date'])

start_date = '2020-01-19'
end_date = '2022-01-30'

filter_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
filter_df = filter_df.copy()
filter_df['timestamp'] = filter_df["Date"].astype('int64') // 10**9
filter_df["Date"] = filter_df['Date'].dt.tz_localize("UTC")
filter_df.to_csv('data/processed/filtered_eth_usd_data',index=False)

df = pd.read_csv('data/raw/eth_post.csv')
df['Date'] = pd.to_datetime(df['created_utc'],unit='s', utc=True)
df = df[df['body'].notna() & (df['body'] != '')]
df['body'] = df['body'].apply(utility.normalize_text)
df.to_csv('data/processed/cleaned_ethereum_posts',index=False)

