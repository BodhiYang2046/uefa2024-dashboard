import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def scrape_uefa_data():
    url = "https://fbref.com/en/comps/676/schedule/European-Championship-Scores-and-Fixtures"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        logger.error(f"Error fetching URL: {e}")
        return pd.DataFrame()

    soup = BeautifulSoup(response.content, 'html.parser')
    
    try:
        table = soup.find_all('table', class_='stats_table sortable min_width')[0]
    except IndexError:
        logger.error("Could not find the required table on the page")
        return pd.DataFrame()

    thead = table.find('thead')
    header = [th.text.strip().lower().replace(" ", "_") for th in thead.find_all('th')]

    tbody = table.find('tbody')
    rows = tbody.find_all('tr')

    data = []
    for row in rows:
        cols = row.find_all(['th', 'td'])  
        cols = [col.text.strip() for col in cols]
        if len(cols) == len(header) and cols[0] != '':
            logger.info(f"Processing row: {cols}")
            data.append(cols)
        else:
            logger.warning(f"Skipping row due to column mismatch: {cols}")

    df = pd.DataFrame(data, columns=header)

        # Renaming columns to match PostgreSQL table column names
    df.columns = ['round', 'week', 'day', 'date', 'time', 'home_team', 'home_xg', 'score', 'away_xg', 'away_team', 'attendance', 'venue', 'referee', 'match_report', 'notes']
    
    # Replace empty strings with None for numeric columns
    numeric_columns = ['week', 'home_xg', 'away_xg', 'attendance']
    df[numeric_columns] = df[numeric_columns].replace('', None)
    
    # Convert columns to appropriate data types
    df['week'] = df['week'].astype(float)
    df['home_xg'] = df['home_xg'].astype(float)
    df['away_xg'] = df['away_xg'].astype(float)
    df['attendance'] = df['attendance'].str.replace(',', '').astype(float)

    logger.info(f"Scraped {len(df)} rows of data")

    return df