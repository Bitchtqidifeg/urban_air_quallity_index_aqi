import joblib
import numpy as np

model = joblib.load("model.pkl")
imputer = joblib.load("imputer.pkl")

def predict_aqi(
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
):

    data = np.array([[

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

    ]])

    data = imputer.transform(data)

    prediction = model.predict(data)

    return prediction[0]