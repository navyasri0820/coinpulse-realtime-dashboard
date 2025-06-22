# 📊 CoinPulse- A Realtime-Dashboard

CoinPulse is a complete end-to-end data analytics project that automates real-time cryptocurrency data ingestion from the CoinGecko API and visualizes trends through a Power BI dashboard. This project demonstrates strong hands-on skills in Python scripting, API integration, data transformation, time-series analysis, and dashboard development—making it a portfolio-ready example for data analyst and business intelligence roles.

## 🚀 Project Summary

The project is built around a custom Python script that fetches live market data for the top 50 cryptocurrencies, including price, volume, market cap, and 24-hour price change. The data is appended daily to a growing historical dataset (`crypto_daily.csv`) using Task Scheduler. Power BI is then used to connect and refresh insights based on this data.

This setup demonstrates real-world data engineering and analytics workflows, covering ETL (Extract, Transform, Load), data automation, and visualization—without reliance on expensive cloud tools.

## 🛠 Technologies Used

- **Python** – for data ingestion, transformation, and error handling
- **Pandas** – for data manipulation and cleaning
- **CoinGecko API** – for real-time cryptocurrency market data
- **Power BI** – for interactive reporting and data visualization
- **Windows Task Scheduler** – for local automation of daily script execution

## 📂 Project Structure
Crypto360/
├── scripts/
│   └── crypto_api_pull.py           # Python script for pulling and storing daily data
├── data/
│   └── crypto_daily.csv             # CSV file storing time-stamped historical data
├── dashboard/
│   └── Crypto360.pbix               # Power BI file with interactive visuals
└── README.md

## 📊 Dataset Schema (`crypto_daily.csv`)

| Column                        | Description                                  |
|------------------------------|----------------------------------------------|
| `id`                         | CoinGecko's unique coin ID                   |
| `symbol`                     | Ticker symbol (e.g., BTC, ETH)               |
| `name`                       | Full name of the cryptocurrency              |
| `current_price`              | Current market price in USD                  |
| `market_cap`                 | Market capitalization in USD                 |
| `price_change_percentage_24h`| % price change in the last 24 hours          |
| `total_volume`               | 24-hour trading volume                       |
| `pulled_at`                  | Timestamp of the data extraction             |

## 📈 Dashboard Highlights

- 📉 Real-time crypto tracking with visual comparisons
- 📊 Market cap and volume analysis
- 📈 24h price change metrics and trend lines
- ⏱ Drill-down filtering with timestamp (`pulled_at`)
- 📅 Date-wise trend comparisons using slicers

## 🔁 Power BI Refresh Strategy

While Power BI Service supports cloud-based auto-refresh, this project uses **local automation** via Windows Task Scheduler and **manual dashboard refresh**.

This project uses a manual refresh strategy in Power BI to avoid the need for Pro licenses or cloud gateways. The data pipeline is automated using Python and Task Scheduler, while users manually refresh visuals in Power BI. This keeps the solution fully offline, transparent, and easy to present in interviews, learning environments, or portfolio demonstrations—while still simulating a real-world daily reporting workflow.

## 📂 Project Files
scripts/crypto_api_pull.py – Python script that pulls and appends data daily
data/crypto_daily.csv – Time-stamped historical dataset of top 50 cryptocurrencies
dashboard/Crypto360.pbix – Power BI dashboard with filters, visuals, and KPIs
README.md – Project documentation

## 💼 Skills Demonstrated

- ✅ REST API data integration (CoinGecko)
- ✅ Data transformation using Pandas
- ✅ Daily data appending & time-series structuring
- ✅ Power BI dashboard design and DAX usage
- ✅ Local automation with Windows Task Scheduler
- ✅ Real-time insights and dynamic report building

## 📎 Useful Links
https://www.linkedin.com/in/gadaley-navya-sri-4b5aa81ba/ [LinkedIn]

https://github.com/navyasri0820/coinpulse-realtime-dashboard [GitHub Repository]

