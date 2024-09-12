import sqlite3
from typing import List
from parente import Parente

# Cria a tabela de parentes no banco de dados
def criar_tabela():
    conexao = sqlite3.connect('parentes.db')
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS parentes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        pais TEXT,
                        filhos TEXT,
                        irmaos TEXT,
                        conjuge_id TEXT)''')
    conexao.commit()
    conexao.close()

def adicionar_parente(parente: Parente):
    conexao = sqlite3.connect('parentes.db')
    cursor = conexao.cursor()
    cursor.execute('''INSERT INTO parentes (nome, pais, filhos, irmaos, conjuge_id) VALUES (?, ?, ?, ?, ?)''', 
                   (parente.nome, 
                    str(' '.join(str(pai) for pai in parente.pais)), 
                    str(' '.join(str(filho) for filho in parente.filhos)), 
                    str(' '.join(str(irmao) for irmao in parente.irmaos)), 
                    parente.conjuge))
    conexao.commit()
    cursor.execute('''SELECT last_insert_rowid()''')
    parente_id = cursor.fetchone()[0]
    conexao.close()
    return parente_id

# Lista todos os parentes
def listar_parentes() -> List[Parente]:
    conexao = sqlite3.connect('parentes.db')
    cursor = conexao.cursor()
    cursor.execute('''SELECT id, nome, pais, filhos, irmaos, conjuge_id FROM parentes''')
    parentes_raw = cursor.fetchall()
    conexao.close()

    parentes = []
    for parente_raw in parentes_raw:
        id, nome, pais_str, filhos_str, irmaos_str, conjuge_id = parente_raw
        pais = [pai for pai in pais_str.split()] if pais_str else []
        filhos = [filho for filho in filhos_str.split()] if filhos_str else []
        irmaos = [irmao for irmao in irmaos_str.split()] if irmaos_str else []
        conjuge = conjuge_id if conjuge_id else None
        parente = Parente(id, nome, pais, filhos, irmaos, conjuge)
        parentes.append(parente)

    return parentes

# Atualiza um parente por ID
def atualizar_parente(parente: Parente):
    conexao = sqlite3.connect('parentes.db')
    cursor = conexao.cursor()
    cursor.execute('''
        UPDATE parentes
        SET nome = ?, pais = ?, filhos = ?, irmaos = ?, conjuge_id = ?
        WHERE id = ?
    ''', (parente.nome, 
            str(' '.join(str(pai) for pai in parente.pais)), 
            str(' '.join(str(filho) for filho in parente.filhos)), 
            str(' '.join(str(irmao) for irmao in parente.irmaos)), 
            parente.conjuge,
            parente.id))
    conexao.commit()
    conexao.close()

# Deleta um parente por ID
def deletar_parente(id):
    conexao = sqlite3.connect('parentes.db')
    cursor = conexao.cursor()
    cursor.execute('''DELETE FROM parentes WHERE id = ?''', (id,))
    conexao.commit()
    conexao.close()

# Retorna um parente por ID
def buscar_parente(id):
    conexao = sqlite3.connect('parentes.db')
    cursor = conexao.cursor()
    cursor.execute('''SELECT id, nome, pais, filhos, irmaos, conjuge_id FROM parentes WHERE id = ?''', (id,))
    parente_raw = cursor.fetchone()
    conexao.close()

    if parente_raw:
        id, nome, pais_str, filhos_str, irmaos_str, conjuge_id = parente_raw
        pais = [pai for pai in pais_str.split()] if pais_str else []
        filhos = [filho for filho in filhos_str.split()] if filhos_str else []
        irmaos = [irmao for irmao in irmaos_str.split()] if irmaos_str else []
        conjuge = conjuge_id if conjuge_id else None
        return Parente(id, nome, pais, filhos, irmaos, conjuge)
    return None

def imprime_arvore():
    conexao = sqlite3.connect('parentes.db')
    cursor = conexao.cursor()
    cursor.execute('''SELECT * FROM parentes''')
    parentes = cursor.fetchall()
    conexao.close()
    return parentes
