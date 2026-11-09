import pytest
from faker import Faker
from fastapi.testclient import TestClient
from src.main import app

fake = Faker("pt_BR")

@pytest.fixture
def client():
    """Setup do TestClient"""
    with TestClient(app) as c:
        yield c

@pytest.fixture
def workstation_factory():
    """Factory de massa de dados sintética"""
    def _create_workstation():
        return {
            "hostname": f"PC-{fake.lexify(text='??????').upper()}",
            "os_version": fake.random_element(elements=("Win11_Pro_23H2", "Ubuntu_24_04_LTS"))
        }
    return _create_workstation