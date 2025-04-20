from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_welcome_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the ML API"}


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_predict():
    # Assuming the model expects 4 features for prediction
    data = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2,
    }
    response = client.post("/predict", json=data)
    assert response.status_code == 200
    assert "prediction" in response.json()
    # Check if the prediction is one of the expected classes
    assert response.json()["prediction"] in ["setosa", "versicolor", "virginica"]
