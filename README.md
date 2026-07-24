# 🌍 Urban Air Quality Prediction System

An AI-powered web application that provides **real-time air quality monitoring** and **AQI prediction** using Machine Learning. The application helps users understand current pollution levels, weather conditions, and health recommendations through an interactive dashboard.

---

## 🚀 Live Demo

🔗 https://urbanairquallityindexaqi-4xh43c2ucdhjgktdfnniyn.streamlit.app/

---

## 📌 Features

- 🌍 Live Air Quality Index (AQI) Monitoring
- 📍 Search AQI by City Name
- 🌡 Real-time Weather Information
  - Temperature
  - Humidity
  - Wind Speed
  - Pressure
- 📊 Interactive AQI Gauge
- 📈 Pollutant Visualization
- 🤖 AQI Prediction using Machine Learning
- 💡 Health Recommendations based on AQI
- 📄 Download AQI Report as PDF
- 🎨 User-friendly Streamlit Interface

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Machine Learning
- Scikit-learn
- Random Forest Regressor

### Web Framework
- Streamlit

### Data Analysis
- Pandas
- NumPy

### Data Visualization
- Plotly

### API
- OpenWeather API

### Report Generation
- ReportLab

---

## 📂 Project Structure

```text
Urban-Air-Quality-Prediction/
│
├── app.py
├── Home.py
├── api.py
├── predict.py
├── utils.py
├── requirements.txt
├── runtime.txt
├── model.pkl
├── imputer.pkl
│
├── pages/
│   ├── Live_AQI.py
│   └── AQI_Prediction.py
│
├── dataset/
│   └── city_day.csv
│
├── assets/
│   └── logo.png
│
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/urban_air_quality_prediction.git
```

Navigate to the project folder

```bash
cd urban_air_quality_prediction
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install the required packages

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 🌐 Deployment

This project is deployed using **Streamlit Community Cloud**.

### Steps to Deploy

1. Push the project to GitHub.
2. Sign in to Streamlit Cloud.
3. Click **New App**.
4. Select your GitHub repository.
5. Choose the `main` branch.
6. Select `app.py` as the entry point.
7. Click **Deploy**.

---

## 🔑 API Configuration

This project uses the **OpenWeather API**.

Create a file:

```
.streamlit/secrets.toml
```

Add your API key:

```toml
API_KEY = "YOUR_API_KEY"
```

Or configure it directly from the **Streamlit Cloud Secrets** section.

---

## 📊 Machine Learning Model

Algorithm Used:

- Random Forest Regressor

Model Performance:

- ✅ R² Score: **0.91**
- ✅ Mean Absolute Error (MAE): **20.85**

---

## 📷 Application Modules

### 🌍 Live AQI

- Current AQI
- Weather Details
- Pollutant Levels
- AQI Gauge
- Health Recommendations
- PDF Report Download

### 🤖 AQI Prediction

- Predict AQI using pollutant values
- Interactive charts
- Health Recommendation
- PDF Report Generation

---

## 👩‍💻 Author

**Chandana V**

Final Year Computer Science Engineering Student

---

## 📄 License

This project is developed for educational and academic purposes.
