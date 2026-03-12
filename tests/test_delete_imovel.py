def test_remover_imovel(client):
    response = client.delete("/imoveis/1")

    assert response.status_code == 204