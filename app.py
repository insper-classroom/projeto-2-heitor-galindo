from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/imoveis", methods=["GET"]) # Listar todos os imóveis
def listar_imoveis():
    return jsonify([])

@app.route("/imoveis/<int:id>", methods=["GET"]) # Listar imóvel por ID
def buscar_imovel_por_id(id):
    return jsonify({"id": id})

@app.route("/imoveis", methods=["POST"]) # Criar um novo imóvel
def criar_imovel():
    data = request.json
    return jsonify(data), 201