# fastapi
This project is part of the WAES Full Stack Developer Industry Standard Bootcamp. The goal is to create a backend using FastAPI.

## Guide to Building this REST API with FastAPI

### Table of Contents
1. [Prerequisites](#prerequisites)
2. [Project Setup](#project-setup)
3. [Running the FastAPI Server](#running-the-fastapi-server)
4. [Testing the API Endpoints](#testing-the-api-endpoints)
5. [Advanced Testing](#advanced-testing)
    - [Parameter Validation](#parameter-validation)
    - [Summation](#summation)
6. [Logging Verification](#logging-verification)
7. [Next Steps](#next-steps)


# 1. Prerequisites

    Before starting, ensure you have:

    - Python 3.7+ installed
    - pip (Python package manager)
    - A terminal (Bash, PowerShell, or Command Prompt)
    - (Optional) Postman or curl for API testing

# 2. Project Setup

    ## Step 1: Create a New Project Directory
        mkdir fastapi && cd fastapi
        mkdir backend && cd backend

    ## Step 2: Set Up a Virtual Environment (Recommended)
        python -m venv venv
        source venv/bin/activate  # Linux/Mac
        .\venv\Scripts\activate  # Windows

    ## Step 3: Install Required Packages
        pip install fastapi uvicorn

    ## Step 4: Create the FastAPI Application
        Create a file named main.py with the code provided in this project directory "/backend/main.py"

# 3. Running the FastAPI Server

    Start the server using Uvicorn:

        uvicorn main:app --reload

    The API will be available at:
        🔹 http://localhost:8000
        🔹 Interactive Docs (Swagger UI): http://localhost:8000/docs

# 4. Testing the API Endpoints

    ## Test 1: Root Endpoint

        curl http://localhost:8000/
        Expected Output: {"message": "FastAPI REST API"}

    ## Test 2: GET /item (Basic Test)

        curl "http://localhost:8000/item?a=3&b=4"
        Expected Output: {"sum": 7}

    ## Test 3: PUT /item (Basic Test)

        curl -X PUT -H "Content-Type: application/json" -d '{"name":"Premium Laptop","price":1299}' http://localhost:8000/item/1
        Expected Output: {"id":1,"name":"Premium Laptop","price":1299.0}

    ## Test 3: DELETE /item (Basic Test)

        curl -X DELETE http://localhost:8000/item/1
        Expected Output: {"message":"Item deleted"}

# 5. Advanced Testing (Parameter Validation & Summation)

    ## Test 3: Missing Parameters (Error Handling)

        curl "http://localhost:8000/item"
        Expected Output: {"detail": "No parameters provided"}

    ## Test 4: Invalid Parameters (Non-Integer Values)

        curl "http://localhost:8000/item?a=3&b=hello"
        Expected Output: {"detail": ["Parameter 'b' must be an integer"]}

# 6. Logging Verification

    Check api.log to confirm all requests are logged:

        cat api.log : or you can get the api.log in the directory : "/backend/api.log"

    Sample Log Output:

        2025-05-16 10:00:00 - INFO - {"method": "GET", "url": "http://localhost:8000/item?a=3&b=4", "status_code": 200, "process_time": 0.0005}
        2025-05-16 10:00:05 - INFO - {"method": "GET", "url": "http://localhost:8000/item?a=hello", "status_code": 400, "process_time": 0.0002}

# 7. Next Steps

- **Expand CRUD Operations**: Implement `POST`, `PUT`, and `DELETE` endpoints to handle full CRUD functionality for your API.

- **Add Database**: Integrate a database for persistent storage. 

- **Deploy**: Containerize the application using Docker and deploy it to a cloud platform such as AWS, or Heroku (Student Pack) for production use.




