# Configuration Management API

This API manages configuration requirements for different countries.

### Running the FastAPI Application

Ensure your FastAPI application is running using `uvicorn`:

```bash
uvicorn main:app --reload


API Endpoints
1. Create Configuration (POST /create_configuration)
Create a configuration for a country.


curl -X 'POST' \
  'http://localhost:8000/create_configuration' \
  -H 'Content-Type: application/json' \
  -d '{
  "country_code": "IN",
  "business_name": "Example Business India",
  "registration_number": "12345",
  "additional_details": "Some details for India"
}'

2. Get Configuration (GET /get_configuration/{country_code})
Retrieve the configuration for a specific country.

curl -X 'GET' \
  'http://localhost:8000/get_configuration/IN'


3. Update Configuration (POST /update_configuration)
Update the configuration for a country.

curl -X 'POST' \
  'http://localhost:8000/update_configuration' \
  -H 'Content-Type: application/json' \
  -d '{
  "country_code": "IN",
  "business_name": "Updated Business India",
  "registration_number": "54321",
  "additional_details": "Updated details for India"
}'

4. Delete Configuration (DELETE /delete_configuration)
Delete the configuration for a country.

curl -X 'DELETE' \
  'http://localhost:8000/delete_configuration' \
  -H 'Content-Type: application/json' \
  -d '{
  "country_code": "IN"
}'
