import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app


def test_homepage():

    tester = app.test_client()

    response = tester.get("/")

    assert response.status_code == 200


def test_menu_page():

    tester = app.test_client()

    response = tester.get("/menu")

    assert response.status_code == 200


def test_api_orders():

    tester = app.test_client()

    response = tester.get("/api/orders")

    assert response.status_code == 200