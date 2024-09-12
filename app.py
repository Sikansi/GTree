from flask import Flask, request, jsonify, render_template
from parente import Parente
import crud
import business

app = Flask(__name__)

# Traz o arquivo index.html para a raiz do projeto
@app.route('/')
def index():
    return render_template('index.html')

# Método post para criar novos parentes
@app.route('/parentes', methods=['POST'])
def adicionar_parente():
    data = request.json
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    # Pega os dados passados no forms pelo front
    nome = data.get('nome')
    pais = data.get('pais', [])
    filhos = data.get('filhos', [])
    irmaos = data.get('irmaos', [])
    conjuge = data.get('conjuge')
    # Cria um objeto Parente com id = 0 para não tornar este um parâmetro opcional
    parente = Parente(0, nome, pais, filhos, irmaos, conjuge)
    parente_id = crud.adicionar_parente(parente)
    parente.id = parente_id
    # A função atualiza_parente é responsável por adicionar o parente recém criado ao 
    # objeto no banco de dados dos parentes com ele relacionados
    business.atualiza_parente(parente)
    return jsonify({"id": parente_id}), 201

# Método get para buscar todos os parentes a fim de disponibilizar no front para facilitar 
# a criação de relação com novos parentes a serem criados
@app.route('/parentes', methods=['GET'])
def listar_parentes():
    parentes = crud.listar_parentes()
    return jsonify([{"id": parente.id, "nome": parente.nome, "pais": parente.pais, "filhos": parente.filhos, "irmaos": parente.irmaos, "conjuge": parente.conjuge} for parente in parentes]), 200

# Método put utilizado para trocar o nome de um parente, atualmente não utilizado
@app.route('/parentes/<int:id>', methods=['PUT'])
def atualizar_parente(id):
    data = request.json
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    nome = data.get('nome')
    parente = Parente(id, nome)
    crud.atualizar_parente(parente)
    return jsonify({"message": "Parente atualizado com sucesso"}), 200

# Método get para buscar todos os parentes de uma árvore e futuramente organizá-los de 
# maneira a facilitar a impressão dos mesmos na forma de árvore genealógica
@app.route('/arvore', methods=['GET'])
def imprime_arvore():
    arvore = crud.imprime_arvore()
    return jsonify(arvore), 200

if __name__ == '__main__':
    crud.criar_tabela()
    app.run(debug=True)
