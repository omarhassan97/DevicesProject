from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from typing import Dict, List
import device_store
import prediction
import uvicorn

app = FastAPI(debug=True)

@app.get("/api/devices", response_model=List[Dict])
def get_all_devices():
    return device_store.load_devices()

@app.get("/api/devices/{id}", response_model=Dict)
def get_device_by_id(id: int):
    device = device_store.get_device_by_id(id)
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    return device

@app.post("/api/devices", response_model=Dict)
def create_device(device: Dict):
    # Generate a new ID
    devices = device_store.load_devices()
    device_id = max([d.get("id", 0) for d in devices], default=0) + 1
    device["id"] = device_id
    device_store.add_device(device)
    return device



@app.get("/api/predict/{device_id}")
def predict_and_update_price(device_id: int):
    device = device_store.get_device_by_id(device_id)
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")

    predicted_price = prediction.predict_price(device)
    return predicted_price


@app.get("/", response_class=HTMLResponse)
def read_root():
    return "Device managment system:  use http://127.0.0.1:8000/docs for better view of endpoints" 

if __name__ == '__main':
    uvicorn.run(app)

