from fastapi.testclient import TestClient  # pyright: ignore[reportMissingImports]

from sample_api.main import app

client = TestClient(app)


def test_root() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Python DevSecOps application is running",
    }


def test_health() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
    }


def test_hello() -> None:
    response = client.get("/hello/Vigneshwar")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello, Vigneshwar",
    }


def test_security_headers() -> None:
    response = client.get("/")

    assert response.headers["X-Content-Type-Options"] == "nosniff"
    assert response.headers["X-Frame-Options"] == "DENY"
