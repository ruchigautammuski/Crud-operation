from typing import Dict
from pydantic import BaseModel

class Configuration(BaseModel):
    country_code: str
    business_name: str
    registration_number: str
    additional_details: str

configurations_db: Dict[str, Configuration] = {}

def create_configuration(config: Configuration):
    configurations_db[config.country_code] = config
    return config

def get_configuration(country_code: str):
    return configurations_db.get(country_code)

def update_configuration(config: Configuration):
    if config.country_code in configurations_db:
        configurations_db[config.country_code] = config
        return config
    else:
        return None

def delete_configuration(country_code: str):
    if country_code in configurations_db:
        del configurations_db[country_code]
        return True
    else:
        return False
