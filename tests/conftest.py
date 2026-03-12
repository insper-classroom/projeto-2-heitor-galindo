import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
        
'''
ação	           código
GET sucesso	       200
POST criado	       201
DELETE sucesso	   204
não encontrado	   404
erro de validação  400
'''
