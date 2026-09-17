from fastapi import FastAPI
import os
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

app = FastAPI(
    title="Python DevSecOps Online Lab",
    version="1.0.0",
)


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self,
        request: Request,
        call_next,
    ) -> Response:
        response = await call_next(request)

        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Content-Security-Policy"] = "default-src 'self'"
        response.headers["Referrer-Policy"] = "no-referrer"

        return response


app.add_middleware(SecurityHeadersMiddleware)


@app.get("/")
def read_root() -> dict[str, str]:
    return {
        "message": "Python DevSecOps application is running",
    }


@app.get("/health")
def health_check() -> dict[str, str]:
    return {
        "status": "healthy",
    }


@app.get("/hello/{name}")
def say_hello(name: str) -> dict[str, str]:
    return {
        "message": f"Hello, {name}",
    }
