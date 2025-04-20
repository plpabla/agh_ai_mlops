from .training import load_data, train_model, save_model, save_feature_and_target_names
from .inference import load_model, load_feature_and_target_names
import os


print(">>> Starting the ML API...")
if os.path.exists("model.pkl"):
    print(">>> Loading existing model...")
    model = load_model()
    feature_names, target_names = load_feature_and_target_names()
else:
    print(">>> No existing model found. Training a new model...")
    X, y, feature_names, target_names = load_data()
    model = train_model(X, y)
    save_model(model)
    save_feature_and_target_names(feature_names, target_names)
