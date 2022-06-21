# IMPORTANDO SQL
import sqlite3 as lite

# CONEXÃO
conexao = lite.connect('dados_equipamentos.db')

# TABELAS
with conexao:
    cursor = conexao.cursor()
    cursor.execute('CREATE TABLE equipamentos(id INTEGER PRIMARY KEY AUTOINCREMENT, nome_equipamento TEXT, num_serie INTEGER, tipo TEXT, obs TEXT, status TEXT,  dt_cadastro DATE)')
