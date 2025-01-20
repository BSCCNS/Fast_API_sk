# Fast_API_sk
**Generic skeleton for API using FastAPI.**

## Instructions

1. Clone the repository.
2. Create a virtual environment with `python -m venv venv`.
3. Enter into the backend folder `cd backend`
4. Install the requirements with `pip install -r requirements.txt`.
5. Run the server with uvicorn `uvicorn main:app`. Add the flag `--reload` for automatic reloading when testing.


## Overview

```bash
├── backend/
│   ├── auth/
│   │   ├── auth.py
│   │   ├── hashing.py
│   ├── core/
│   │   ├── config.py
│   │   ├── endpoints.py 
│   │   ├── routers.py    
│   ├── data/
│   │   ├── db_methods.py
│   │   ├── fake_db.py
│   │   ├── users_db_fake.json
│   ├── schemas/
│   │   ├── token_schema.py
│   │   ├── user_schema.py
│   ├── user/
│   │   ├── user_endpoints.py
├── main.py
├── requirements.txt
├── README.md
```

The API is modular. Basic configuration is in the core folder (settings and a file collecting all the router points). Different functionalities are implemented in their corresponding folder. Each one through a router object. The `main.py`file calls the application and connects the routers.


## Folder description

`auth`: Contains functions for user authentication using an Ouath2 scheme. It implements password hashing and identification throug a JWT token.

`core`: Contains core functions for the API. In particular, it routes together all routers in the different code pieces. It also provides a configuration file with the API settings, and an example of a get endpoint.

`data`: Contains external data for the API. In this barebones version, it only contains a fake database file implemented through a dictionary.

`schemas`: Contains pydantic schemas for the different variables used.

`user`: Contains methods related to user creation and deletion.


## Authenticating

Users must authenticate in order to get a token that allows them to perform calls to the endpoints. This is achieved through a Ouath2 scheme in `/token`. Afterwards, every call must provide the bearer token.

Endpoints must check authenticity of the token through a dependence. See example:

```python
from typing import Annotated
from fastapi import Depends
from auth.auth import check_token

@router.get("/")
def get_endpoint(token: Annotated[str, Depends(check_token)]):
    ...
```