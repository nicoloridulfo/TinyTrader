import yfinance as yf

def main():
    with open("TinyTrader/symbols.txt", "r") as f:
        symbols = f.read().split("\n")
        df = yf.download(symbols, group_by="ticker")
        for symbol in df.columns.levels[0]:
            df[symbol].to_pickle(f"data/{symbol}.p")

if __name__ == "__main__":
    main()
