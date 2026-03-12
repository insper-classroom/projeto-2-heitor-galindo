def test_listar_imoveis_por_cidade(client):
    response = client.get("/imoveis/cidade/São Paulo")

    assert response.status_code == 200
    assert response.is_json