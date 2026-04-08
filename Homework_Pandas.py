import pandas as pd
import numpy as np

df = pd.read_csv('baltics_dividends.csv')

print(df.info())
# print(df.head())

#1. Set the column ticker as a new index of the DataFrame.

df = df.set_index('ticker')

print(df.head())

#2. Find mean and median of dividend_count column.

mean_value = df['dividend_count'].mean()
median_value = df['dividend_count'].median()

print("Mean:", mean_value)
print("Median:", median_value)

#3. What is the percentage of companies started to pay dividends after year 2018?

after_2018 = df[df['years_from'] > 2018]

percentage = len(after_2018) / len(df) * 100

print(f"Percentage: {percentage:.2f}%")

#4. What is the highest price of the Latvian companies?

print(df['market'].unique())

latvia_max_price = df.loc[df['market'] == 'RIG', 'price'].max()

print("Highest price (Latvia):", latvia_max_price)

#5. Replace market values to Estonia, Latvia and Lithuania.

market_map = {
    'TLN': 'Estonia',
    'RIG': 'Latvia',
    'VLN': 'Lithuania'
}

df['market'] = df['market'].map(market_map)

print(df['market'].unique())

#6. Count values of years with dividend payments (total_years) and sort them in ascending order.

print(df['total_years'].value_counts().sort_index())

#7. Create a new column 'dividend_avg' by using dividend_min and dividend_max.

df['dividend_avg'] = (df['dividend_min'] + df['dividend_max']) / 2

print(df[['dividend_min', 'dividend_max', 'dividend_avg']].head())

#8. Group the DataFrame by market and year of start dividend payment then summate annual payout for every group.

print(df.groupby(['market', 'years_from'])['annual_payout'].sum())

#9. Group DataFrame by market and create a new DataFrame that shows min and max annual payout, mean and median price for every group.

print(df.groupby('market').agg(
    annual_min=('annual_payout', 'min'),
    annual_max=('annual_payout', 'max'),
    price_mean=('price', 'mean'),
    price_median=('price', 'median')
))


