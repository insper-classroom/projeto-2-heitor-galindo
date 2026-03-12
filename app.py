'''
ação	           código
GET sucesso	       200
POST criado	       201
DELETE sucesso	   204
não encontrado	   404
erro de validação  400
'''

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/imoveis", methods=["GET"])
def listar_imoveis():
    return jsonify([])