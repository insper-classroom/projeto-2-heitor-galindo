from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/imoveis", methods=["GET"]) # Listar todos os imóveis
def listar_imoveis():
    return jsonify([])

@app.route("/imoveis/<int:id>", methods=["GET"]) # Listar imóvel por ID
def buscar_imovel_por_id(id):
    return jsonify({"id": id})