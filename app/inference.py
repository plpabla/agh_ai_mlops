import numpy as np


def load_model(filename="model.pkl"):
    import joblib

    return joblib.load(filename)


def load_feature_and_target_names(filename="feature_target_names.pkl"):
    import joblib

    with open(filename, "rb") as f:
        feature_names, target_names = joblib.load(f)
    return feature_names, target_names


def predict(model, data):
    # Ensure the data is in the correct format
    data = np.array(data).reshape(1, -1)
    # Make a prediction
    prediction = model.predict(data)
    return prediction[0]
