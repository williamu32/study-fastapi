import os
DATABASE_URL = 'sqlite:///testedb.sqlite'
os.environ['DATABASE_URL'] = DATABASE_URL
os.environ['TEST_DATABASE'] = 'true'

from types import GeneratorType
from fastapi.testclient import TestClient
import pytest
from study_fastapi.main import app
from study_fastapi.criar_tabelas import configurar_banco

@pytest.fixture(scope='function')
def client() -> GeneratorType:
    configurar_banco(DATABASE_URL)
    with TestClient(app) as c:
        yield c