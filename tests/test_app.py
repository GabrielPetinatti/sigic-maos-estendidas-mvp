from app import app, calcular_alerta_fifo
from datetime import datetime, timedelta

def test_ordenacao_e_alerta_fifo():
    hoje = datetime.now().date()
    data_critica = (hoje + timedelta(days=10)).strftime("%Y-%m-%d")
    data_normal = (hoje + timedelta(days=90)).strftime("%Y-%m-%d")
    itens_teste = [
        {"nome": "Feijão", "validade": data_normal},
        {"nome": "Leite", "validade": data_critica}
    ]
    resultado = calcular_alerta_fifo(itens_teste)
    assert resultado[0]['nome'] == "Leite"
    assert resultado[0]['alerta_critico'] is True
    assert resultado[1]['alerta_critico'] is False

def test_bloqueio_rota_sem_login():
    client = app.test_client()
    resposta = client.get('/painel')
    assert resposta.status_code == 302
