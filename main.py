from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class MapFeature(BaseModel):
    type: str
    location: List[float]
    label: str

@app.get("/data", response_model=List[MapFeature])
def get_data():
    return [
        {"type": "liikennemerkki", "location": [60.221, 24.811], "label": "Pysäköintikielto"},
        {"type": "kuoppa", "location": [60.225, 24.815], "label": "Tien kunto - huono"},
        {"type": "työmaa", "location": [60.229, 24.820], "label": "Rakennustyömaa"}
    ]