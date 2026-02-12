# predict.py

import joblib
import pandas as pd

# Load trained model
model = joblib.load("congestion_model.pkl")

def predict_congestion(time, distance, cars):
    df = pd.DataFrame([{"time": time, "distance": distance, "cars": cars}])
    return model.predict(df)[0]

# Example usage
if __name__ == "__main__":
    congestion = predict_congestion(time=10, distance=8, cars=3)
    print(f"Predicted congestion: {congestion:.2f}")
