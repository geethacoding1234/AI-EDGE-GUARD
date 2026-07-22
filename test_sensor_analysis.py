from utils.sensor_analysis import *

print("Fuel Efficiency")
print(calculate_fuel_efficiency(2500, 60, 1.5))

print()

print("Maintenance Countdown")
print(maintenance_countdown(92))

print()

print("Recommendations")
print(maintenance_recommendations(
    85,
    12.5,
    2500,
    55,
    90,
    1.5,
    32,
    15
))

print()

print("Sensor Health")
print(sensor_health(85, 12.5))
