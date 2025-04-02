# Documentação da API Flask para Gerenciamento de Livros

## Introdução
Esta é uma API desenvolvida em Flask para o gerenciamento de livros. A API permite a doação de livros, listagem dos livros cadastrados e exclusão de um livro específico. A base de dados utilizada é SQLite.

## Tecnologias Utilizadas
- Python
- Flask
- SQLite
- Marshmallow (para validação de dados)
- Flask-CORS (para habilitar o CORS)

## Instalação e Execução

1. Clone o repositório:
   ```sh
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DO_REPOSITORIO>
   ```

2. Instale as dependências:
   ```sh
   pip install flask flask-cors marshmallow sqlite3
   ```

3. Execute a aplicação:
   ```sh
   python app.py
   ```

A API será executada em `http://127.0.0.1:5000/`.

## Estrutura do Banco de Dados
A API cria automaticamente um banco de dados SQLite (`database.db`) com a seguinte estrutura:

| Campo       | Tipo    | Restrições                 |
|------------|--------|--------------------------|
| id         | INTEGER | PRIMARY KEY AUTOINCREMENT |
| titulo     | TEXT   | NOT NULL                  |
| categoria  | TEXT   | NOT NULL                  |
| autor      | TEXT   | NOT NULL                  |
| imagem_url | TEXT   | NOT NULL                  |

## Rotas da API

### 1. Rota Home
- **Rota:** `/`
- **Método:** `GET`
- **Resposta:** Retorna uma página HTML simples com `Flask Home Page`.

### 2. Doar um Livro
- **Rota:** `/doar`
- **Método:** `POST`
- **Requisição:** JSON com os seguintes campos obrigatórios:
  ```json
  {
    "titulo": "Nome do Livro",
    "categoria": "Categoria do Livro",
    "autor": "Nome do Autor",
    "imagem_url": "https://exemplo.com/imagem.jpg"
  }
  ```
- **Validação:**
  - Todos os campos são obrigatórios.
  - A URL da imagem deve começar com `https://`.
- **Resposta:**
  - `201 Created` se o livro for cadastrado com sucesso.
  - `400 Bad Request` se houver erro de validação.

### 3. Listar Todos os Livros
- **Rota:** `/livros`
- **Método:** `GET`
- **Resposta:** Retorna um JSON com todos os livros cadastrados:
  ```json
  [
    {
      "id": 1,
      "titulo": "Nome do Livro",
      "categoria": "Categoria do Livro",
      "autor": "Nome do Autor",
      "imagem_url": "https://exemplo.com/imagem.jpg"
    }
  ]
  ```

### 4. Excluir um Livro
- **Rota:** `/livros/<id>`
- **Método:** `DELETE`
- **Parâmetro:** `id` (inteiro, identificação do livro a ser excluído)
- **Resposta:**
  - `200 OK` se o livro for excluído com sucesso.
  - `404 Not Found` se o livro não for encontrado.

## Considerações Finais
Esta API é uma solução simples para o gerenciamento de doação de livros, permitindo a adição, listagem e remoção de livros de um banco de dados SQLite. Caso deseje expandir a API, recomenda-se adicionar autenticação e mais validações nos dados enviados.

