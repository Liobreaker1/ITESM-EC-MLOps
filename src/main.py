
from typing import Optional
from fastapi import FastAPI

from src.prediction.predict import predict_model
from src.utils.logging import setup_logging

logger = setup_logging("api")


app = FastAPI()

@app.get("/")
def read_root():
    logger.info("Hello World!")
    return {"Hello": "World"}
    
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    logger.debug(f"item_id: {item_id}")
    return {"item_id": item_id, "q": q}

@app.post("/predict")
def predict(data: dict):
    logger.info(f"Received data for prediction: {data}")
    # Here you would typically call your model to make a prediction
    prediction = predict_model(data)
    logger.info(f"Prediction result: {prediction}")
    return prediction


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000, log_level="info")
    logger.info("API is running on http://localhost:8000")
    # Note: In production, you would not run the app this way, but rather use a server like Gunicorn or Uvicorn directly.
    