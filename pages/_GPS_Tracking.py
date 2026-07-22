import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="GPS Tracking",
    page_icon="📍",
    layout="wide"
)

st.title("📍 Vehicle GPS & Speed Tracking")
st.markdown("### Real-Time Vehicle Location Monitoring")

st.divider()

# -----------------------------------------------------
# Sidebar Inputs
# -----------------------------------------------------

st.sidebar.header("Vehicle GPS Details")

latitude = st.sidebar.number_input(
    "Latitude",
    value=17.3850,
    format="%.6f"
)

longitude = st.sidebar.number_input(
    "Longitude",
    value=78.4867,
    format="%.6f"
)

speed = st.sidebar.slider(
    "Vehicle Speed (km/h)",
    0,
    180,
    60
)

heading = st.sidebar.slider(
    "Vehicle Direction (°)",
    0,
    360,
    90
)

# -----------------------------------------------------
# Vehicle Status
# -----------------------------------------------------

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("🚗 Speed", f"{speed} km/h")

with c2:
    st.metric("📍 Latitude", f"{latitude:.4f}")

with c3:
    st.metric("📍 Longitude", f"{longitude:.4f}")

st.divider()

# -----------------------------------------------------
# GPS Status
# -----------------------------------------------------

st.subheader("📡 GPS Status")

if speed == 0:
    st.warning("Vehicle is currently parked.")
else:
    st.success("Vehicle is moving.")

st.write(f"Direction: **{heading}°**")

st.divider()

# -----------------------------------------------------
# Map
# -----------------------------------------------------

st.subheader("🗺 Vehicle Location")

location = pd.DataFrame({
    "lat": [latitude],
    "lon": [longitude]
})

st.map(location)

st.divider()

# -----------------------------------------------------
# Location Information
# -----------------------------------------------------

st.subheader("📋 Current Coordinates")

info = pd.DataFrame({
    "Parameter": [
        "Latitude",
        "Longitude",
        "Speed",
        "Direction"
    ],
    "Value": [
        latitude,
        longitude,
        f"{speed} km/h",
        f"{heading}°"
    ]
})

st.dataframe(
    info,
    use_container_width=True,
    hide_index=True
)

st.divider()

# -----------------------------------------------------
# GPS Recommendations
# -----------------------------------------------------

st.subheader("🚦 Driving Recommendation")

if speed < 40:
    st.info("Driving at a safe speed.")

elif speed < 80:
    st.success("Optimal driving speed.")

elif speed < 120:
    st.warning("Drive carefully. Moderate speed.")

else:
    st.error("Overspeed detected! Reduce speed immediately.")

st.divider()

st.success("✅ GPS Tracking Module Running Successfully")
