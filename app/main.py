from fastapi import FastAPI
from app import model, target_names
from .models.iris import PredictRequest, PredictResponse

app = FastAPI()


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    data = [[v for v in request.model_dump().values()]]
    prediction = model.predict(data)[0]
    return PredictResponse(prediction=str(target_names[prediction]))
