# routers.py

from fastapi import APIRouter, Security
from {{cookiecutter.project_slug}}.auth import auth
from {{cookiecutter.project_slug}}.core import endpoints
from {{cookiecutter.project_slug}}.user import superuser_endpoints
from {{cookiecutter.project_slug}}.auth.auth import check_superuser

# We define a router that collects everything together
api_router = APIRouter()
api_router.include_router(auth.router, prefix="")  # Security
api_router.include_router(endpoints.router, prefix="")  # Generic endpoint
api_router.include_router(
    superuser_endpoints.router,
    prefix="/superuser",
    dependencies=[Security(check_superuser, scopes=["superuser"])],
)  # User management endpoints
