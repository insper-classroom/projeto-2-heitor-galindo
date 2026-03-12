def test_buscar_imovel_por_id(client):
    response = client.get("/imoveis/1")

    assert response.status_code == 200
    assert response.is_json