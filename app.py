import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="EdgeGuard AI",
    page_icon="🚗",
    layout="wide"
)

# ==========================================================
# LOAD CSS
# ==========================================================

try:
    with open("style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )
except:
    pass

# ==========================================================
# LOAD MODELS
# ==========================================================

health_model = joblib.load("health_model.pkl")
status_model = joblib.load("status_model.pkl")
encoder = joblib.load("label_encoder.pkl")

# ==========================================================
# HEADER
# ==========================================================

st.title("🚗 EdgeGuard AI")
st.subheader("Real-Time Vehicle Health Monitoring & Predictive Maintenance")

st.markdown("---")

left, middle, right = st.columns(3)

with left:
    st.info("🚘 Vehicle ID : VEH-001")

with middle:
    st.info("📡 Connection : Connected")

with right:
    st.info(
        "🕒 " +
        datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    )

st.markdown("---")

# ==========================================================
# SENSOR INPUTS
# ==========================================================

st.header("📥 Vehicle Sensor Inputs")

col1, col2 = st.columns(2)

with col1:

    engine = st.number_input(
        "🌡 Engine Temperature (°C)",
        min_value=0.0,
        max_value=150.0,
        value=85.0
    )

    battery = st.number_input(
        "🔋 Battery Voltage (V)",
        min_value=8.0,
        max_value=15.0,
        value=12.5
    )

    rpm = st.number_input(
        "⚙ Engine RPM",
        min_value=0,
        max_value=6000,
        value=2500
    )

    speed = st.number_input(
        "🚗 Vehicle Speed (km/h)",
        min_value=0.0,
        max_value=220.0,
        value=60.0
    )

    vibration = st.number_input(
        "📳 Engine Vibration",
        min_value=0.0,
        max_value=10.0,
        value=1.5
    )

with col2:

    oil = st.number_input(
        "🛢 Oil Pressure",
        min_value=0.0,
        max_value=100.0,
        value=55.0
    )

    coolant = st.number_input(
        "💧 Coolant Temperature",
        min_value=0.0,
        max_value=150.0,
        value=90.0
    )

    current = st.number_input(
        "🔌 Battery Current",
        min_value=0.0,
        max_value=100.0,
        value=15.0
    )

    tire = st.number_input(
        "🛞 Tire Pressure",
        min_value=0.0,
        max_value=50.0,
        value=32.0
    )

    ambient = st.number_input(
        "🌤 Ambient Temperature",
        min_value=-20.0,
        max_value=60.0,
        value=30.0
    )

st.markdown("")

predict = st.button(
    "🚗 Predict Vehicle Health",
    use_container_width=True
)

# ==========================================================
# AI PREDICTION
# ==========================================================

if predict:

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

    health = health_model.predict(sample)[0]

    status = status_model.predict(sample)

    status = encoder.inverse_transform(status)[0]

    confidence = status_model.predict_proba(sample).max()*100

    st.markdown("---")

    st.header("📊 AI Dashboard")

    dash1, dash2 = st.columns([1.5,1])

    # ======================================================
    # SPEEDOMETER
    # ======================================================

    with dash1:

        gauge = go.Figure(go.Indicator(

            mode="gauge+number",

            value=health,

            number={"suffix":"%"},

            title={"text":"Vehicle Health Score"},

            gauge={

                "axis":{"range":[0,100]},

                "bar":{"color":"darkblue"},

                "steps":[

                    {"range":[0,50],"color":"#ff4d4d"},

                    {"range":[50,80],"color":"orange"},

                    {"range":[80,100],"color":"green"}

                ],

                "threshold":{

                    "line":{"color":"white","width":4},

                    "thickness":0.75,

                    "value":health

                }

            }

        ))

        gauge.update_layout(
            height=360,
            margin=dict(l=20,r=20,t=50,b=20)
        )

        st.plotly_chart(
            gauge,
            use_container_width=True
        )

    # ======================================================
    # METRICS + AI CARD
    # ======================================================

    with dash2:

        st.metric(
            "🎯 Prediction Confidence",
            f"{confidence:.2f}%"
        )

        st.progress(
            min(max(int(health),0),100)
        )

        if status=="Healthy":

            st.markdown(
            """
<div style="
background:#16a34a;
padding:25px;
border-radius:15px;
text-align:center;
color:white;
">
<h2>🟢 Healthy</h2>
<p>Vehicle Operating Normally</p>
</div>
""",
unsafe_allow_html=True
            )

        elif status=="Maintenance Required":

            st.markdown(
            """
<div style="
background:#f59e0b;
padding:25px;
border-radius:15px;
text-align:center;
color:white;
">
<h2>🟡 Maintenance Required</h2>
<p>Vehicle Needs Inspection</p>
</div>
""",
unsafe_allow_html=True
            )

        else:

            st.markdown(
            """
<div style="
background:#dc2626;
padding:25px;
border-radius:15px;
text-align:center;
color:white;
">
<h2>🔴 Critical Fault</h2>
<p>Immediate Service Required</p>
</div>
""",
unsafe_allow_html=True)

                # ======================================================
    # MAINTENANCE RECOMMENDATIONS
    # ======================================================

    st.markdown("---")
    st.header("🚨 Maintenance Recommendations")

    if status == "Healthy":

        st.success("""
### Recommended Actions

✔ Engine condition is normal

✔ Battery voltage is stable

✔ Cooling system is functioning properly

✔ Continue normal driving

✔ Schedule the next routine service after **500 km**
""")

    elif status == "Maintenance Required":

        st.warning("""
### Recommended Actions

✔ Replace engine oil

✔ Inspect coolant level

✔ Check battery health

✔ Inspect tire pressure

✔ Reduce continuous high RPM driving

✔ Schedule vehicle servicing immediately
""")

    else:

        st.error("""
### Recommended Actions

✔ Stop the vehicle immediately

✔ Inspect engine cooling system

✔ Check oil pressure

✔ Inspect engine vibration

✔ Contact an authorized service center

✔ Do not continue driving until repaired
""")

    # ======================================================
    # SENSOR SUMMARY
    # ======================================================

    st.markdown("---")
    st.header("📋 Sensor Summary")

    sensor_summary = pd.DataFrame({

        "🌡 Engine Temp (°C)" : [engine],

        "🔋 Battery (V)" : [battery],

        "⚙ RPM" : [rpm],

        "🚗 Speed (km/h)" : [speed],

        "📳 Vibration" : [vibration],

        "🛢 Oil Pressure" : [oil],

        "💧 Coolant Temp" : [coolant],

        "🔌 Battery Current" : [current],

        "🛞 Tire Pressure" : [tire],

        "🌤 Ambient Temp" : [ambient]

    })

    st.dataframe(
        sensor_summary,
        use_container_width=True,
        hide_index=True
    )

    # ======================================================
    # LIVE SENSOR BAR GRAPH
    # ======================================================

    st.markdown("---")
    st.header("📊 Live Sensor Analysis")

    graph = pd.DataFrame({

        "Sensor":[

            "Engine Temp",

            "Battery",

            "RPM",

            "Speed",

            "Vibration",

            "Oil Pressure",

            "Coolant",

            "Battery Current",

            "Tire Pressure",

            "Ambient"

        ],

        "Value":[

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

    fig = px.bar(

        graph,

        x="Sensor",

        y="Value",

        color="Value",

        color_continuous_scale="Turbo",

        text="Value"

    )

    fig.update_layout(

        height=500,

        title="Vehicle Sensor Readings",

        xaxis_title="Sensors",

        yaxis_title="Values"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.markdown("---")

    st.header("📈 Individual Sensor Gauges")

    g1, g2, g3 = st.columns(3)
        # ======================================================
    # ENGINE TEMPERATURE GAUGE
    # ======================================================

    with g1:

        engine_gauge = go.Figure(go.Indicator(

            mode="gauge+number",

            value=engine,

            title={"text":"🌡 Engine Temperature (°C)"},

            gauge={

                "axis":{"range":[0,150]},

                "bar":{"color":"red"},

                "steps":[

                    {"range":[0,80],"color":"green"},

                    {"range":[80,110],"color":"orange"},

                    {"range":[110,150],"color":"red"}

                ]

            }

        ))

        engine_gauge.update_layout(height=320)

        st.plotly_chart(
            engine_gauge,
            use_container_width=True
        )

    # ======================================================
    # RPM GAUGE
    # ======================================================

    with g2:

        rpm_gauge = go.Figure(go.Indicator(

            mode="gauge+number",

            value=rpm,

            title={"text":"⚙ Engine RPM"},

            gauge={

                "axis":{"range":[0,6000]},

                "bar":{"color":"royalblue"},

                "steps":[

                    {"range":[0,2500],"color":"green"},

                    {"range":[2500,4500],"color":"orange"},

                    {"range":[4500,6000],"color":"red"}

                ]

            }

        ))

        rpm_gauge.update_layout(height=320)

        st.plotly_chart(
            rpm_gauge,
            use_container_width=True
        )

    # ======================================================
    # BATTERY VOLTAGE GAUGE
    # ======================================================

    with g3:

        battery_gauge = go.Figure(go.Indicator(

            mode="gauge+number",

            value=battery,

            title={"text":"🔋 Battery Voltage (V)"},

            gauge={

                "axis":{"range":[8,15]},

                "bar":{"color":"green"},

                "steps":[

                    {"range":[8,11],"color":"red"},

                    {"range":[11,12],"color":"orange"},

                    {"range":[12,15],"color":"green"}

                ]

            }

        ))

        battery_gauge.update_layout(height=320)

        st.plotly_chart(
            battery_gauge,
            use_container_width=True
        )

    # ======================================================
    # FOOTER
    # ======================================================

    st.markdown("---")

    st.markdown(
        """
        <div style="
            text-align:center;
            padding:15px;
            color:gray;
            font-size:16px;
        ">
        🚗 <b>EdgeGuard AI</b><br>
        Real-Time Vehicle Health Monitoring & Predictive Maintenance<br><br>
        developed by TECH ALLIANCE
        </div>
        """,
        unsafe_allow_html=True
    )
    
