# CloudForAI-ML-Exercise3
## Overview

This project is a machine learning prediction API built using FastAPI. The API allows users to make predictions using a pre-trained Random Forest classifier, trained on the Titanic dataset (Titanic-Dataset.csv). It also supports easy deployment using Docker for production-grade setups.

## Setup and Installation
### Prerequisites
    
    ```
    Python 3.10+
    Docker (optional, for containerized deployment)
    ```

### Steps to Run Locally

1. Clone the repository:

    ```
    git clone https://github.com/Tim-Mortier/CloudForAI-ML-Exercise3.git
    cd CloudForAI-ML-Exercise3
    ```    

2. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

3. Train the model and generate random_forest_model.pkl:

    ```
    python model.py
    ```

4. Start the API server:

    ```
    uvicorn app.main:app --reload
    ```

5. Open your browser and visit http://127.0.0.1:8000/docs to explore the API using Swagger UI.

## API Endpoints

1. GET `/`

    Returns a welcome message and guidance for using the `/predict` endpoint.

    Response:

    ```
    {
        "message": "Welcome to the prediction API! Use the /predict endpoint to make predictions."
    }
    ```

2. POST `/predict`

    Accepts a JSON object with input data for prediction. Data corresponds to the features used by the Random Forest model (e.g., Age, Pclass, SibSp).

    Request Body:

    ```
    {
        "data": [3, "male", 22, 1, 0, 7.25, "S"]
    }
    ```

    Response:

    ```
    {
        "prediction": [0]
    }
    ```

3. GET `/favicon.ico`

    Serves the favicon for the application.

## Testing the API

You can test the API using curl or tools like Postman.

Example Curl Command:

    ```
    curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d "{\"data\": [0,3,1,22,1,0,7.25,0,1]}"
    ```

## Docker Support

### Building and Running the Docker Image

1. Build the Docker image:

    ```
    docker build -t fastapi-predictor .
    ```

2. Run the Docker container:

    ```
    docker run -p 8000:8000 fastapi-predictor
    ```

3. Access the API at http://127.0.0.1:8000.

