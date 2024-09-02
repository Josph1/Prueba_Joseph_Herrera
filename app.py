from flask import Flask, request, jsonify
from main import encontrar_el_subarreglo  

app = Flask(__name__)

@app.route('/subarreglo', methods=['POST'])
def encontrar_subarreglo():
    datos = request.get_json()
    arreglo_inicial = datos.get('array')
    numero_objetivo = datos.get('target')

    if not arreglo_inicial:  
        return jsonify({"subarray": [], "message": "No hay subarreglo en un array vacío"})

    arreglo_out = encontrar_el_subarreglo(arreglo_inicial, numero_objetivo)
    
    if arreglo_out is None:
        return jsonify({"subarray": [], "message": "No hay subarreglo cuya suma sea igual al objetivo"})

    return jsonify({"subarray": arreglo_out})

if __name__ == '__main__':
    app.run(debug=True)



