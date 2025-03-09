# Bitcoin Price Tracker

A simple Python script to fetch the current Bitcoin price data using the CoinGecko API.

## Features

- Fetches real-time Bitcoin price in USD
- Retrieves additional market data including:
  - Market capitalization
  - 24-hour trading volume
  - 24-hour price change percentage
  - Last updated timestamp

## Requirements

- Python 3.6 or higher
- `requests` library

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/btc_price_tracker.git
   cd btc_price_tracker
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the script using Python:

```
python btc_price.py
```

The script will fetch the current Bitcoin price data from the CoinGecko API and display it in a formatted way.

## Sample Output

```
Fetching Bitcoin price data...

========== BITCOIN PRICE INFO ==========
Price: $51,234.56 USD
Market Cap: $985,674,321,000.00 USD
24h Volume: $32,456,789,000.00 USD
24h Change: 2.34%
Last Updated: 2025-03-09 17:30:45
========================================
```

## Note

The CoinGecko API has rate limits for free usage. This script makes a single API call each time it runs, which should be well within the free tier limits.

## License

MIT
