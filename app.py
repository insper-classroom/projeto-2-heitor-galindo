from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/imoveis", methods=["GET"]) # Listar todos os imóveis, 200
def listar_imoveis():
    return jsonify([])

@app.route("/imoveis/<int:id>", methods=["GET"]) # Listar imóvel por ID, 200
def buscar_imovel_por_id(id):
    return jsonify({"id": id})

@app.route("/imoveis", methods=["POST"]) # Criar um novo imóvel, 201
def criar_imovel():
    data = request.json
    return jsonify(data), 201

@app.route("/imoveis/<int:id>", methods=["PUT"]) # Atualizar um imóvel existente, 200
def atualizar_imovel(id):
    data = request.json
    return jsonify({"id": id, **data})

@app.route("/imoveis/<int:id>", methods=["DELETE"]) # Remover um imóvel, 204
def remover_imovel(id):
    return "", 204

