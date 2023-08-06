import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv('germany_all.csv')

def preprocess(dataframe):
    PARAMS = {'teams': {0: 'Aalen', 1: 'Augsburg', 2: 'Bayern Munich', 3: 'Bielefeld', 4: 'Bochum', 5: 'Braunschweig',
              6: 'Cottbus', 7: 'Darmstadt', 8: 'Dortmund', 9: 'Dresden', 10: 'Duisburg', 11: 'Ein Frankfurt',
              12: 'Erzgebirge Aue', 13: 'FC Koln', 14: 'Fortuna Dusseldorf', 15: 'Frankfurt FSV', 16: 'Freiburg', 17: 'Greuther Furth', 18: 'Hamburg',
                19: 'Hannover', 20: 'Heidenheim', 21: 'Hertha', 22: 'Hoffenheim', 23: 'Holstein Kiel', 24: 'Ingolstadt', 25: 'Kaiserslautern',
                  26: 'Karlsruhe', 27: 'Leverkusen', 28: "M'gladbach", 29: 'Magdeburg', 30: 'Mainz', 31: 'Munich 1860', 32: 'Nurnberg', 33:
                    'Paderborn', 34: 'RB Leipzig', 35: 'Regensburg', 36: 'Sandhausen', 37: 'Schalke 04', 38: 'St Pauli', 39: 'Stuttgart', 40: 
                    'Union Berlin', 41: 'Werder Bremen', 42: 'Wolfsburg', 43: 'Wurzburger Kickers'}}

    # Select the relevant columns
    relevant_cols = [
        'Div', 'HomeTeam', 'AwayTeam',
        'B365H', 'B365D', 'B365A', 
        'BbAv<2.5', 'BbAv>2.5', 
        'BbAvAHH', 'BbAvAHA', 'FTR'
    ]
    df = dataframe[relevant_cols]

    # Drop rows with missing values
    df = df.dropna()

    # Use the params to encode the 'HomeTeam' and 'AwayTeam' columns
    team_encoder = LabelEncoder()
    team_encoder.fit(list(PARAMS['teams'].values()))
    df['HomeTeam'] = team_encoder.transform(df['HomeTeam'])
    df['AwayTeam'] = team_encoder.transform(df['AwayTeam'])

    # Encode 'Div' column, without creating new columns
    df = pd.get_dummies(df, columns=['Div'], drop_first=True)

    return df

df = preprocess(data)

# save the preprocessed data
df.to_csv('preprocessed_data.csv', index=False)