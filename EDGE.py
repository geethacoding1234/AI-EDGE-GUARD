import joblib
import pandas as pd

# Load Models

health_model = joblib.load("health_model.pkl")

status_model = joblib.load("status_model.pkl")

encoder = joblib.load("label_encoder.pkl")

print()

print("Enter Sensor Values")

engine = float(input("Engine Temperature : "))

battery = float(input("Battery Voltage : "))

rpm = int(input("RPM : "))

speed = float(input("Speed : "))

vibration = float(input("Engine Vibration : "))

oil = float(input("Oil Pressure : "))

coolant = float(input("Coolant Temperature : "))

current = float(input("Battery Current : "))

tire = float(input("Tire Pressure : "))

ambient = float(input("Ambient Temperature : "))

sample = pd.DataFrame({

"EngineTemp":[engine],

"BatteryVoltage":[battery],

"RPM":[rpm],

"Speed":[speed],

"EngineVibration":[vibration],

"OilPressure":[oil],

"CoolantTemp":[coolant],

"BatteryCurrent":[current],

"TirePressure":[tire],

"AmbientTemp":[ambient]

})

# Predict

health = health_model.predict(sample)[0]

status = status_model.predict(sample)

status = encoder.inverse_transform(status)[0]

confidence = status_model.predict_proba(sample).max()*100

print()

print("============================")

print(" VEHICLE HEALTH REPORT")

print("============================")

print(f"Health Score : {health:.2f}%")

print(f"Vehicle Status : {status}")

print(f"Confidence : {confidence:.2f}%")
