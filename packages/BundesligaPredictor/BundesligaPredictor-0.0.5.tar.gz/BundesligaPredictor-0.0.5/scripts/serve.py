from scripts.load import load_model
import numpy as np

def serve(df, batch):
    try:
        # Load the model
        model = load_model()

        # Reshape the data if necessary
        if len(df.shape) == 1:
            df = df.reshape(1, -1)

        # Make predictions
        probabilities = model.predict_proba(df)

        # Find the class with the highest probability for each prediction
        predictions = np.argmax(probabilities, axis=1)

    except ValueError as e:
        print(f"Error: {e}")
        raise ValueError('Incorrect values supplied to the model!')

    # If batch is True, return all predictions. Otherwise, return only the first one.
    return predictions if batch else predictions[0]
