import pickle
import numpy as np

def make_prediction(data: list[float]):
    """
    Load model and make prediction on input data.

    Args:
        data (list[float]): Input features for prediction.

    Returns:
        numpy.ndarray: Predicted output.
    """
    try:
        # Load the model
        model = pickle.load(open("random_forest_model.pkl", "rb"))
    except FileNotFoundError:
        raise FileNotFoundError("The model file 'model.pkl' was not found. Please ensure it is in the correct directory.")

    try:
        # Prepare data and make prediction
        data = np.array(data).reshape(1, -1)
        prediction = model.predict(data)
    except Exception as e:
        raise ValueError(f"Error during prediction: {e}")
    
    return prediction
