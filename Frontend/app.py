from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

@app.route('/guardar_cliente', methods=['POST'])
def guardar_cliente():
    datos = request.json
    print("Cliente recibido:", datos)  
    return jsonify({"mensaje": "Cliente guardado correctamente (simulado)."}), 200

if __name__ == '__main__':
    app.run(debug=True)
