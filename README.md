# Calculator Final Project

## Overview

This project is a full-stack calculator application built with FastAPI. Users can register, log in, create calculations, view saved calculation history, edit existing calculations, and delete calculations. Calculation records are stored in PostgreSQL and scoped to the authenticated user.

The app demonstrates a complete BREAD workflow: Browse, Read, Edit, Add, and Delete.

## Features

- User registration and login
- JWT-based authentication
- Authenticated calculation history
- Create, view, edit, and delete calculations
- Server-side validation with Pydantic
- Client-side validation in JavaScript
- PostgreSQL persistence with SQLAlchemy
- Docker Compose setup for the app, database, and pgAdmin
- Unit, integration, API, and Playwright E2E tests

## Supported Operations

- Addition
- Subtraction
- Multiplication
- Division
- Power / exponentiation
- Modulus

Division by zero and modulus by zero are rejected by validation.

## Tech Stack

- FastAPI
- SQLAlchemy
- Pydantic
- PostgreSQL
- Jinja templates
- JavaScript
- Docker / Docker Compose
- Pytest
- Playwright

## Run With Docker

Start the application and database:

```bash
docker compose up --build
```

The FastAPI app runs with Uvicorn inside the container:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Application URLs

- Frontend login: <http://localhost:8000/login>
- Frontend registration: <http://localhost:8000/register>
- Dashboard: <http://localhost:8000/dashboard>
- Swagger UI: <http://localhost:8000/docs>
- pgAdmin: <http://localhost:5050>

## Database Connection

Docker database settings:

- Host: `db`
- Username: `postgres`
- Password: `postgres`
- Database: `fastapi_db`

Local test/development settings commonly use:

- Host: `localhost`
- Port: `5432`
- Username: `postgres`
- Password: `postgres`
- Database: `fastapi_db`

## Authentication

Users register with:

- first name
- last name
- email
- username
- password
- confirm password

Passwords are hashed with bcrypt. After login, the frontend stores the JWT access token in `localStorage` and sends it in the `Authorization` header for protected calculation routes.

## API Endpoints

All `/calculations` endpoints require authentication.

### Create Calculation

`POST /calculations`

```json
{
  "type": "power",
  "a": 2,
  "b": 3
}
```

Example result:

```json
{
  "type": "power",
  "a": 2,
  "b": 3,
  "result": 8
}
```

### Browse Calculations

`GET /calculations`

Returns all calculations for the authenticated user.

### Read Calculation

`GET /calculations/{calculation_id}`

Returns one calculation if it belongs to the authenticated user.

### Update Calculation

`PUT /calculations/{calculation_id}`

Updates the operation type, inputs, and recalculated result.

### Delete Calculation

`DELETE /calculations/{calculation_id}`

Deletes one calculation if it belongs to the authenticated user.

## Testing

Create and activate a local virtual environment if needed:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

Run unit tests:

```bash
python -m pytest tests/unit
```

Run integration tests:

```bash
python -m pytest tests/integration
```

Run Playwright E2E tests:

```bash
python -m pytest tests/e2e -m e2e
```

Run the full test suite:

```bash
python -m pytest
```

The integration and E2E tests require the configured PostgreSQL database to be available.

## Test Coverage Areas

- Calculator operation functions
- SQLAlchemy calculation model behavior
- Pydantic schema validation
- Authenticated calculation API routes
- Positive calculation workflows
- Negative validation scenarios
- Frontend BREAD workflow through Playwright
- Unauthorized dashboard redirect behavior

## Alembic / Migration Note

No Alembic migration was required for adding power and modulus.

The existing `calculations.type` column is already a string column, so it can store new operation names such as `power` and `modulus`. The existing `a`, `b`, and `result` columns already store numeric values. This feature changed application behavior, not the database schema.

## Docker Hub

Docker Hub repository:

<https://hub.docker.com/repository/docker/bry633/calculator-final-project>
