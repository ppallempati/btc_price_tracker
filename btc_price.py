import requests
import time
from datetime import datetime


def get_bitcoin_price():
    """
    Fetches the current Bitcoin price in USD from CoinGecko API
    
    Returns:
        dict: A dictionary containing the current price and timestamp
    """
    try:
        # CoinGecko API endpoint for Bitcoin price in USD
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true"
        
        # Send GET request to the API
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            
            # Extract the Bitcoin data
            if 'bitcoin' in data:
                bitcoin_data = data['bitcoin']
                
                # Format the timestamp
                last_updated_timestamp = bitcoin_data['last_updated_at']
                last_updated = datetime.fromtimestamp(last_updated_timestamp).strftime('%Y-%m-%d %H:%M:%S')
                
                # Create a formatted result
                result = {
                    'price_usd': bitcoin_data['usd'],
                    'market_cap_usd': bitcoin_data['usd_market_cap'],
                    'volume_24h_usd': bitcoin_data['usd_24h_vol'],
                    'change_24h_percent': bitcoin_data['usd_24h_change'],
                    'last_updated': last_updated,
                    'timestamp': last_updated_timestamp
                }
                
                return result
            else:
                raise Exception("Bitcoin data not found in the response")
        else:
            raise Exception(f"Failed to fetch data: HTTP {response.status_code}")
            
    except Exception as e:
        print(f"Error: {str(e)}")
        return None


def display_bitcoin_info(data):
    """
    Displays the Bitcoin price information in a formatted way
    
    Args:
        data (dict): Bitcoin price data
    """
    if data:
        print("\n========== BITCOIN PRICE INFO ==========")
        print(f"Price: ${data['price_usd']:,.2f} USD")
        print(f"Market Cap: ${data['market_cap_usd']:,.2f} USD")
        print(f"24h Volume: ${data['volume_24h_usd']:,.2f} USD")
        print(f"24h Change: {data['change_24h_percent']:.2f}%")
        print(f"Last Updated: {data['last_updated']}")
        print("========================================\n")
    else:
        print("No data available")


def main():
    """
    Main function to fetch and display Bitcoin price
    """
    print("Fetching Bitcoin price data...")
    btc_data = get_bitcoin_price()
    display_bitcoin_info(btc_data)


if __name__ == "__main__":
    main()
