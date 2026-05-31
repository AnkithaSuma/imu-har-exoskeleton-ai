from pathlib import Path
import joblib

# --------------------------------------------------
# Activity Labels
# --------------------------------------------------

activity_map = {
    0: "WALKING",
    1: "WALKING_UPSTAIRS",
    2: "WALKING_DOWNSTAIRS",
    3: "SITTING",
    4: "STANDING",
    5: "LAYING"
}

# --------------------------------------------------
# Load Model
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

MODEL_PATH = PROJECT_ROOT / "models" / "xgboost.pkl"

xgb_model = joblib.load(MODEL_PATH)

print("XGBoost model loaded successfully.")

# --------------------------------------------------
# Prediction Function
# --------------------------------------------------

def predict_activity(sample):

    prediction = xgb_model.predict(sample)[0]

    return activity_map[prediction]


print("Realtime simulation module ready.")