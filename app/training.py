from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib


def load_data():
    iris = load_iris()
    X = iris.data
    y = iris.target
    feature_names = iris.feature_names
    target_names = iris.target_names

    return X, y, feature_names, target_names


def train_model(X, y):
    # Split the data into training and testing sets
    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a Random Forest Classifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)

    # Train the model
    model.fit(X_train, y_train)

    return model


def save_model(model, filename="model.pkl"):
    joblib.dump(model, filename)


def save_feature_and_target_names(
    feature_names, target_names, filename="feature_target_names.pkl"
):
    with open(filename, "wb") as f:
        joblib.dump((feature_names, target_names), f)
