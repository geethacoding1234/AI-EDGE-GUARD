import streamlit as st
import pandas as pd
import joblib

# ----------------------------
# Load Models
# ----------------------------
health_model = joblib.load("health_model.pkl")
status_model = joblib.load("status_model.pkl")
encoder = joblib.load("label_encoder.pkl")

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="EdgeGuard AI",
    page_icon="🚗",
    layout="wide"
)

# ----------------------------
# Title
# ----------------------------
st.title("🚗 EdgeGuard AI")
st.subheader("Real-Time Vehicle Health Monitoring & Predictive Maintenance")

st.markdown("---")

# ----------------------------
# Sensor Inputs
# ----------------------------
col1, col2 = st.columns(2)

with col1:
    engine = st.number_input("🌡 Engine Temperature (°C)", value=85.0)
    battery = st.number_input("🔋 Battery Voltage (V)", value=12.5)
    rpm = st.number_input("⚙ Engine RPM", value=2500)
    speed = st.number_input("🚗 Vehicle Speed (km/h)", value=60.0)
    vibration = st.number_input("📳 Engine Vibration", value=1.5)

with col2:
    oil = st.number_input("🛢 Oil Pressure (PSI)", value=55.0)
    coolant = st.number_input("💧 Coolant Temperature (°C)", value=90.0)
    current = st.number_input("🔌 Battery Current (A)", value=15.0)
    tire = st.number_input("🛞 Tire Pressure (PSI)", value=32.0)
    ambient = st.number_input("🌤 Ambient Temperature (°C)", value=30.0)

st.markdown("---")

# ----------------------------
# Predict Button
# ----------------------------
if st.button("🚗 Predict Vehicle Health"):

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

    # ----------------------------
    # Predictions
    # ----------------------------
    health = health_model.predict(sample)[0]

    status = status_model.predict(sample)
    status = encoder.inverse_transform(status)[0]

    confidence = status_model.predict_proba(sample).max() * 100

    st.markdown("## 📊 Prediction Results")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("🚗 Vehicle Health Score", f"{health:.2f}%")

    with c2:
        st.metric("🎯 Prediction Confidence", f"{confidence:.2f}%")

    with c3:
        if status == "Healthy":
            st.success("🟢 Healthy")
        elif status == "Maintenance Required":
            st.warning("🟡 Maintenance Required")
        else:
            st.error("🔴 Critical Fault")

    # ----------------------------
    # Progress Bar
    # ----------------------------
    st.progress(min(max(int(health), 0), 100))

    # ----------------------------
    # Maintenance Alert
    # ----------------------------
    st.markdown("## 🚨 Maintenance Alert")

    if status == "Healthy":
        st.success("✅ Vehicle is operating normally. No maintenance required.")

    elif status == "Maintenance Required":
        st.warning("⚠ Vehicle needs maintenance soon. Please inspect all critical components.")

    else:
        st.error("🚨 Critical fault detected! Stop the vehicle immediately and perform maintenance.")

    # ----------------------------
    # Sensor Summary
    # ----------------------------
    st.markdown("## 📋 Sensor Summary")

    sensor_summary = pd.DataFrame({
        "🌡 Engine Temp (°C)": [engine],
        "🔋 Battery (V)": [battery],
        "⚙ RPM": [rpm],
        "🚗 Speed (km/h)": [speed],
        "📳 Vibration": [vibration],
        "🛢 Oil Pressure": [oil],
        "💧 Coolant Temp": [coolant],
        "🔌 Battery Current": [current],
        "🛞 Tire Pressure": [tire],
        "🌤 Ambient Temp": [ambient]
    })

    st.dataframe(
        sensor_summary,
        use_container_width=True,
        hide_index=True
    )
