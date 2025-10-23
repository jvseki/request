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
    fator2 = request.args.get('fator2')
    if not fator2:
        return "Fator2 não fornecido."
    
    fator2 = int(fator2)
    resultado = fator1 * fator2
    return f"O produto de {fator1} e {fator2} é {resultado}."
 

@app.route("/compra")
def compra():
    item = request.args.get('item')
    quantidade = request.args.get('quantidade')

    if item is None or quantidade is None:
        return "Item ou quantidade não fornecidos."
    quantidade = int(quantidade)
    return f"Você comprou {quantidade} unidade(s) de {item}."


@app.route("/classificar")
def classificar():
    nota = request.args.get('nota')
    if nota is None:
        return "Nota não fornecida."
    nota = float(nota)
    if nota >= 7.0:
        return "Aluno com bom desempenho!!"
    elif 5.0 <= nota < 7.0:
        return "Aluno em recuperação."
    else:
        return "Aluno reprovado."
    
@app.route('/senha')
def senha():
    tamanho = request.args.get('tamanho')
    if tamanho is None:
        return "Tamanho não fornecido."
    tamanho = int(tamanho)
    if tamanho < 8:
        return "Senha fraca."
    elif 8 <= tamanho <= 12:
        return "Senha média."
    else:
        return "Senha forte."
    

@app.route('/autenticar')
def autenticar():
    user = request.args.get('user')
    password = request.args.get('password')
    if user == 'admin' and password == '123':
        return "Acesso concedido."
    else:
        return "Acesso negado."
    
@app.route('/mensagem')
def mensagem():
    rementente = request.args.get('remetente')
    destinatario = request.args.get('destinatario')
    if rementente and destinatario:
        return f"mensagem de {rementente} para {destinatario} enviada com sucesso."
    else:
        return "Remetente ou destinatário não fornecidos."
   


@app.route('/api/versao')
def versao():
    versao = 3.12
    if versao:
        return f"A versão atual da API é {versao}."
    else:
        try:
            raise ValueError("Versão não disponível.")
        except ValueError as e:
            return str(e)
        

@app.route('/media')
def media():
    nota1 = request.args.get('nota1')
    nota2 = request.args.get('nota2')
    nota3 = request.args.get('nota3')
    if nota1 is None or nota2 is None or nota3 is None:
        return "Todas as três notas devem ser fornecidas."
    nota1 = float(nota1)
    nota2 = float(nota2)
    nota3 = float(nota3)
    resultado = (nota1 + nota2 + nota3) / 3
    return f"A média das notas é {resultado}."


if __name__ == '__main__':
    app.run(debug=True)