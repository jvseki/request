from flask import Flask, request

app = Flask(__name__)

@app.route("/saudacao")
def home():
    nome_usuario = request.args.get('nome')

    if nome_usuario:
        return f"Olá, {nome_usuario}!"  
    else:
        return "Olá, visitante!"

@app.route("/soma")
def soma():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    num1 = int(num1)
    num2 = int(num2)
    
    soma = num1 + num2

    if soma:
        return f"A soma de {num1} e {num2} é {soma}."


@app.route("/status")
def status():
    ativo = request.args.get('ativo')
    if ativo == 'True':
        return "O sistema está ativo."
    else:
        return "O sistema está inativo."
    

@app.route("/multiplicacao")
def multiplicacao():
    fator1 = 5
    fator1 = int(fator1)
    fator2 = request.args.get('fator2')
    fator2 = int(fator2)
    if not int(fator2):
         return "O fator1 não foi fornecido."
    multiplicacao =  int(fator1 * fator2)
    return f"A multiplicação de {fator1} e {fator2} é {multiplicacao}."
 

@app.route("/compra")
def compra():
    item = request.args.get('item')
    quantidade = request.args.get('quantidade')

    if item is None or quantidade is None:
        return "Item ou quantidade não fornecidos."
    quantidade = int(quantidade)
    return f"Você comprou {quantidade} unidade(s) de {item}."


if __name__ == '__main__':
    app.run(debug=True)