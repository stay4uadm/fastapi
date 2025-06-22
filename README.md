---
title: FastAPI
description: A FastAPI server
tags:
  - fastapi
  - hypercorn
  - python
---

# FastAPI Example

![CI/CD Pipeline](https://github.com/seu-usuario/fastapi-1/workflows/CI/CD%20Pipeline/badge.svg)

Este exemplo inicia um servidor [FastAPI](https://fastapi.tiangolo.com/) que busca datas indisponíveis de calendários de reservas de diferentes plataformas (Booking, VRBO, Holmy, Airbnb).

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/-NvLj4?referralCode=CRJ8FE)

## ✨ Funcionalidades

- FastAPI
- [Hypercorn](https://hypercorn.readthedocs.io/)
- Python 3
- Integração com calendários iCal
- Testes automatizados com pytest
- CI/CD com GitHub Actions
- Análise de cobertura de código

## 📋 Endpoints

- `GET /` - Endpoint de saudação
- `GET /datas-indisponiveis` - Retorna datas indisponíveis de todas as plataformas

## 💁‍♀️ Como usar

### Instalação local
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/fastapi-1.git
cd fastapi-1

# Instale as dependências
pip install -r requirements.txt

# Execute localmente
hypercorn main:app --reload
```

### Executando testes
```bash
# Execute todos os testes
pytest

# Execute com cobertura
pytest --cov=main

# Execute testes específicos
pytest test_main.py::test_root_endpoint -v
```

## 🧪 Testes

O projeto inclui testes abrangentes que cobrem:
- ✅ Endpoint raiz (`/`)
- ✅ Endpoint de datas indisponíveis (`/datas-indisponiveis`)
- ✅ Tratamento de erros de requisição
- ✅ Processamento de calendários vazios
- ✅ Múltiplos eventos de calendário
- ✅ Mocks de requisições HTTP

### Estrutura de testes
- `test_main.py` - Testes principais da API
- `pytest.ini` - Configuração do pytest
- CI/CD configurado com GitHub Actions

## 🚀 Deploy

O projeto está configurado para deploy automático no Railway quando mudanças são feitas na branch `main`.

## 📝 Notas

- Para aprender sobre o uso do FastAPI, visite a [Documentação do FastAPI](https://fastapi.tiangolo.com/tutorial/)
- Para aprender sobre Hypercorn e como configurá-lo, leia a [Documentação](https://hypercorn.readthedocs.io/)
- Os testes usam mocks para evitar requisições reais durante os testes

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

Os testes são executados automaticamente em cada PR!
