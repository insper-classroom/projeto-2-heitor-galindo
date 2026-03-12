def test_listar_imoveis(client):
    response = client.get("/imoveis")

    assert response.status_code == 200
    assert response.is_json