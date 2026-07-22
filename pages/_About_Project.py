import streamlit as st

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="About EdgeGuard AI",
    page_icon="ℹ️",
    layout="wide"
)

# ---------------------------------------------------
# Title
# ---------------------------------------------------
st.title("ℹ️ About EdgeGuard AI")
st.markdown("---")

# ---------------------------------------------------
# Overview
# ---------------------------------------------------
st.header("🚗 Project Overview")

st.write("""
**EdgeGuard AI** is an AI-powered Vehicle Health Monitoring and Predictive
Maintenance System developed to monitor real-time vehicle sensor data,
predict vehicle health, detect faults, and provide intelligent maintenance
recommendations before failures occur.

The system uses Machine Learning models trained on vehicle sensor data to
estimate the health of the vehicle and classify its current condition.
""")

st.markdown("---")

# ---------------------------------------------------
# Objectives
# ---------------------------------------------------
st.header("🎯 Project Objectives")

st.markdown("""
- Predict vehicle health using Artificial Intelligence
- Detect maintenance requirements
- Identify critical faults
- Monitor real-time vehicle sensors
- Improve vehicle safety
- Increase fuel efficiency
- Reduce maintenance cost
- Generate professional PDF reports
""")

st.markdown("---")

# ---------------------------------------------------
# Technologies
# ---------------------------------------------------
st.header("⚙️ Technologies Used")

col1, col2 = st.columns(2)

with col1:
    st.info("""
**Programming**

- Python
- Streamlit
- Pandas
- NumPy
- Joblib
""")

with col2:
    st.info("""
**Machine Learning**

- Scikit-Learn
- Random Forest
- Plotly
- ReportLab
- OpenPyXL
""")

st.markdown("---")

# ---------------------------------------------------
# Dataset
# ---------------------------------------------------
st.header("📊 Dataset Information")

st.success("""
Dataset Size : 1000 Vehicle Records

Input Features : 10 Vehicle Sensors

Models Used:
• Random Forest Regressor
• Random Forest Classifier

Outputs:
• Vehicle Health Score
• Vehicle Status
""")

st.markdown("---")

# ---------------------------------------------------
# Sensors
# ---------------------------------------------------
st.header("📡 Vehicle Sensors")

sensor_col1, sensor_col2 = st.columns(2)

with sensor_col1:
    st.write("🌡 Engine Temperature")
    st.write("🔋 Battery Voltage")
    st.write("⚙ Engine RPM")
    st.write("🚗 Vehicle Speed")
    st.write("📳 Engine Vibration")

with sensor_col2:
    st.write("🛢 Oil Pressure")
    st.write("💧 Coolant Temperature")
    st.write("🔌 Battery Current")
    st.write("🛞 Tire Pressure")
    st.write("🌤 Ambient Temperature")

st.markdown("---")

# ---------------------------------------------------
# Features
# ---------------------------------------------------
st.header("✨ Key Features")

st.markdown("""
✅ AI Vehicle Health Prediction

✅ Real-Time Vehicle Monitoring

✅ Smart Maintenance Recommendations

✅ Predictive Maintenance Countdown

✅ Fuel Efficiency Monitor

✅ GPS & Speed Tracking

✅ Interactive Graphs

✅ Dataset Explorer

✅ PDF Report Generation

✅ Machine Learning Dashboard

✅ Multi-Page Professional Interface
""")

st.markdown("---")

# ---------------------------------------------------
# Workflow
# ---------------------------------------------------
st.header("🔄 System Workflow")

st.write("""
Vehicle Sensors
⬇

Data Collection
⬇

Machine Learning Prediction
⬇

Vehicle Health Analysis
⬇

Maintenance Recommendation
⬇

PDF Report Generation
""")
