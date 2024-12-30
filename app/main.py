from fastapi import FastAPI
from fastapi.responses import FileResponse
from app.routes.prediction import router as prediction_router

app = FastAPI(title="Prediction API", version="1.0.0")

@app.get("/")
def read_root():
    """
    Root endpoint providing a welcome message.
    """
    return {"message": "Welcome to the prediction API! Use the /predict endpoint to make predictions."}

app.include_router(prediction_router)
