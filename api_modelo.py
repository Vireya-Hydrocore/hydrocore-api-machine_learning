from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import pickle

class WaterData(BaseModel):
    ph: float
    Hardness: float
    Solids: float
    Chloramines: float
    Sulfate: float
    Conductivity: float
    Organic_carbon: float
    Trihalomethanes: float
    Turbidity: float

app = FastAPI(title="API de Previsão de Potabilidade da Água")


with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.post("/predict")
def predict(data: WaterData):
    input_data = pd.DataFrame([data.dict()])
    prediction = model.predict(input_data)
    return {"Potability": int(prediction[0])}
