def test_atualizar_imovel(client):
    imovel_atualizado = {"valor": 300000}

    response = client.put("/imoveis/1", json=imovel_atualizado)

    assert response.status_code == 200
    assert response.is_json