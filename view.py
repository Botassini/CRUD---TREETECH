# IMPORTANDO SQlite
import sqlite3 as lite

# CRIANDO CONEXAO
con = lite.connect('dados_equipamentos.db')



# INSERINDO INFORMAÇÕES NO  (INSERT)
def inserir_info(i):
    with con:
        cursor = con.cursor()
        query = 'INSERT INTO equipamentos(nome_equipamento, num_serie, tipo, obs, status, dt_cadastro) VALUES(?, ?, ?, ?, ?, ?)'
        cursor.execute(query, i)





# ACESSANDO INFORMAÇÕES NO DB (SELECT)
def mostrar_info():
    lista_mostrar = []
    with con:
        cursor = con.cursor()
        query = 'SELECT * FROM equipamentos'
        cursor.execute(query)
        info = cursor.fetchall()

        for i in info:
            lista_mostrar.append(i)
    
    return lista_mostrar



# ATUALIZANDO AS INFORMAÇÕES DO DB (UPDATE)
def atualizar_info(i):
    with con:
        cursor = con.cursor()
        query = 'UPDATE equipamentos SET nome_equipamento=?, num_serie=?, tipo=?, obs=?, status=?, dt_cadastro=? where id=?'
        cursor.execute(query, i)


# DELETANDO INFORMAÇÕES NO DB (DELETE)
def deletar_info(i):
    with con:
        cursor = con.cursor()
        query = 'DELETE FROM equipamentos WHERE id=?'
        cursor.execute(query, i)