# Stock Info Retriever

This Python script fetches and displays random stock market data using the Free API from api.freeapi.app. It's designed for quick demos and learning purposes around API consumption.

## Features

- Retrieves random stock details
- Displays company name, ISIN, listing date, ROE, ROCE, market cap, and current price
- Includes basic error handling for connection issues

## Requirements

- Python 3.x(x = 9 or 9+)
- requests library (`pip install requests`)

## How to Use

1. Run the script with: `python script_name.py`
   (Replace `script_name.py` with your actual filename)
2. The script will print random stock information from the API.
3. If the API fails or internet is unavailable, an exception is raised:
   `"failed please check your internet connection"`

## API Details

- Source: FreeAPI – https://api.freeapi.app
- Endpoint: `https://api.freeapi.app/api/v1/public/stocks/stock/random`
- This is a demo API and the data is randomly generated for learning/testing.

## About

A minimal and practical script created to demonstrate how to consume REST APIs in Python using the requests module.
