import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from hyperopt import hp, fmin, tpe, STATUS_OK, Trials

# Objective function for hyperopt
def objective(params):
    params = {'n_estimators': int(params['n_estimators']), 
              'max_depth': int(params['max_depth']), 
              'min_samples_leaf': int(params['min_samples_leaf']),
              'criterion': params['criterion'],
              'bootstrap': params['bootstrap']
              }
    
    clf = RandomForestClassifier(**params)
    clf.fit(X_train, y_train)
    predictions = clf.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    
    return {'loss': -accuracy, 'status': STATUS_OK}

# Load and preprocess dataset
df_preprocessed = pd.read_csv('data/preprocessed_data.csv')  # replace with your csv path


# Split dataset
X = df_preprocessed.drop(columns=['FTR'])
y = df_preprocessed['FTR']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define search space for hyperparameters
space = {
    'n_estimators': hp.quniform('n_estimators', 100, 2000, 1),
    'max_depth': hp.quniform('max_depth', 1, 20, 1),
    'criterion': hp.choice('criterion', ['gini', 'entropy']),
    'bootstrap': hp.choice('bootstrap', [True, False]),
    'min_samples_leaf': hp.quniform('min_samples_leaf', 1, 10, 1),
}


# Run optimization
trials = Trials()
best = fmin(fn=objective,
            space=space,
            algo=tpe.suggest,
            max_evals=100,
            trials=trials)

print("Best hyperparameters: ", best)

# Train model with best hyperparameters
best['n_estimators'] = int(best['n_estimators'])
best['max_depth'] = int(best['max_depth'])
best['min_samples_leaf'] = int(best['min_samples_leaf'])
best['criterion'] = 'entropy' if best['criterion'] == 1 else 'gini'
best['bootstrap'] = True if best['bootstrap'] == 1 else False


model = RandomForestClassifier(**best)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))


# Save model
import pickle
import os
os.makedirs('../model', exist_ok=True)
pickle.dump(model, open('../model/model.pkl', 'wb'))