# django-bank-api

API responsável por gerenciar empréstimos e pagamentos.

## Estrutura do Projeto

```
core/
    settings.py
    urls.py
    wsgi.py
    asgi.py
    .env-example
    ...
api/
    models/
    serializers/
    views/
    api/urls.py
    api/tests.py
    ...
manage.py
requirements.txt
```

## Descrição

- **core/**: Contém as configurações principais do projeto Django, incluindo arquivos de configuração, variáveis de ambiente e roteamento global.
- **api/**: Implementa a lógica da aplicação, incluindo modelos de empréstimos e pagamentos, serializadores, views, rotas da API e testes automatizados.

## Instalação

1. Clone o repositório.
2. Crie um ambiente virtual e ative-o.
3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```
4. Configure as variáveis de ambiente no arquivo `.env` baseado em `.env-example` dentro da pasta core.
5. Realize as migrações:
   ```sh
   python manage.py migrate
   ```
6. Crie um superusuário (opcional):
   ```sh
   python manage.py createsuperuser
   ```

## Execução

Para rodar o servidor de desenvolvimento:
```sh
python manage.py runserver
```

## Endpoints Principais

- `/api/loan` — CRUD de empréstimos
- `/api/payment` — CRUD de pagamentos
- `/token/` — Autenticação via token

## Testes

Execute os testes automatizados com:
```sh
python manage.py test
```

---
