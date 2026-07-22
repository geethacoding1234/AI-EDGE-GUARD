import streamlit as st


# -----------------------------------
# Page Configuration
# -----------------------------------

st.set_page_config(
    page_title="EdgeGuard AI",
    page_icon="🚗",
    layout="wide"
)


# -----------------------------------
# Professional CSS
# -----------------------------------

st.markdown("""
<style>

/* Main Background */

.stApp {
    background-color: #ffffff;
}


/* All Text */

html, body, [class*="css"] {

    color: #000000;

    font-family:
    "Segoe UI",
    Arial,
    sans-serif;

}


/* Main Title */

.main-title {

    font-size:45px;
    font-weight:700;
    color:#0B3D91;
    text-align:center;

}


/* Subtitle */

.sub-title {

    font-size:22px;
    color:#333333;
    text-align:center;

}


/* Cards */

.card {

    background:white;

    padding:25px;

    border-radius:15px;

    border:1px solid #d9e2f3;

    box-shadow:
    0px 4px 12px rgba(0,0,0,0.08);

    height:180px;

}


.card-title {

    font-size:22px;

    font-weight:600;

    color:#0B3D91;

}


.card-text {

    font-size:16px;

    color:#333333;

}


/* Section Headers */

h1,h2,h3 {

    color:#0B3D91 !important;

}


/* Table */

[data-testid="stTable"] {

    color:black;

}


</style>

""",
unsafe_allow_html=True)



# -----------------------------------
# Header
# -----------------------------------

st.markdown(
"""
<div class="main-title">

🚗 EdgeGuard AI

</div>

<div class="sub-title">

Real-Time Vehicle Health Monitoring
& Predictive Maintenance System

</div>

""",
unsafe_allow_html=True
)



st.write("")

st.markdown("---")



# -----------------------------------
# Project Overview
# -----------------------------------

st.header("📌 Project Overview")


st.write(
"""
EdgeGuard AI is an Artificial Intelligence based
vehicle health monitoring platform designed to
predict vehicle condition using machine learning.

The system analyzes vehicle sensor parameters and
provides:

• Vehicle Health Score

• Fault Prediction

• Maintenance Recommendations

• Sensor Monitoring

• Automated Reports
"""
)



# -----------------------------------
# Features
# -----------------------------------

st.header("🚀 Core Features")


col1,col2,col3 = st.columns(3)


with col1:

    st.markdown(
    """
    <div class="card">

    <div class="card-title">
    🤖 AI Prediction
    </div>

    <br>

    <div class="card-text">

    Machine learning based
    vehicle health prediction
    using XGBoost models.

    </div>

    </div>

    """,
    unsafe_allow_html=True
    )



with col2:

    st.markdown(
    """
    <div class="card">

    <div class="card-title">
    📊 Sensor Monitoring
    </div>

    <br>

    <div class="card-text">

    Real-time monitoring of
    engine temperature, RPM,
    battery and vehicle sensors.

    </div>

    </div>

    """,
    unsafe_allow_html=True
    )



with col3:

    st.markdown(
    """
    <div class="card">

    <div class="card-title">
    🛠 Predictive Maintenance
    </div>

    <br>

    <div class="card-text">

    Early fault detection and
    intelligent maintenance
    recommendations.

    </div>

    </div>

    """,
    unsafe_allow_html=True
    )



st.write("")



# -----------------------------------
# Technology Stack
# -----------------------------------

st.header("⚙ Technology Stack")


technology = pd.DataFrame({

"Technology":[
"Python",
"Streamlit",
"XGBoost",
"Pandas",
"Plotly",
"Machine Learning"
],

"Purpose":[
"Programming Language",
"Web Dashboard",
"Prediction Model",
"Data Processing",
"Visualization",
"AI Analysis"
]

})


st.table(technology)



# -----------------------------------
# System Architecture
# -----------------------------------

st.header("🏗 System Architecture")


st.info(
"""
Vehicle Sensor Data

↓

Data Processing

↓

Machine Learning Model

↓

Health Score Prediction

↓

Maintenance Recommendation

↓

Dashboard & Reports
"""
)



# -----------------------------------
# Footer
# -----------------------------------

st.markdown("---")


st.caption(
"""
EdgeGuard AI |
AI Based Vehicle Health Monitoring and Predictive Maintenance System
"""
)
