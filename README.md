# Web Scraping apcc
Simple script for data extraction from the "Portuguese commercial centers association" website

## Context
A friend of mine had to do a large "mechanical" transcript from an official website with a terrible response time and put all that into a spreadsheet. This would require much time from him, so I figured a way out to automate it with Selenium.

## Running the Script
Requirements:
1. Python 3.6+
2. Selenium (for the actual web scraping)
3. Chrome [webdriver](https://chromedriver.chromium.org/downloads)
4. xlwt (to export the data in an .xls file)

All the packages can be installed via pip:
```python
pip install -U selenium
pip install xlwt
```
