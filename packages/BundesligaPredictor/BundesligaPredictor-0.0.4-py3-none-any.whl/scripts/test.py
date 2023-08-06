import pandas as pd
from sklearn.preprocessing import LabelEncoder
from pre_process import FootballDataPreprocessor

data = pd.read_csv('data/germany_all.csv')

preprocessor = FootballDataPreprocessor(data)

data = preprocessor.preprocess()

print(data.head())
