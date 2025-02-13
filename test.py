from flask import Flask, request, jsonify
 
app = Flask(__name__)

@app.route('/')
def helloWorld():
    return jsonify({"status": "success", "result": 'Hello World'})
 
@app.route('/procesar', methods=['POST'])
def procesar():
    # Obtener los parámetros
    valor1 = request.json.get("valor1")
    valor2 = request.json.get("valor2")
 
    if valor1 is None or valor2 is None:
        return jsonify({"status": "error", "message": "Faltan valores"})
 
    resultado = valor1 + valor2
 
    return jsonify({"status": "success", "resultado": resultado})
 
if __name__ == '__main__':
    app.run(host='0.0.0.0')