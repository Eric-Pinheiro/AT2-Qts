# Projeto AT2 - QTS

Projeto de avaliação para a disciplina de Qualidade e Teste de Software (QTS). Consiste em uma aplicação FastAPI para provisionamento de workstations de TI, contemplando testes de integração, E2E, acessibilidade e performance, avaliando os requisitos da ISO/IEC 25010.

## Pré-requisitos

- Gerenciador de pacotes uv instalado.
- Python 3.12+.

## Instalação

# 1. Clone o repositório e acesse o diretório:
   ```bash
   git clone https://github.com/Eric-Pinheiro/AT2-Qts.git
   ``` 
   ```
   cd qts-workstation-provisioning
   ```

Instale as dependências e os navegadores exigidos pelo Playwright:

```Bash
uv sync
uv run playwright install
```
# Como Executar
## 1. Subir a Aplicação Web
Inicie o servidor local:

```Bash
uv run uvicorn src.main:app --port 8000
A interface estará disponível em: http://localhost:8000
```
## 2. Rodar a Suíte de Testes (Pytest)
Execute os testes de integração (com Mocks e Faker), E2E e de Acessibilidade (Axe-core):

```Bash
uv run pytest -v
```
## 3. Rodar o Teste de Carga (Locust)
Para executar o teste de carga simulando múltiplos usuários concorrentes pelo terminal (modo headless):

```Bash
uv run locust --headless -u 50 -r 10 -t 30s 
```
