# train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Load dataset
df = pd.read_csv("traffic_dataset.csv")

# Features: time, distance, cars
X = df[["time", "distance", "cars"]]
y = df["congestion"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train simple regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate
score = model.score(X_test, y_test)
print(f"Model R^2 score: {score:.2f}")

# Save model
joblib.dump(model, "congestion_model.pkl")
print("Model saved: congestion_model.pkl")
