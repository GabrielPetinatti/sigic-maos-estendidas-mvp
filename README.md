# SIGIC - Mãos Estendidas (MVP)

**Sistema Integrado de Gestão de Inventário Comunitário** desenvolvido em Python e Flask para a **Associação Beneficente Mãos Estendidas** (Cidade Tiradentes, São Paulo - SP).

## Objetivo do Projeto
Substituir o controle manual de doações feito em cadernos por uma aplicação web responsiva e ultraleve, eliminando o desperdício involuntário de alimentos por vencimento através da ordenação preventiva **FIFO (First-In, First-Out)** e apoiando o **ODS 2 (Fome Zero)** da ONU.

## Arquitetura e Tecnologias
- **Padrão Arquitetural:** Monolítico em Camadas (MVC)
- **Linguagem:** Python 3.12
- **Framework Web:** Flask 3.0
- **Banco de Dados:** PostgreSQL (Supabase)
- **Interface:** HTML5 e CSS3 Responsivos (Acessibilidade WCAG 2.1 AA)

## Estrutura do Repositório
- `app.py`: Rotas principais, regras de negócio (algoritmo FIFO) e controle de sessão.
- `requirements.txt`: Dependências do projeto Python.
- `templates/`: Telas HTML responsivas (Login, Cadastro/Baixa e Painel FIFO).
- `tests/`: Testes automatizados unitários e de integração (`pytest`).
