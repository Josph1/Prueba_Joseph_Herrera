from flask import Flask, request, jsonify
from main import encontrar_el_subarreglo  

app = Flask(__name__) # Inicializacion de la aplicacion flask

@app.route('/subarreglo', methods=['POST'])#Define la ruta y el método HTTP
def encontrar_subarreglo():
    datos = request.get_json()# Obtiene los datos JSON de la solicitud
    arreglo_inicial = datos.get('array')
    numero_objetivo = datos.get('target')

    # Verifica si el arreglo está vacío
    if not arreglo_inicial:  
        return jsonify({"subarray": [], "message": "No hay subarreglo en un array vacío"})

    arreglo_out = encontrar_el_subarreglo(arreglo_inicial, numero_objetivo)

    # Verifica si se encontró un subarreglo válido
    if arreglo_out is None: 
        return jsonify({"subarray": [], "message": "No hay subarreglo cuya suma sea igual al objetivo"})
        
    return jsonify({"subarray": arreglo_out})
    
if __name__ == '__main__':
    app.run(debug=True)#Ejecución de la aplicación Flask en modo debug



