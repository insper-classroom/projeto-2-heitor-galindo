def test_criar_imovel(client):
    novo_imovel = {
        "logradouro": "Rua A",
        "tipo_logradouro": "Rua",
        "bairro": "Centro",
        "cidade": "São Paulo",
        "cep": "00000-000",
        "tipo": "casa",
        "valor": 500000
    }

    response = client.post("/imoveis", json=novo_imovel)

    assert response.status_code == 201
    assert response.is_json