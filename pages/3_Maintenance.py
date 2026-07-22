import streamlit as st
from utils.sensor_analysis import (
    calculate_fuel_efficiency,
    maintenance_countdown,
    maintenance_recommendations,
)
from utils.voice import vehicle_voice_alert

# -----------------------------------------------------
# Page Configuration
# -----------------------------------------------------

st.set_page_config(
    page_title="Maintenance",
    page_icon="🛠",
    layout="wide"
)

st.title("🛠 Smart Maintenance Center")
st.markdown("### AI-Based Predictive Maintenance")

st.divider()

# -----------------------------------------------------
# Sidebar Inputs
# -----------------------------------------------------

st.sidebar.header("Vehicle Sensor Values")

health = st.sidebar.slider("Vehicle Health Score", 0, 100, 92)

engine = st.sidebar.slider("Engine Temperature (°C)", 50.0, 150.0, 85.0)

battery = st.sidebar.slider("Battery Voltage (V)", 8.0, 15.0, 12.5)

rpm = st.sidebar.slider("RPM", 500, 7000, 2500)

speed = st.sidebar.slider("Speed (km/h)", 0, 180, 60)

vibration = st.sidebar.slider("Engine Vibration", 0.0, 10.0, 1.5)

oil = st.sidebar.slider("Oil Pressure", 10.0, 100.0, 55.0)

coolant = st.sidebar.slider("Coolant Temperature", 40.0, 130.0, 90.0)

current = st.sidebar.slider("Battery Current", 0.0, 60.0, 15.0)

tire = st.sidebar.slider("Tire Pressure", 10.0, 50.0, 32.0)

# -----------------------------------------------------
# Calculations
# -----------------------------------------------------

fuel = calculate_fuel_efficiency(rpm, speed, vibration)

remaining = maintenance_countdown(health)

recommendations = maintenance_recommendations(
    engine,
    battery,
    rpm,
    oil,
    coolant,
    vibration,
    tire,
    current
)

# -----------------------------------------------------
# KPI Cards
# -----------------------------------------------------

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("⛽ Fuel Efficiency", f"{fuel:.2f} km/L")

with c2:
    st.metric("⏳ Remaining Service", f"{remaining} km")

with c3:
    st.metric("❤️ Vehicle Health", f"{health}%")

st.divider()

# -----------------------------------------------------
# Maintenance Recommendations
# -----------------------------------------------------

st.subheader("🤖 AI Maintenance Recommendations")

for item in recommendations:
    st.info(item)

st.divider()

# -----------------------------------------------------
# Voice Alert
# -----------------------------------------------------

st.subheader("🔊 Voice Alert")

status = "Healthy"

if health < 40:
    status = "Critical Fault"

elif health < 70:
    status = "Maintenance Required"

st.write(f"Current Status : **{status}**")

if st.button("🔊 Play Voice Alert"):
    vehicle_voice_alert(status)
    st.success("Voice alert completed.")

st.divider()

# -----------------------------------------------------
# Component Health
# -----------------------------------------------------

st.subheader("🔧 Component Health")

components = {

    "Engine": 100 - max(0, engine - 80),

    "Battery": battery * 8,

    "Oil System": oil,

    "Cooling System": 100 - max(0, coolant - 85),

    "Tires": tire * 3,

}

for name, value in components.items():

    value = max(0, min(100, value))

    st.write(name)

    st.progress(int(value))

st.divider()

# -----------------------------------------------------
# Service Checklist
# -----------------------------------------------------

st.subheader("📋 Recommended Service Checklist")

checklist = [

    "✔ Check Engine Oil",

    "✔ Inspect Battery",

    "✔ Inspect Cooling System",

    "✔ Check Tire Pressure",

    "✔ Inspect Brake System",

    "✔ Check Electrical Connections",

    "✔ Clean Air Filter",

    "✔ Inspect Belts",

]

for item in checklist:

    st.checkbox(item)

st.divider()

# -----------------------------------------------------
# Maintenance Schedule
# -----------------------------------------------------

st.subheader("📅 Suggested Next Service")

if health >= 90:

    st.success("Next Service after 10,000 km")

elif health >= 70:

    st.warning("Next Service after 5,000 km")

elif health >= 50:

    st.warning("Service Recommended within 2,000 km")

else:

    st.error("Immediate Service Required")

st.divider()

st.success("✅ AI Maintenance Module Running Successfully")
