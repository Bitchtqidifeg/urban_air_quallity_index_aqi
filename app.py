# ==========================================================
# Urban Air Quality Prediction System
# ==========================================================

import streamlit as st
from PIL import Image
import plotly.graph_objects as go
import pandas as pd

from api import get_coordinates, get_weather, get_air_quality
from utils import get_aqi_status
from predict import predict_aqi

# ----------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------

st.set_page_config(
    page_title="Urban Air Quality Prediction System",
    page_icon="🌍",
    layout="wide"
)

# Load Google font and small layout CSS
st.markdown(
        """
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap" rel="stylesheet">
        <style>
            html, body, [class*="css"]  { font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial; }
            .block-container { max-width: 1100px; margin: 24px auto; }
            .hero-card { margin-bottom: 18px; }
        </style>
        """,
        unsafe_allow_html=True,
)

# ----------------------------------------------------------
# SESSION STATE
# ----------------------------------------------------------

if "predicted" not in st.session_state:
    st.session_state.predicted = None

# ----------------------------------------------------------
# CSS
# ----------------------------------------------------------

try:
    with open("styles/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )
except:
    pass

# ---------------- Theme Selector (Bright / Vivid / Dark) ----------------
theme_choice = st.sidebar.selectbox("Theme", ["Bright", "Vivid", "Dark"], index=0)

if theme_choice == "Dark":
    dark_css = """
    <style>
    :root { --bg-dark: #0b1020; --panel: rgba(18,24,40,0.75); --muted: #9aa6bf; --accent: #6b8eff; }
    html, body, .stApp, .reportview-container, .main { background: linear-gradient(180deg,#05060a 0%, #0b1020 100%) !important; color: #e6eef8 !important; }
    .block-container, .card { background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01)) !important; box-shadow: 0 12px 40px rgba(0,0,0,0.6) !important; }
    .hero-card { background: linear-gradient(135deg, rgba(55,65,120,0.95), rgba(40,45,80,0.95)) !important; }
    .stButton > button, .stDownloadButton > button { box-shadow: 0 18px 40px rgba(0,0,0,0.6) !important; }
    .stTextInput input, .stNumberInput input { background: rgba(255,255,255,0.03) !important; color: #e6eef8 !important; border: 1px solid rgba(255,255,255,0.06) !important; }
    [data-testid="stMetric"] { background: linear-gradient(180deg, rgba(255,255,255,0.03), rgba(255,255,255,0.01)) !important; }
    </style>
    """
    st.markdown(dark_css, unsafe_allow_html=True)

elif theme_choice == "Vivid":
    vivid_css = """
    <style>
    :root { --accent-1: #ff4d6d; --accent-2: #ffd24a; --accent-3: #45e6b8; --accent-4: #4f9bff; }
    html, body, .stApp, .reportview-container, .main { background: radial-gradient(circle at 10% 10%, #fff4f8 0%, transparent 20%), radial-gradient(circle at 90% 80%, #f0fbff 0%, transparent 20%), linear-gradient(90deg,#fff7f0 0%,#f6f0ff 100%) !important; }
    .block-container, .card { background: linear-gradient(180deg, rgba(255,255,255,0.92), rgba(255,255,255,0.88)) !important; }
    .hero-card { background: linear-gradient(135deg, #4f9bff 0%, #d29bff 45%, #ff4d6d 100%) !important; }
    .stButton > button { background: linear-gradient(90deg, #4f9bff, #d29bff) !important; }
    .stDownloadButton > button { background: linear-gradient(90deg, #45e6b8, #ffd24a) !important; color: #072634 !important; }
    </style>
    """
    st.markdown(vivid_css, unsafe_allow_html=True)

# Bright uses the default `styles/style.css` already loaded

# ----------------------------------------------------------
# LOGO
# ----------------------------------------------------------

try:
    logo = Image.open("assets/logo.png")
    st.image(logo, width=90)
except:
    pass

# ----------------------------------------------------------
# TITLE
# ----------------------------------------------------------

st.title("🌍 Urban Air Quality Prediction System")

st.caption(
    "Real-Time Air Quality Monitoring & Machine Learning Prediction"
)

st.markdown(
    """
    <div class="hero-card">
        <div class="hero-title">Air Quality Intelligence Dashboard</div>
        <div class="hero-subtitle">Monitor live AQI data and predict future air quality with a clean, modern interface.</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ==========================================================
# LIVE AQI & PREDICTION TABS
# ==========================================================

live_tab, prediction_tab = st.tabs(["🌍 Live AQI", "🤖 AQI Prediction"])

with live_tab:

    st.header("🌍 Live Air Quality")

    # Try to load city names from dataset if available
    city_options = []
    try:
        import pandas as _pd
        df_cities = _pd.read_csv("dataset/city_day.xls")
        if "City" in df_cities.columns:
            city_options = sorted(df_cities["City"].dropna().unique().tolist())
    except Exception:
        city_options = []

    # Fallback list if dataset has no City column
    if not city_options:
        city_options = [
            "Bengaluru",
            "Delhi",
            "Mumbai",
            "Chennai",
            "Kolkata",
            "Hyderabad",
            "Pune",
            "Ahmedabad",
            "Lucknow",
            "Jaipur",
        ]

    city_selection = st.selectbox("Select City (or choose Other)", options=city_options + ["Other"], index=0)

    if city_selection == "Other":
        city = st.text_input("Enter City Name", placeholder="Type a city name, e.g., Bangalore")
    else:
        city = city_selection

    weather = None
    air = None
    status = ""
    advice = ""

    if st.button("🔍 Get Live AQI", use_container_width=True):

        coordinates = get_coordinates(city)

        if coordinates:

            lat, lon = coordinates

            weather = get_weather(lat, lon)

            air = get_air_quality(lat, lon)

            status, advice = get_aqi_status(air["aqi"])

            st.success(f"Showing Live AQI for {city.title()}")

            st.divider()

            c1, c2, c3 = st.columns(3)

            c1.metric("AQI", air["aqi"])
            c2.metric("PM2.5", air["pm2_5"])
            c3.metric("PM10", air["pm10"])

            c4, c5, c6 = st.columns(3)

            c4.metric("CO", air["co"])
            c5.metric("NO₂", air["no2"])
            c6.metric("SO₂", air["so2"])

            st.metric("O₃", air["o3"])

            st.divider()

            st.subheader("AQI Status")

            st.success(status)

            st.info(advice)

            fig = go.Figure(go.Indicator(

                mode="gauge+number",

                value=air["aqi"],

                title={"text": "Live AQI Category"},

                gauge={

                    "axis": {"range": [1, 5]},

                    "bar": {"color": "darkblue"},

                    "steps": [

                        {"range": [1, 2], "color": "green"},

                        {"range": [2, 3], "color": "yellow"},

                        {"range": [3, 4], "color": "orange"},

                        {"range": [4, 5], "color": "red"}

                    ]

                }

            ))

            st.plotly_chart(fig, use_container_width=True)

        else:

            st.error("City not found.")

    if air is not None:

        st.divider()

        live_report = pd.DataFrame({
            "City": [city.strip().title() if city.strip() else "Unknown City"],
            "Live AQI": [air["aqi"]],
            "PM2.5": [air["pm2_5"]],
            "PM10": [air["pm10"]],
            "CO": [air["co"]],
            "NO2": [air["no2"]],
            "SO2": [air["so2"]],
            "O3": [air["o3"]],
            "Status": [status]
        })

        csv = live_report.to_csv(index=False).encode("utf-8")

        st.download_button(
            "📄 Download Live AQI Report",
            data=csv,
            file_name=f"{city.strip().title() if city.strip() else 'unknown_city'}_Live_AQI_Report.csv",
            mime="text/csv",
            use_container_width=True
        )

with prediction_tab:

    st.header("🤖 Machine Learning AQI Prediction")

    st.write("Enter pollutant values to predict the AQI.")

    col1, col2, col3 = st.columns(3)

    with col1:
        pm25 = st.number_input("PM2.5", min_value=0.0)
        pm10 = st.number_input("PM10", min_value=0.0)
        no = st.number_input("NO", min_value=0.0)
        no2 = st.number_input("NO₂", min_value=0.0)

    with col2:
        nox = st.number_input("NOx", min_value=0.0)
        nh3 = st.number_input("NH₃", min_value=0.0)
        co = st.number_input("CO", min_value=0.0)
        so2 = st.number_input("SO₂", min_value=0.0)

    with col3:
        o3 = st.number_input("O₃", min_value=0.0)
        benzene = st.number_input("Benzene", min_value=0.0)
        toluene = st.number_input("Toluene", min_value=0.0)
        xylene = st.number_input("Xylene", min_value=0.0)

    st.divider()

    if st.button("🚀 Predict AQI", use_container_width=True):

        st.session_state.predicted = predict_aqi(
            pm25,
            pm10,
            no,
            no2,
            nox,
            nh3,
            co,
            so2,
            o3,
            benzene,
            toluene,
            xylene
        )

        predicted = st.session_state.predicted

        st.success("Prediction Completed Successfully!")

        st.metric(
            "🌍 Predicted AQI",
            round(predicted, 2)
        )

        fig = go.Figure(go.Indicator(

            mode="gauge+number",

            value=predicted,

            title={"text": "Predicted AQI"},

            gauge={

                "axis": {"range": [0, 500]},

                "bar": {"color": "darkblue"},

                "steps": [

                    {"range": [0, 50], "color": "green"},
                    {"range": [50, 100], "color": "yellow"},
                    {"range": [100, 200], "color": "orange"},
                    {"range": [200, 300], "color": "red"},
                    {"range": [300, 400], "color": "purple"},
                    {"range": [400, 500], "color": "maroon"}

                ]

            }

        ))

        st.plotly_chart(fig, use_container_width=True)

        if predicted <= 50:
            category = "🟢 Good"
            advice_ml = "Air quality is good. Enjoy outdoor activities."

        elif predicted <= 100:
            category = "🟡 Satisfactory"
            advice_ml = "Air quality is acceptable."

        elif predicted <= 200:
            category = "🟠 Moderate"
            advice_ml = "Sensitive groups should reduce prolonged outdoor activities."

        elif predicted <= 300:
            category = "🔴 Poor"
            advice_ml = "Avoid prolonged outdoor activities."

        elif predicted <= 400:
            category = "🟣 Very Poor"
            advice_ml = "Stay indoors if possible."

        else:
            category = "⚫ Severe"
            advice_ml = "Avoid outdoor exposure. Wear a mask if you must go outside."

        st.divider()

        col1, col2 = st.columns(2)

        with col1:
            st.metric("AQI Category", category)

        with col2:
            st.info(advice_ml)

    if st.session_state.predicted is not None:

        st.divider()

        prediction_report = pd.DataFrame({
            "Input PM2.5": [pm25],
            "Input PM10": [pm10],
            "Input NO": [no],
            "Input NO2": [no2],
            "Input NOx": [nox],
            "Input NH3": [nh3],
            "Input CO": [co],
            "Input SO2": [so2],
            "Input O3": [o3],
            "Input Benzene": [benzene],
            "Input Toluene": [toluene],
            "Input Xylene": [xylene],
            "Predicted AQI": [round(st.session_state.predicted, 2)]
        })

        csv = prediction_report.to_csv(index=False).encode("utf-8")

        st.download_button(
            "📄 Download Prediction Report",
            data=csv,
            file_name="prediction_report.csv",
            mime="text/csv",
            use_container_width=True
        )

st.divider()

st.caption("© 2026 Urban Air Quality Prediction System | AI & ML Project")