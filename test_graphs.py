import streamlit as st

from utils.graphs import (
    health_gauge,
    engine_temp_gauge,
    rpm_gauge,
    battery_gauge,
    sensor_chart
)

st.title("Graph Testing")

st.plotly_chart(health_gauge(92))

st.plotly_chart(engine_temp_gauge(85))

st.plotly_chart(rpm_gauge(2500))

st.plotly_chart(battery_gauge(12.5))

st.plotly_chart(
    sensor_chart(
        85,
        12.5,
        2500,
        60,
        1.5,
        55,
        90,
        15,
        32,
        30,
    )
)
