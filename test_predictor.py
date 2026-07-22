from utils.predictor import predict_vehicle

health, status, confidence = predict_vehicle(
    85,      # Engine Temperature
    12.5,    # Battery Voltage
    2500,    # RPM
    60,      # Speed
    1.5,     # Engine Vibration
    55,      # Oil Pressure
    90,      # Coolant Temperature
    15,      # Battery Current
    32,      # Tire Pressure
    30       # Ambient Temperature
)

print("Health Score :", health)
print("Vehicle Status :", status)
print("Confidence :", confidence)
