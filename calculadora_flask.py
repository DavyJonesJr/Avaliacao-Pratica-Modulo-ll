from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template("index.html")

@app.route("/soma", methods=["GET"])
def soma():
    valor1 = float(request.args.get("valor1"))
    valor2 = float(request.args.get("valor2"))

    return jsonify(f"Resultado: {valor1 + valor2}"), 201

@app.route("/subtrair", methods=["GET"])
def subtrair():
    valor1 = float(request.args.get("valor1"))
    valor2 = float(request.args.get("valor2"))

    return jsonify(f"Resultado: {valor1 - valor2}"), 201

@app.route("/multiplicar", methods=["GET"])
def multiplicar():
    valor1 = float(request.args.get("valor1"))
    valor2 = float(request.args.get("valor2"))

    return jsonify(f"Resultado: {valor1 * valor2}"), 201

@app.route("/dividir", methods=["GET"])
def dividir():
    valor1 = float(request.args.get("valor1"))
    valor2 = float(request.args.get("valor2"))

    if valor2 == 0:
        return{"erro": "Divisao por zero pode nao"}

    else: 
        return jsonify(f"Resultado: {valor1 / valor2}"), 201

if __name__ == "__main__":
    app.run(debug=True)