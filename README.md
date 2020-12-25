# Tiny Trader
The goal of tiny trader is facilitate strategy development and signal generation while keeping the code as short and simple as possible (in the beginning at least).
Example 1, writing strategies using backtraders. This allows us to both backtest and run the strategy without having to rewrite it.
Example 2, not using an SQL-database to keep the data. Since the data will not be updated that often and to both minimize code complexity and query times. Instead, the pandas dataframes will be pickled.
