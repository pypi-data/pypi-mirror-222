import unittest
from scripts.pre_process import FootballDataPreprocessor
import pandas as pd
import numpy as np

class TestFootballDataPreprocessor(unittest.TestCase):

    def setUp(self):
        self.data = pd.DataFrame({
            'Div': ['A', 'A', 'B'],
            'HomeTeam': ['Aalen', 'Augsburg', 'Bayern Munich'],
            'AwayTeam': ['Bielefeld', 'Bochum', 'Braunschweig'],
            'B365H': [1.5, 2.3, 3.4],
            'B365D': [2.4, 3.2, 2.1],
            'B365A': [2.5, 3.4, 2.2],
            'BbAv<2.5': [1.6, 2.7, 1.8],
            'BbAv>2.5': [2.6, 3.8, 2.9],
            'BbAvAHH': [1.7, 2.8, 1.9],
            'BbAvAHA': [2.7, 3.9, 2.1],
            'FTR': ['H', 'A', 'D']
        })

        self.processor = FootballDataPreprocessor(self.data)

    def test_preprocess(self):
        processed_data = self.processor.preprocess()

        # Check if the output DataFrame has the right shape
        self.assertEqual(processed_data.shape, self.data.shape)

        # Check if the output DataFrame has the right columns
        expected_columns = ['HomeTeam', 'AwayTeam', 'FTR', 'B365H', 'B365D', 'B365A', 'BbAv<2.5', 'BbAv>2.5', 'BbAvAHH', 'BbAvAHA', 'Div_B']
        self.assertListEqual(list(processed_data.columns), expected_columns)

        # Check if the 'Div_B' column has been correctly created
        expected_div_b = np.array([0, 0, 1])
        np.testing.assert_array_equal(processed_data['Div_B'].values, expected_div_b)

if __name__ == '__main__':
    unittest.main()