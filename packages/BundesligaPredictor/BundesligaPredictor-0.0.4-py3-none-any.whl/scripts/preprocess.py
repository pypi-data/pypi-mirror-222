import pandas as pd
from sklearn.preprocessing import LabelEncoder

class FootballDataPreprocessor:
    '''
    Preprocess the football data.
    
    '''

    def __init__(self, dataframe):
        self.dataframe = dataframe
        self.team_encoder = LabelEncoder()
        self.teams = {0: 'Aalen', 1: 'Augsburg', 2: 'Bayern Munich', 3: 'Bielefeld', 4: 'Bochum', 5: 'Braunschweig',
                      6: 'Cottbus', 7: 'Darmstadt', 8: 'Dortmund', 9: 'Dresden', 10: 'Duisburg', 11: 'Ein Frankfurt',
                      12: 'Erzgebirge Aue', 13: 'FC Koln', 14: 'Fortuna Dusseldorf', 15: 'Frankfurt FSV', 16: 'Freiburg', 
                      17: 'Greuther Furth', 18: 'Hamburg', 19: 'Hannover', 20: 'Heidenheim', 21: 'Hertha', 
                      22: 'Hoffenheim', 23: 'Holstein Kiel', 24: 'Ingolstadt', 25: 'Kaiserslautern', 26: 'Karlsruhe', 
                      27: 'Leverkusen', 28: "M'gladbach", 29: 'Magdeburg', 30: 'Mainz', 31: 'Munich 1860', 32: 'Nurnberg', 
                      33: 'Paderborn', 34: 'RB Leipzig', 35: 'Regensburg', 36: 'Sandhausen', 37: 'Schalke 04', 
                      38: 'St Pauli', 39: 'Stuttgart', 40: 'Union Berlin', 41: 'Werder Bremen', 42: 'Wolfsburg', 
                      43: 'Wurzburger Kickers'}

    def preprocess(self):
        # Select the relevant columns
        relevant_cols = ['HomeTeam', 'AwayTeam', 'B365H', 'B365D', 'B365A', 'BbAv<2.5', 'BbAv>2.5', 'BbAvAHH', 'BbAvAHA', 'Div']
        df = self.dataframe[relevant_cols]

        # Drop rows with missing values
        df = df.dropna()

        # Use the params to encode the 'HomeTeam' and 'AwayTeam' columns
        self.team_encoder.fit(sorted(list(self.teams.values())))
        df['HomeTeam'] = self.team_encoder.transform(df['HomeTeam'])
        df['AwayTeam'] = self.team_encoder.transform(df['AwayTeam'])

        # Encode div manuallt 1 if Div = D1, 0 if Div = D2
        df['Div'] = df['Div'].apply(lambda x: 1 if x == 'D2' else 0)
        
        return df