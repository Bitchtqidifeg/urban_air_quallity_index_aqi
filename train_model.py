import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.metrics import r2_score, mean_absolute_error
import joblib

# ---------------- Load Dataset ----------------
df = pd.read_csv("dataset/city_day.xls")

# ---------------- Select Features ----------------
features = [
    "PM2.5",
    "PM10",
    "NO",
    "NO2",
    "NOx",
    "NH3",
    "CO",
    "SO2",
    "O3",
    "Benzene",
    "Toluene",
    "Xylene"
]
target = "AQI"

# Keep only required columns
df = df[features + [target]]

# Remove rows where AQI is missing
df = df.dropna(subset=[target])

# Fill missing feature values
imputer = SimpleImputer(strategy="mean")

X = imputer.fit_transform(df[features])

y = df[target]

# ---------------- Train Test Split ----------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ---------------- Train Model ----------------
model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# ---------------- Evaluate ----------------
predictions = model.predict(X_test)

print("R2 Score :", r2_score(y_test, predictions))
print("MAE      :", mean_absolute_error(y_test, predictions))

# ---------------- Save Model ----------------
joblib.dump(model, "model.pkl")
joblib.dump(imputer, "imputer.pkl")

print("Model saved successfully!")