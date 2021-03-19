import os
from app import app
from flask import Flask, jsonify, request

@app.route('/')
def nao_entre_em_panico():
    if request.headers.get('Authorization') == '42':
        return jsonify({"42": "a resposta para a vida, o universo e tudo mais"})
    return jsonify({"message": "Não entre em pânico!"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("DEBUG", False)
    host = os.environ.get("HOST", "0.0.0.0")
    
    app.run(host=host, port=port, debug=debug)