### CAPM Return Estimator with Live Data (Streamlit App)
# File: capm_app.py

import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# CAPM Formula
def calculate_capm(rf, beta, rm):
    return rf + beta * (rm - rf)

# Streamlit UI
st.set_page_config(page_title="CAPM Calculator", layout="centered")
st.title("CAPM Expected Return Calculator")

# Input: Stock symbol
symbol = st.text_input("Enter Stock Symbol (e.g., AAPL, TSLA, MSFT):").upper()

if symbol:
    try:
        stock = yf.Ticker(symbol)
        beta = stock.info.get('beta', None)

        if beta is None:
            st.error("Beta not found. Please try another stock.")
        else:
            # Input: Risk-Free Rate and Market Return
            rf_percent = st.slider("Select Risk-Free Rate (%)", 0.0, 10.0, 4.5)
            rm_percent = st.slider("Select Market Return (%)", 5.0, 15.0, 10.0)

            rf = rf_percent / 100
            rm = rm_percent / 100

            # Calculate Expected Return
            expected_return = calculate_capm(rf, beta, rm)
            expected_percent = expected_return * 100

            # Display Results
            st.success(f"Beta: {beta:.2f}")
            st.success(f"Expected Return (CAPM): {expected_percent:.2f}%")

            # Chart
            chart_data = pd.DataFrame({
                'Returns': [rf_percent, expected_percent, rm_percent]
            }, index=['Risk-Free Rate', f'{symbol} Expected Return', 'Market Return'])

            st.bar_chart(chart_data)

    except Exception as e:
        st.error(f"Error: {str(e)}")

st.caption("Developed by [SHAIK JAMEEL AHAMMAD, BEPARI HUZAIF ALI KHAN] | Final Year CSE Mini Project")
