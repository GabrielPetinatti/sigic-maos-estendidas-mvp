from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'chave_segura_mvp_sigic_2026')

USUARIO_PADRAO = {"username": "voluntario_01", "password_hash": generate_password_hash("senha_teste_123")}
estoque = [
    {"id": 1, "nome": "Macarrão Parafuso", "categoria": "Alimento", "quantidade": 15, "validade": "2026-11-28"},
    {"id": 2, "nome": "Arroz Agulhinha", "categoria": "Alimento", "quantidade": 40, "validade": "2027-03-10"}
]

def calcular_alerta_fifo(itens):
    hoje = datetime.now().date()
    limite = hoje + timedelta(days=30)
    ordenados = sorted(itens, key=lambda x: x['validade'])
    for item in ordenados:
        dt_val = datetime.strptime(item['validade'], "%Y-%m-%d").date()
        item['alerta_critico'] = dt_val <= limite
    return ordenados

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('username')
        pwd = request.form.get('password')
        if user == USUARIO_PADRAO['username'] and check_password_hash(USUARIO_PADRAO['password_hash'], pwd):
            session['usuario'] = user
            return redirect(url_for('painel'))
    return render_template('login.html')

@app.route('/painel')
def painel():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    itens_fifo = calcular_alerta_fifo(estoque)
    return render_template('painel.html', itens=itens_fifo)

@app.route('/movimentar', methods=['POST'])
def movimentar():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    nome = request.form.get('nome')
    categoria = request.form.get('categoria')
    qtd = int(request.form.get('quantidade', 0))
    validade = request.form.get('validade')
    if nome and qtd > 0 and validade:
        estoque.append({"id": len(estoque)+1, "nome": nome, "categoria": categoria, "quantidade": qtd, "validade": validade})
    return redirect(url_for('painel'))

if __name__ == '__main__':
    app.run(debug=False)
