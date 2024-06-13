import requests

base_url = 'http://localhost:8000'

# Create configuration
create_payload = {
    "country_code": "IN",
    "business_name": "Example Business India",
    "registration_number": "12345",
    "additional_details": "Some details for India"
}
response = requests.post(f"{base_url}/create_configuration", json=create_payload)
print("Create Configuration Response:", response.json())

# Get configuration
response = requests.get(f"{base_url}/get_configuration/IN")
print("Get Configuration Response:", response.json())

# Update configuration
update_payload = {
    "country_code": "IN",
    "business_name": "Updated Business India",
    "registration_number": "54321",
    "additional_details": "Updated details for India"
}
response = requests.post(f"{base_url}/update_configuration", json=update_payload)
print("Update Configuration Response:", response.json())

# Delete configuration
delete_payload = {
    "country_code": "IN"
}
response = requests.delete(f"{base_url}/delete_configuration", json=delete_payload)
print("Delete Configuration Response:", response.json())
