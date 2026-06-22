import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
df = pd.read_csv("student-mat.csv", sep=";")

# Create pass/fail column
# Pass = G3 >= 10
# Fail = G3 < 10
df["pass_fail"] = (df["G3"] >= 10).astype(int)

# Select features
X = df[["studytime", "absences", "G1"]]

# Target
y = df["pass_fail"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Test accuracy
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy:.2f}")

# Save model
joblib.dump(model, "model.pkl")

print("Model saved as model.pkl")