# 📈 Random Stock Info Viewer

A lightweight Python application that displays live data for randomly selected stocks using a **free API key**. The app returns key company details including current price, market cap, listing date, return on investment, and more.

## 🚀 Features

- Get real-time stock data from a free public API
- Display key metrics like:
  - Company Name
  - Current Price
  - Listing Date
  - ISIN
  - Return on Investment (%)
  - Market Capitalization (₹ Cr.)
  - ROCE (%)
- Quick setup and easy to use

## 🧪 Example Output

```
Name: Palred Technologies Limited  
Current Price: ₹ 192  
Listing Date: 09-May-16  
ISIN: INE218G01033  
Return on Investment: -0.08%  
Market Cap: ₹ 235 Cr.  
ROCE: 4.41%
```

## 🔧 Getting Started

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/random-stock-info-viewer.git
   cd random-stock-info-viewer
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your API key to the `.env` file:
   ```
   API_KEY=your_api_key_here
   ```

4. Run the app:
   ```bash
   python app.py
   ```

## 🔍 Data Source

This app uses data from [ExampleFreeAPI.com](https://examplefreeapi.com) _(replace with actual API name)_ which provides free access to stock data for research and educational use.

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
