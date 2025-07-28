# 🌱 Earth911 Recycling Locator Scraper

A Python automation project that scrapes **recycling center data** from [Earth911.com](https://search.earth911.com/).

## 🚀 What It Does
✅ Automates search for **"Electronics"** recycling centers in a given ZIP code.  
✅ Extracts key details for each center:
- **Business Name**
- **Full Address** (all 3 address lines combined)
- **Materials Accepted**

✅ Handles **popups, dropdown selection (100-mile radius)**, and saves the data into a **CSV file**.

## 🛠 Tech Stack
- **Python**
- **Selenium** – for web automation
- **Pandas** – for data handling & CSV export
- **Webdriver-Manager** – to auto-manage ChromeDriver

## ▶️ How to Run

1. Clone this repository  
   ```bash
   git clone https://github.com/utkarsh0002/earth911-scraper.git
   cd earth911-scraper
2. Install dependencies 
   ```bash
    pip install -r requirements.txt
3. Run the script 
   ```bash
   python earth911_scraper.py
