
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, Field
import pandas as pd
import numpy as np
import joblib
import logging
import time

from prometheus_client import Counter, Histogram
from prometheus_fastapi_instrumentator import Instrumentator

# Initialize FastAPI
app = FastAPI(
    title="Online Payment Fraud Detection System",
    description="Machine Learning Based Fraud Detection API",
    version="1.0"
)

# Load trained model
model = joblib.load("/content/fraud_model.pkl")

# Configure logging
logging.basicConfig(
    filename="/content/fraud_app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Prometheus metrics
REQUEST_COUNT = Counter(
    "transaction_request_count",
    "Total transaction requests"
)

PREDICTION_COUNT = Counter(
    "fraud_prediction_count",
    "Total predictions"
)

ERROR_COUNT = Counter(
    "application_error_count",
    "Total errors"
)

RESPONSE_TIME = Histogram(
    "transaction_response_time_seconds",
    "Transaction processing time"
)

# Prometheus instrumentation
Instrumentator().instrument(app).expose(
    app,
    endpoint="/metrics"
)

# Transaction input format
class Transaction(BaseModel):

    Transaction_Amount_INR: float
    Transaction_Hour: int = Field(ge=0, le=23)

    Payment_Method: str
    Transaction_Channel: str
    Device_Status: str
    Location_Type: str

    Transactions_Last_Hour: float
    Account_Age_Days: int
    Fraud_Risk_Signal: float
    Failed_OTP_Attempts: int
    Previous_Disputes: int
    Minutes_Since_Last_Transaction: int


# Health endpoint
@app.get("/health")
def health():

    return {
        "status": "healthy",
        "model": "loaded"
    }


# Prediction endpoint
@app.post("/predict")
def predict(transaction: Transaction):

    start_time = time.time()
    REQUEST_COUNT.inc()

    try:

        data = transaction.model_dump()

        # Handle invalid transaction amount
        if data["Transaction_Amount_INR"] == -999:
            data["Transaction_Amount_INR"] = np.nan

        # Feature engineering
        data["Hour_Sin"] = np.sin(
            2 * np.pi * data["Transaction_Hour"] / 24
        )

        data["Hour_Cos"] = np.cos(
            2 * np.pi * data["Transaction_Hour"] / 24
        )

        data["High_Amount"] = int(
            data["Transaction_Amount_INR"] > 2000
        ) if not pd.isna(
            data["Transaction_Amount_INR"]
        ) else 0

        # Convert to DataFrame
        input_df = pd.DataFrame([data])

        # Predict
        prediction = int(model.predict(input_df)[0])

        probability = float(
            model.predict_proba(input_df)[0][1]
        )

        result = (
            "Fraudulent" if prediction == 1
            else "Legitimate"
        )

        PREDICTION_COUNT.inc()

        processing_time = time.time() - start_time

        RESPONSE_TIME.observe(processing_time)

        # Record request and result
        logging.info(
            f"Transaction={data}, "
            f"Prediction={result}, "
            f"Fraud_Probability={probability:.4f}, "
            f"Processing_Time={processing_time:.4f}s"
        )

        return {
            "prediction": result,
            "fraud_probability": probability,
            "processing_time": processing_time
        }

    except Exception as e:

        ERROR_COUNT.inc()

        logging.exception("Prediction error")

        raise HTTPException(
            status_code=500,
            detail="Prediction failed"
        )
