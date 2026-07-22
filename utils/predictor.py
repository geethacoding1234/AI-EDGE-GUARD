import pandas as pd
import joblib

# Load models only once
health_model = joblib.load("health_model.pkl")
status_model = joblib.load("status_model.pkl")
encoder = joblib.load("label_encoder.pkl")


def predict_vehicle(
    engine,
    battery,
    rpm,
    speed,
    vibration,
    oil,
    coolant,
    current,
    tire,
    ambient,
):
    sample = pd.DataFrame({
        "EngineTemp": [engine],
        "BatteryVoltage": [battery],
        "RPM": [rpm],
        "Speed": [speed],
        "EngineVibration": [vibration],
        "OilPressure": [oil],
        "CoolantTemp": [coolant],
        "BatteryCurrent": [current],
        "TirePressure": [tire],
        "AmbientTemp": [ambient]
    })

    health = health_model.predict(sample)[0]

    status = status_model.predict(sample)
    status = encoder.inverse_transform(status)[0]

    confidence = status_model.predict_proba(sample).max() * 100

    return health, status, confidence
