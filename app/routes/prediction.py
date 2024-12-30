from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, ValidationError
from app.utils.predictor import make_prediction

router = APIRouter()

class PredictionInput(BaseModel):
    data: list

@router.post("/predict")
def predict(input_data: PredictionInput):
    """
    Endpoint to make predictions.

    Args:
        input_data (PredictionInput): Input data for prediction.

    Returns:
        dict: JSON response with prediction results.
    """
    try:
        prediction = make_prediction(input_data.data)
        return {"prediction": prediction.tolist()}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=f"Invalid input data: {ve}")
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Model file not found.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")
