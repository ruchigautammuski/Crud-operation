
from fastapi import FastAPI, HTTPException
from config import configurations

app = FastAPI()

@app.post("/create_configuration", response_model=configurations.Configuration)
def create_configuration(config: configurations.Configuration):
    return configurations.create_configuration(config)

@app.get("/get_configuration/{country_code}", response_model=configurations.Configuration)
def get_configuration(country_code: str):
    config = configurations.get_configuration(country_code)
    if config is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return config

@app.post("/update_configuration", response_model=configurations.Configuration)
def update_configuration(config: configurations.Configuration):
    updated_config = configurations.update_configuration(config)
    if updated_config is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return updated_config

@app.delete("/delete_configuration", response_model=bool)
def delete_configuration(country_code: str):
    deleted = configurations.delete_configuration(country_code)
    if not deleted:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return True
