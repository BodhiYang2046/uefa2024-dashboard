import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def scrape_uefa_data():
    url = "https://fbref.com/en/comps/676/schedule/European-Championship-Scores-and-Fixtures"
    lst = [] #To append columns' names
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    standings = []
    # groups = soup.find_all('table') 
    table = soup.find_all('table', class_='stats_table sortable min_width')[0]
    print(type(table))

    thead = table.find('thead')
    header = [th.text.strip() for th in thead.find_all('th')]

    tbody = table.find('tbody')
    rows = tbody.find_all('tr')

    data = []
    for row in rows:
        cols = row.find_all(['th', 'td'])  
        cols = [col.text.strip() for col in cols]
        if len(cols) == len(header) and cols[0]!='':
            print(cols)
            data.append(cols)
        else:
            print(f"Skipping row due to column mismatch: {cols}")

    df = pd.DataFrame(data, columns=header) 
    # df.to_csv('uefa.csv', encoding='utf8', index=False)
    return df

if __name__ == "__main__":
    scrape_uefa_data()