import pandas as pd
from sklearn.preprocessing import LabelEncoder
from preprocess import FootballDataPreprocessor

data = pd.read_csv('data/germany_all.csv')

preprocessor = FootballDataPreprocessor(data)

df = preprocessor.preprocess()

#give FTR column from data to df
df['FTR'] = data['FTR']

df.to_csv('data/preprocessed.csv', index=False)