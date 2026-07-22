import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_absolute_error

from xgboost import XGBRegressor
from xgboost import XGBClassifier

# -------------------------------
# Load Dataset
# -------------------------------

data = pd.read_excel("vehicle_health_dataset_1000.xlsx")

# -------------------------------
# Input Features
# -------------------------------

X = data[[
    "EngineTemp",
    "BatteryVoltage",
    "RPM",
    "Speed",
    "EngineVibration",
    "OilPressure",
    "CoolantTemp",
    "BatteryCurrent",
    "TirePressure",
    "AmbientTemp"
]]

# -------------------------------
# Outputs
# -------------------------------

health = data["HealthScore"]

status = data["Status"]

# Encode Status

encoder = LabelEncoder()

status = encoder.fit_transform(status)

# -------------------------------
# Train Test Split
# -------------------------------

X_train, X_test, health_train, health_test, status_train, status_test = train_test_split(
    X,
    health,
    status,
    test_size=0.20,
    random_state=42
)

# -------------------------------
# XGBoost Regressor
# -------------------------------

health_model = XGBRegressor(

    n_estimators=300,

    learning_rate=0.05,

    max_depth=6,

    random_state=42

)

health_model.fit(X_train, health_train)

# -------------------------------
# XGBoost Classifier
# -------------------------------

status_model = XGBClassifier(

    n_estimators=300,

    learning_rate=0.05,

    max_depth=6,

    eval_metric="mlogloss",

    random_state=42

)

status_model.fit(X_train, status_train)

# -------------------------------
# Predictions
# -------------------------------

health_prediction = health_model.predict(X_test)

status_prediction = status_model.predict(X_test)

print()

print("Health Score MAE")

print(mean_absolute_error(health_test, health_prediction))

print()

print("Status Accuracy")

print(accuracy_score(status_test, status_prediction))

# -------------------------------
# Save Models
# -------------------------------

joblib.dump(health_model, "health_model.pkl")

joblib.dump(status_model, "status_model.pkl")

joblib.dump(encoder, "label_encoder.pkl")

print()

print("Models Saved Successfully")
