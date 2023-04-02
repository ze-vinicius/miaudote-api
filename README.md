# Miaudote - Backend

## Requesitos

- Python 3.9+
- Pip

## Instalação

1. Clone o repositório:

```bash
  git clone https://github.com/seu_usuario/miaudote-backend.git
  cd miaudote-backend
```

2. Instale as dependências:

```bash
  pip install -r requirements.txt
```

3. Configure as variáveis de ambiente no arquivo .env. Um exemplo de arquivo .env.example está incluído no repositório.

```bash
  cp .env.example .env
```

4. Ajuste as configurações no arquivo .env

## Execução

Para executar o servidor de desenvolvimento localmente, use o seguinte comando:

```bash
  uvicorn app.main:app --reload
```

O servidor estará disponível em http://localhost:8000.

## Endpoints

Os principais endpoints da api incluem:

- POST/GET `/pet_shelters`: Lista e cria um abrigo
- GET `/pet_shelters/{id}/pets`: Lista os pets disponíveis de um abrigo
- POST `/pets`: Cria um animal para adoção vinculado ao abrigo do usuário autenticado
