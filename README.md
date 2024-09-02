# Buscador de Subarreglos con Flask

Este repositorio contiene una aplicación Flask que encuentra un subarreglo dentro de un arreglo dado cuya suma es igual a un número objetivo especificado.

## Tabla de Contenidos

- [Descripción](#descripción)
- [Instalación](#instalación)
- [Uso](#uso)

## Descripción

Esta aplicación utiliza Flask para proporcionar una API REST que permite encontrar subarreglos en un arreglo de números que sumen a un objetivo específico.

## Instalación

Para instalar la aplicación en Windows, sigue estos pasos:

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/flask-subarray-finder.git
   cd flask-subarray-finder
   
2. **Instala Flask**: Asegúrate de tener Python instalado en tu sistema. Luego, instala Flask utilizando pip:
   pip install flask
   
## **Uso**
Para ejecutar la aplicación Flask en Windows, sigue estos pasos:

1. **Ejecuta la aplicación**: Abre una terminal en la carpeta del proyecto y ejecuta el siguiente comando:
   ```bash
   python app.py

   Por defecto, la aplicación se ejecutará en http://localhost:5000.

2. **Probar el endpoint:**

   Puedes probar el endpoint /subarreglo utilizando curl o cualquier cliente HTTP (como Postman). Aquí hay un ejemplo usando curl en la línea de comandos de Windows
   
   ```bash
   curl -X POST -H "Content-Type: application/json" -d "{\"array\": [1, -2, 1, 1, -1, 2, 4], \"target\": 0}" http://localhost:5000/subarreglo

4. **Salida Esperada**
Para la entrada {"array": [1, -2, 1, 1, -1, 2, 4], "target": 0}, la salida esperada será:

```bash
{
    "subarray": [1, -2, 1, 1, -1]
}

