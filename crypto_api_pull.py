import pandas as pd
import requests
import datetime
import os
import traceback

try:
    # === File path ===
    daily_file = r'C:\Users\Navya Sri Gadaley\OneDrive\Desktop\Crypto360\data\crypto_daily.csv'

    # === Get current timestamp ===
    now = datetime.datetime.now().strftime('%m/%d/%Y %H:%M')

    # === Fetch data from CoinGecko ===
    response = requests.get("https://api.coingecko.com/api/v3/coins/markets", params={
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 50,
        "page": 1,
        "sparkline": False
    })

    if response.status_code != 200:
        raise Exception("❌ Failed to fetch data from CoinGecko API")

    # === Extract fields to match the Excel format ===
    df = pd.DataFrame(response.json())[
        ['id', 'symbol', 'name', 'current_price', 'market_cap', 'price_change_percentage_24h', 'total_volume']
    ]

    # === Fill any missing 24h change with 0.0
    df['price_change_percentage_24h'].fillna(0.0, inplace=True)

    # === Add pulled_at column
    df['pulled_at'] = now

    # === Final column order
    final_columns = ['id', 'symbol', 'name', 'current_price', 'market_cap',
                     'price_change_percentage_24h', 'total_volume', 'pulled_at']
    df = df[final_columns]

    # === Append or create the CSV
    if os.path.exists(daily_file):
        df_existing = pd.read_csv(daily_file)

        # Align columns (drop any extras or shuffle)
        df_existing = df_existing[[col for col in final_columns if col in df_existing.columns]]

        df_combined = pd.concat([df_existing, df], ignore_index=True)
        df_combined.to_csv(daily_file, index=False)
        print(f"✅ Appended new data for {now}")
    else:
        df.to_csv(daily_file, index=False)
        print(f"🆕 Created crypto_daily_1234.csv with data for {now}")

except Exception as e:
    print("❌ An error occurred:")
    traceback.print_exc()
