from flask import Flask, requests , jsonify


app = Flask(__name__)

@app.route('/subarreglo', methods=['POST'])

def encontrar_subarreglo():
  datos = request.get_json()
  arreglo_inicial = data.get('array')
  numero_objetivo = datos.get('target')
  arreglo_out = encontar_el_subarreglo(arreglo, numero_objetivo)
  return jsonify("subarray": arreglo_out)

if __name__ == '__main__':
  app.run(debug=True)




