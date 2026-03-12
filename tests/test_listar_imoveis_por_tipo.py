def test_listar_imoveis_por_tipo(client):
    response = client.get("/imoveis/tipo/casa")

    assert response.status_code == 200
    assert response.is_json