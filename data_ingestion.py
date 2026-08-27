import yfinance as yf
import pandas as pd 
import time

class MarketData:

    """Handles Yahoo Finance API data downloads with rate limiting."""

    def __init__(self, tickers, start_date, end_date):
        self.tickers = tickers
        self.start_date = start_date
        self.end_date = end_date
        self.data = None


    def download_data(self):

        """
        Downloads 'Close' prices sequentially. 
        Returns: (pd.DataFrame of prices, list of valid tickers).
        """

        print(f"[SYSTEM] Downloading data for: {self.tickers}...")

        all_closes = pd.DataFrame()
        valid_tickers = []

        for ticker in self.tickers:
            print(f" -> Fetching {ticker}...")
            try:

                temp_data = yf.download(ticker, start=self.start_date, end=self.end_date, progress=False)

                if not temp_data.empty:
                    all_closes[ticker] = temp_data['Close']
                    valid_tickers.append(ticker)

                else:
                    print(f" [!] No data found for {ticker}")
            
            except Exception as e:
                print(f" [!] Exception found for {ticker}: {e}")

            time.sleep(1)

        if not all_closes.empty:
            self.data = all_closes
            self.tickers = valid_tickers
            print(f"\n[SYSTEM] Download completed! Valid assets: {len(self.tickers)}")
            return self.data, self.tickers
        else:
            print("\n[ERROR] All downloads failed.")
            return None, None