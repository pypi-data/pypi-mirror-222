import os
import pandas as pd
import requests
from bs4 import BeautifulSoup

class FootballDataScraper:
    def __init__(self, country, start_season=2013):
        self.country = country
        self.start_season = start_season
        self.dataframes = []

    def download_csv_and_append_to_list(self, url):
        """
        Download a CSV file, convert it to a DataFrame, and append it to the list.
        """
        try:
            df = pd.read_csv(url, encoding='ISO-8859-1')
            self.dataframes.append(df)
            print(f"Successfully downloaded and processed {url}")
        except Exception as e:
            print(f"Failed to process file {url}. Error: {str(e)}")

    def scrape(self):
        """
        Scrape football data for the specified country and seasons.
        """
        base_url = f"https://www.football-data.co.uk/{self.country}m.php"
        response = requests.get(base_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        year = None
        for tag in soup.find_all(['i', 'a']):
            if tag.name == 'i' and "Season" in tag.text:
                year = int(tag.text.split(' ')[1].split('/')[0])
            elif tag.name == 'a' and year is not None and year >= self.start_season:
                href = tag.get('href')
                if href.endswith('.csv'):
                    url = f"https://www.football-data.co.uk/{href}"
                    self.download_csv_and_append_to_list(url)

        # Concatenate all dataframes into a single dataframe
        df_all = pd.concat(self.dataframes, ignore_index=True, axis=0)

        return df_all

    def save_to_parquet(self, df):
        """
        Save the DataFrame to a csv file in the 'data' directory.
        """
        os.makedirs('data', exist_ok=True)
        df.to_csv(os.path.join('data', f'{self.country}_all.csv'))
