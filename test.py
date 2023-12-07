import yfinance as yf
import pandas as pd

dataF = yf.download("EURUSD=X", starts="2022-10-06", end="2022-12-4", interval="15m")
dataF.iloc[-1:,:]
dataF.Open.iloc