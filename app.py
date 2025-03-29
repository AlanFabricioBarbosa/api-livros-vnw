from flask import Flask, request, jsonify
from marshmallow import Schema, fields
import sqlite3
import re
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
def init_db():
   with sqlite3.connect('database.db') as conn:
      conn.execute(
            """CREATE TABLE IF NOT EXISTS livros(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               titulo TEXT NOT NULL,
               categoria TEXT NOT NULL,
               autor TEXT NOT NULL,
               imagem_url TEXT NOT NULL
            )"""
      )
      print('Banco de dados criado!')

init_db()
class LivroSchema(Schema):
   id = fields.Int(dump_only=True)
   titulo = fields.Str(required=True)
   categoria = fields.Str(required=True)
   autor = fields.Str(required=True)
   imagem_url = fields.Str(required=True)

@app.route('/')
def home_page():
   return '<h2>Flask Home Page</h2>'

@app.route('/doar', methods=['POST'])
def doar():
   dados = request.get_json()

   titulo = dados.get('titulo')
   categoria = dados.get('categoria')
   autor = dados.get('autor')
   imagem_url = dados.get('imagem_url')

   if not all([titulo, categoria, autor, imagem_url]):
      return jsonify({"erro": "Todos os campos são obrigatórios"}), 400

   if not re.match(r'^https://', imagem_url):
      return jsonify({"erro": "A URL da imagem deve começar com 'https://'"}), 400

   with sqlite3.connect('database.db') as conn:
      conn.execute(""" INSERT INTO livros (titulo, categoria, autor, imagem_url)
                     VALUES (?,?,?,?)
                     """, (titulo, categoria, autor, imagem_url))
      conn.commit()
   
   return jsonify({"mensagem": "Livro cadastrado com sucesso"}), 201

@app.route('/livros', methods=['GET'])
def listar_livros():
   with sqlite3.connect('database.db') as conn:
      livros = conn.execute("SELECT * FROM livros").fetchall()

      livros_formatados = []
      for livro in livros:
            livro_dict = {
               "id": livro[0],
               "titulo": livro[1],
               "categoria": livro[2],
               "autor": livro[3],
               "imagem_url": livro[4]
            }
            livros_formatados.append(livro_dict)

      livro_schema = LivroSchema(many=True)
      livros_serializados = livro_schema.dump(livros_formatados)

   return jsonify(livros_serializados)

@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
   with sqlite3.connect('database.db') as conn:
      cur = conn.cursor()
      cur.execute("SELECT * FROM livros WHERE id=?", (id,))
      livro = cur.fetchone()

      if livro is None:
            return jsonify({"erro": "Livro não encontrado"}), 404

      conn.execute("DELETE FROM livros WHERE id=?", (id,))
      conn.commit()

   return jsonify({"mensagem": f"Livro com id {id} excluído com sucesso"}), 200

if __name__ == '__main__':
   app.run(debug=True)


