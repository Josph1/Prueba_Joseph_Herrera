from flask import Flask, requests , jsonify


app = Flask(__name__)

@app.route('/subarreglo', methods=['POST'])

def encontrar_subarreglo():
  datos = request.get_json()
  arreglo = data.get('array')
  numero_objetivo = datos.get('target')

subarreglo = encontrar



