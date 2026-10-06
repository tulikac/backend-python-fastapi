from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_serves_landing_page_and_deep_route():
    home = client.get("/")
    deep_route = client.get("/products/widget-1")

    assert home.status_code == 200
    assert "FastAPI backend is running" in home.text
    assert deep_route.status_code == 200
    assert "Widget 1" in deep_route.text


def test_reports_health_and_deployment_identity():
    health = client.get("/health").json()
    app_version = client.get("/api/version").json()

    assert health["status"] == "ok"
    assert health["app"] == "backend-python-fastapi"
    assert app_version["app"] == "backend-python-fastapi"
    assert app_version["framework"].startswith("FastAPI ")
    assert app_version["runtime"]


def test_returns_safe_request_metadata():
    response = client.get(
        "/api/request",
        headers={
            "user-agent": "builder-app-shape-test",
            "authorization": "Bearer must-not-be-returned",
        },
    )
    body = response.json()

    assert body["method"] == "GET"
    assert body["path"] == "/api/request"
    assert body["headers"]["userAgent"] == "builder-app-shape-test"
    assert "authorization" not in body["headers"]


def test_distinguishes_page_and_api_misses():
    page = client.get("/missing-page")
    api = client.get("/api/missing")

    assert page.status_code == 404
    assert "Page not found" in page.text
    assert api.status_code == 404
    assert api.json() == {
        "error": "not_found",
        "message": "The requested API route does not exist.",
    }
