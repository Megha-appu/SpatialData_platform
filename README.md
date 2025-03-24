# Spatial Data Platform API


## Overview
This project provides a backend API for managing and handling spatial data, specifically for storing, updating, and retrieving spatial data related to multiple points and polygons. The API supports two main functionalities:

1. **Storing, updating, and retrieving multiple point data** - Each point represents a location (e.g., city locations) with detailed information.
2. **Storing, updating, and retrieving multiple polygon data** - These polygons can represent regions with specific attributes (e.g., population density in a region).

## Technologies Used

- **Django 5.1.7**
- **Django Rest Framework (DRF)**
- **Django REST Framework GIS (drf-gis)**
- **PostGIS (spatial extension for PostgreSQL)**

## Requirements

1. Python 3.8+
2. PostgreSQL with PostGIS extension enabled.
3. Django 5.1.7+
4. Django REST Framework
5. Django REST Framework GIS

## Setting Up the Project

### Step 1: Set up a Virtual Environment

Create and activate a virtual environment:

```bash
python -m venv env
source env/bin/activate  # On Windows: .\env\Scripts\activate

### Step 2: install dependencies from requirements.txt

```bash
 pip install -r requirements.txt

### Step 3: setup postgresql database and give postgis extension
CREATE EXTENSION postgis;

### Step 4: configure django settings and .env file
create .env file and configure database details inside it
### Step 5: Run the migrations to create the required tables in the database:

python manage.py makemigrations
python manage.py migrate

### Step 6: Now, you can run the Django development server:

python manage.py runserver

The server should be running at http://127.0.0.1:8000/.

### API ENDPOINTS

# 1.Create a City Location (Point Data)

Endpoint: POST /api/location/

# 2.Update a City Location (Point Data)

Endpoint: PUT /api/location/{id}/

# 3.Get All City Locations (Point Data)

Endpoint: GET /api/location/

# 1. Delete a City Location (Point Data)

Endpoint: DELETE /api/location/{id}/

# 1.Create Population Density Area (Polygon Data)

Endpoint: POST /api/density/

# 2.Update Population Density Area (Polygon Data)

Endpoint: PUT /api/density/{id}/

# 3.Get Population Density Area (Polygon Data)

Endpoint: GET /api/density/

# 4.Delete Population Density Area (Polygon Data)

Endpoint: DELETE /api/density/{id}/