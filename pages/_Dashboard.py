import streamlit as st

from utils.predictor import predict_vehicle
from utils.graphs import health_gauge


st.set_page_config(
    page_title="Dashboard",
    page_icon="🚗",
    layout="wide"
)


st.title("📊 Vehicle Health Dashboard")

st.markdown(
"""
### AI Powered Predictive Maintenance System
Real-time vehicle condition analysis using Machine Learning
"""
)


st.divider()


# Sensor Input

st.subheader("Vehicle Sensor Input")


col1,col2 = st.columns(2)


with col1:

    engine = st.number_input(
        "Engine Temperature °C",
        85.0
    )

    battery = st.number_input(
        "Battery Voltage",
        12.5
    )

    rpm = st.number_input(
        "RPM",
        2500
    )

    speed = st.number_input(
        "Speed km/h",
        60
    )

    vibration = st.number_input(
        "Engine Vibration",
        1.5
    )


with col2:

    oil = st.number_input(
        "Oil Pressure",
        55.0
    )

    coolant = st.number_input(
        "Coolant Temperature",
        90.0
    )

    current = st.number_input(
        "Battery Current",
        15.0
    )

    tire = st.number_input(
        "Tire Pressure",
        32.0
    )

    ambient = st.number_input(
        "Ambient Temperature",
        30.0
    )



if st.button(
    "Run AI Prediction",
    type="primary"
):

    health,status,confidence = predict_vehicle(
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


    st.divider()

    st.subheader("AI Prediction Result")


    c1,c2,c3 = st.columns(3)


    with c1:

        st.metric(
            "Health Score",
            f"{health:.2f}%"
        )


    with c2:

        st.metric(
            "Confidence",
            f"{confidence:.2f}%"
        )


    with c3:

        if status=="Healthy":

            st.success(status)

        elif status=="Maintenance Required":

            st.warning(status)

        else:

            st.error(status)



    st.plotly_chart(
        health_gauge(health),
        use_container_width=True
    )



    st.subheader("AI Decision")


    if status=="Healthy":

        st.success(
            "Vehicle condition is excellent. No maintenance required."
        )

    elif status=="Maintenance Required":

        st.warning(
            "Maintenance recommended. Inspect vehicle components."
        )

    else:

        st.error(
            "Critical fault detected. Immediate inspection required."
        )
