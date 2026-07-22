import streamlit as st
import pandas as pd
import os
from datetime import datetime

from utils.predictor import predict_vehicle
from utils.report_generator import generate_report

# -----------------------------------------------------
# Page Configuration
# -----------------------------------------------------

st.set_page_config(
    page_title="Reports",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Vehicle Reports")
st.markdown("### Generate AI Vehicle Health Reports")

st.divider()

# -----------------------------------------------------
# Sensor Inputs
# -----------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    engine = st.number_input("🌡 Engine Temperature (°C)", value=85.0)

    battery = st.number_input("🔋 Battery Voltage (V)", value=12.5)

    rpm = st.number_input("⚙ RPM", value=2500)

    speed = st.number_input("🚗 Speed (km/h)", value=60)

    vibration = st.number_input("📳 Engine Vibration", value=1.5)

with col2:

    oil = st.number_input("🛢 Oil Pressure", value=55.0)

    coolant = st.number_input("💧 Coolant Temperature", value=90.0)

    current = st.number_input("🔌 Battery Current", value=15.0)

    tire = st.number_input("🛞 Tire Pressure", value=32.0)

    ambient = st.number_input("🌤 Ambient Temperature", value=30.0)

st.divider()

# -----------------------------------------------------
# Generate Report
# -----------------------------------------------------

if st.button("📄 Generate Vehicle Report"):

    health, status, confidence = predict_vehicle(
        engine,
        battery,
        rpm,
        speed,
        vibration,
        oil,
        coolant,
        current,
        tire,
        ambient
    )

    if not os.path.exists("reports"):
        os.makedirs("reports")

    filename = f"reports/Vehicle_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

    generate_report(
        filename,
        health,
        status,
        confidence,
        engine,
        battery,
        rpm,
        speed,
        vibration,
        oil,
        coolant,
        current,
        tire,
        ambient
    )

    st.success("✅ PDF Report Generated Successfully")

    # -----------------------------------------------------
    # Download PDF
    # -----------------------------------------------------

    with open(filename, "rb") as pdf:

        st.download_button(
            label="⬇ Download PDF Report",
            data=pdf,
            file_name=os.path.basename(filename),
            mime="application/pdf"
        )

    st.divider()

    # -----------------------------------------------------
    # Prediction Summary
    # -----------------------------------------------------

    st.subheader("📊 Prediction Summary")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Vehicle Health", f"{health:.2f}%")

    with c2:
        st.metric("Status", status)

    with c3:
        st.metric("Confidence", f"{confidence:.2f}%")

    st.divider()

    # -----------------------------------------------------
    # Report Table
    # -----------------------------------------------------

    report_df = pd.DataFrame({

        "Parameter":[

            "Vehicle Health",

            "Vehicle Status",

            "Confidence",

            "Engine Temp",

            "Battery Voltage",

            "RPM",

            "Speed",

            "Engine Vibration",

            "Oil Pressure",

            "Coolant Temp",

            "Battery Current",

            "Tire Pressure",

            "Ambient Temp"

        ],

        "Value":[

            f"{health:.2f}%",

            status,

            f"{confidence:.2f}%",

            engine,

            battery,

            rpm,

            speed,

            vibration,

            oil,

            coolant,

            current,

            tire,

            ambient

        ]

    })

    st.dataframe(
        report_df,
        use_container_width=True,
        hide_index=True
    )

    # -----------------------------------------------------
    # Download CSV
    # -----------------------------------------------------

    csv = report_df.to_csv(index=False).encode("utf-8")

    st.download_button(

        label="⬇ Download CSV",

        data=csv,

        file_name="Vehicle_Report.csv",

        mime="text/csv"

    )

    st.divider()

    # -----------------------------------------------------
    # Report History (Current Session)
    # -----------------------------------------------------

    st.subheader("🕒 Current Report")

    st.info(f"Generated on: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")

    st.success("✅ Report generation completed successfully.")

else:

    st.info("Enter vehicle sensor values and click **Generate Vehicle Report**.")
