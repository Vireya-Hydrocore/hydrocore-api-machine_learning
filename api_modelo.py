from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import uvicorn
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


@app.post("/predict")
def predict(data: WaterData):
    input_data = pd.DataFrame([data.dict()])
    model = pickle.load(open("model.pkl", "rb"))
    prediction = model.predict(input_data)
    return {"Potability": int(prediction)}

if __name__ == "__main__":
    uvicorn.run("api_modelo:app", host="0.0.0.0", port=8000, reload=True)
