import yfinance as yf
import streamlit as st
import pandas as pd 
#check markdown cheetshit for HTML style 
st.write("""
# Stock Price Tracker
Shown are the Stock ** Closing Price** and ***volume*** of Apple, Microsoft and General Motors!""")
# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol =('msft aapl gm')
#get data on this ticker
tickerData = yf.Tickers(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-10-31', end='2020-10-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits
st.write("""## Closing Price""")
st.line_chart(tickerDf.Close)
st.write("""## Volume Price""")
st.line_chart(tickerDf.Volume)
#get event data for ticker 
# get recommendations from analysts 
st.write(""" ## Microsoft Recommendations""")
tickerData.tickers.MSFT.recommendations
st.write(""" ## Dividends""")
tickerData.tickers.MSFT.dividends, 
#to run the stream lit app on browser type cd desktop then press enter and type "streamlit run my app.py
# " myapp.py is my file name
#https://pypi.org/project/yfinance/ for more information on the finance library 