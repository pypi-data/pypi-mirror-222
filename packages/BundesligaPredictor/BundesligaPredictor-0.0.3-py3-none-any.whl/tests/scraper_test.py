import unittest
from scripts.scraper import FootballDataScraper

class TestFootballDataScraper(unittest.TestCase):

    def test_scrape(self):
        scraper = FootballDataScraper('england', start_season=2021)
        df = scraper.scrape()

        # Test that the method returns a non-empty DataFrame
        self.assertIsNotNone(df)
        self.assertFalse(df.empty)

if __name__ == '__main__':
    unittest.main()
