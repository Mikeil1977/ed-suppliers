from fastapi import FastAPI, HTTPException
import yaml
from pathlib import Path

app = FastAPI()
REQUIREMENTS_PATH = Path("data/initial_station_requirements.yaml")

with REQUIREMENTS_PATH.open() as f:
    requirements = yaml.safe_load(f)

@app.get("/station-types")
def get_station_types():
    return list(requirements.keys())

@app.get("/requirements")
def get_requirements(type: str):
    if type not in requirements:
        raise HTTPException(status_code=404, detail="Station type not found")
    return requirements[type]
