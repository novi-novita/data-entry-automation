# Data Entry Automation Repository

## 📌 Description
This repository provides automated solutions for data entry tasks, making workflows more efficient and error-free. It includes scripts for cleaning and formatting data, automating Google Sheets updates, and extracting structured data from websites.

## 📌 Overview
This repository contains automation scripts for data entry tasks, including:
- **Data Cleaning & Formatting**: Removing duplicates, handling missing values, and exporting clean data.
- **Google Sheets Automation**: Automatically inserting data into Google Sheets using Google Sheets API.
- **Web Scraping for Data Entry**: Extracting data from websites and saving it into an Excel file.

## 📂 Project Structure
```
📦 data-entry-automation
 ┣ 📜 clean_data.py       # Script for cleaning Excel data
 ┣ 📜 sheets_api.py       # Google Sheets automation script
 ┣ 📜 scrape_data.py      # Web scraping script for data entry
 ┣ 📜 sample_data.xlsx    # Sample input Excel file
 ┣ 📜 cleaned_data.xlsx   # Output of cleaned data
 ┣ 📜 scraped_data.xlsx   # Output of scraped data
 ┣ 📜 credentials.json    # Google API credentials (DO NOT SHARE)
 ┗ 📜 README.md           # Project documentation
```

## 🚀 How to Use

### 1️⃣ Data Cleaning & Formatting
```bash
# Run the script to clean Excel data
python clean_data.py
```

### 2️⃣ Google Sheets Automation
1. Set up Google API credentials (`credentials.json`).
2. Run the script to append data:
```bash
python sheets_api.py
```

### 3️⃣ Web Scraping for Data Entry
```bash
# Scrape data from a website and save it to an Excel file
python scrape_data.py
```

## 📌 Requirements
Install dependencies using:
```bash
pip install pandas gspread google-auth requests beautifulsoup4 openpyxl
```

## 📜 License
This project is licensed under the MIT License.

## ✨ Contributions
Feel free to fork and improve this project! 🚀
