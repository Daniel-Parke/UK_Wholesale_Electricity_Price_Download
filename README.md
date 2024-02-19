# UK Energy Wholesale Electricity Price - Historical Data Downloader
## General Use Guidelines

This script is designed to download historical UK wholesale electricity prices from the Trading Economics website. Please note that the API link within the script needs to be updated with the correct link each day you run it, as the AUTH key used by trading economics changes daily (see details below). The API link is stored in the `API.txt` file, so no edits to the code are required, simply replace the web address in the .txt file.

## Prerequisites

Before running the program, ensure you meet the following requirements to ensure its correct execution:

- **Python Installation**: Ensure Python 3.9 or higher is installed on your system. This is especially important if you are not using an IDE like Jupyter or VSCode.

- **API Link Update**: The API link used to pull data changes daily. Update the variable assigned to the API with the correct link before running the script. The correct link can be found at [Trading Economics - UK Electricity Price](https://tradingeconomics.com/united-kingdom/electricity-price). For more information on how to find the data source URL from the webpage, visit [How to find data behind a chart/map using 'Inspect'](https://onlinejournalismblog.com/2017/05/10/how-to-find-data-behind-chart-map-using-inspector/).

- **Data Frequency and Range**: When generating the API link, it's important to first select the time range and data frequency you're interested in below the chart on the Trading Economics website. Data is available in **1Y**, **5Y**, **10Y**, and **ALL** time periods, with frequencies of **1 Day**, **1 Week**, and **1 Month**.

## Setup

**Package Installation**: Install the required Python packages listed below if they're not already installed on your system.

## Running the Script

To collect the data, run the `uk_wholesale_energy_data.py` file in your command line. This will generate and save a CSV file with the historical UK energy market electricity prices into the `Downloaded_Data` folder.

## Installation Commands
```python
pip install pandas
pip install requests
```
    
## Libraries used:
```python
from timeit import default_timer as timer
import os.path
import requests
import pandas as pd 
```

![WiseWattage](https://i.imgur.com/Y7oMz2Y.png)