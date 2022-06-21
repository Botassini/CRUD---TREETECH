# IMPORTANDO BIBLIOTECAS

from msilib.schema import CheckBox
from telnetlib import NAWS
import tkinter
from tkinter.tix import CheckList
from tkinter import ttk
from tkinter import messagebox
from turtle import width
#import request
from tkinter import *
from setuptools import Command

# IMPORTANDO TKCALENDAR
from tkcalendar import Calendar, DateEntry

# IMPORTANDO VIEW (view.py)
from view import *

####################### CORES #######################

co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue

####################### JANELA (INTERFACE) #######################

janela = Tk()
janela.title('TreeTech Sistemy')
janela.geometry('1130x460')
janela.configure(background=co9)
janela.resizable(width=False, height=False)

####################### DIVINDO AS INTERFACES #######################

parte_cima = Frame(janela, width=300, height=50, bg=co2, relief='flat')
parte_cima.grid(row=0, column=0)

parte_baixo = Frame(janela, width=300, height=400, bg=co1, relief='flat')
parte_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

parte_exibicao = Frame(janela, width=747, height=400, bg=co1, relief='flat')
parte_exibicao.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

# TESTE - BUSCA DE EQUIPAMENTOS (FINALIZAR)
#parte_busca = Frame(janela, width=747, height=50, bg=co2, relief='flat')
#parte_busca.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NE)


####################### DIVINDO AS INTERFACES #######################

app_nome = Label(parte_cima, text='Cadastro de Equipamentos', font=('Ivy 14 bold'), fg=co1, bg=co2, relief='flat')
app_nome.place(x=10, y=10)

####################### ORGANIZANDO FORMULARIO #######################

# ID EQUIPAMENTOS
label_id_equipamentos = Label(parte_baixo, text='ID: ', font=('Ivy 10 bold'), fg=co4, bg=co1, relief='flat')
label_id_equipamentos.place(x=10, y=10)
entrada_id_equipamentos = Label(parte_baixo, width=25, justify='left', relief='flat')
entrada_id_equipamentos.place(x=78, y=10)

# NOME DOS EQUIPAMENTOS
label_nome_equipamentos = Label(parte_baixo, text='Nome: ', font=('Ivy 10 bold'), fg=co4, bg=co1, relief='flat')
label_nome_equipamentos.place(x=10, y=40)

entrada_nome_equipamentos = Entry(parte_baixo, width=30, justify='left', relief='solid')
entrada_nome_equipamentos.place(x=78, y=40)

# NUMERO DE SERIE DOS EQUIPAMENTOS
label_num_serie = Label(parte_baixo, text='N° Série: ', font=('Ivy 10 bold'), fg=co4, bg=co1, relief='flat')
label_num_serie.place(x=10, y=70)
entrada_label_num_serie = Entry(parte_baixo, width=30, justify='left', relief='solid')
entrada_label_num_serie.place(x=78, y=70)

# TIPO DE EQUIPAMENTO
label_tipo_equipamento = Label(parte_baixo, text='Tipo: ', font=('Ivy 10 bold'), fg=co4, bg=co1, relief='flat')
label_tipo_equipamento.place(x=10, y=100)
entrada_tipo_equipamento = Entry(parte_baixo, width=30, justify='left', relief='solid')
entrada_tipo_equipamento.place(x=78, y=100)

# STATUS DO EQUIPAMENTO
label_status_equipamento = Label(parte_baixo, text='Status: ', font=('Ivy 10 bold'), fg=co4, bg=co1, relief='flat')
label_status_equipamento.place(x=10, y=130)
entrada_status_equipamento = Entry(parte_baixo, width=30, justify='left', relief='solid')
entrada_status_equipamento.place(x=78, y=130)

# DATA DO CADASTRO
label_dt_cadastro = Label(parte_baixo, text='Data de Cadastro: ', font=('Ivy 10 bold'), fg=co4, bg=co1, relief='flat')
label_dt_cadastro.place(x=10, y=190)
entrada_dt_cadastro = DateEntry(parte_baixo, width=10, background='darkblue', foreground='white', borderwidth=2)
entrada_dt_cadastro.place(x=135, y=190)

# OBERSERVAÇÕES
label_observacoes = Label(parte_baixo, text='OBS: ', font=('Ivy 10 bold'), fg=co4, bg=co1, relief='flat')
label_observacoes.place(x=10, y=160)
entrada_observacoes = Entry(parte_baixo, width=30, justify='left', relief='solid')
entrada_observacoes.place(x=78, y=160)


# FUNÇÃO INSERIR 
def inserir():
    nome_equipamentos = entrada_nome_equipamentos.get()
    num_serie = entrada_label_num_serie.get()
    tipo = entrada_tipo_equipamento.get()
    observacoes = entrada_observacoes.get()
    status = entrada_status_equipamento.get()
    data_cadastro = entrada_dt_cadastro.get()
    
    
    lista_inserir = [nome_equipamentos, num_serie, tipo, observacoes, status, data_cadastro]

    # VERIFICAÇAO NOME_EQUIPAMENTOS
    if nome_equipamentos == '':
        messagebox.showerror('Erro', 'O nome não pode ser vazio')
    if num_serie == '':
        messagebox.showerror('ERRO', 'O número de série não pode ser vazio')
    if tipo == '':
        messagebox.showerror('ERRO', 'O tipo de equipamento não pode ser vazio')
    if status == '':
        messagebox.showerror('ERRO', 'O status não pode ser vazio')
        # COLOCAR OU NÃO OBSERVAÇÕES SERÁ OPICIONAL DO USUARIO, PORTANTO NÃO É NECESSÁRIO UMA VERIFICAÇÃO!
    #if observacoes == '':
        #messagebox.showerror('ERRO', 'A observação não podo estar vazia')
    #if data_cadastro == '':
        messagebox.showerror('ERRO', 'A data de cadastro não pode estar vazia')
    else:
        inserir_info(lista_inserir)
        messagebox.showinfo('SUCESSO!', 'Os dados foram inseridos com sucesso')
    
        entrada_nome_equipamentos.delete(0, 'end')
        entrada_label_num_serie.delete(0, 'end')
        entrada_tipo_equipamento.delete(0, 'end')
        entrada_status_equipamento.delete(0, 'end')
        entrada_dt_cadastro.delete(0, 'end')
        entrada_observacoes.delete(0, 'end')

    for widget in parte_exibicao.winfo_children():
        widget.destroy()

    mostrar()


# VARIAVEL GLOBAL tree
global tree
# FUNÇÃO DE ATUALIZAR 
def carregar():
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        entrada_nome_equipamentos.delete(0, 'end')
        entrada_label_num_serie.delete(0, 'end')
        entrada_tipo_equipamento.delete(0, 'end')
        entrada_observacoes.delete(0, 'end')
        entrada_status_equipamento.delete(0, 'end')
        entrada_dt_cadastro.delete(0, 'end')

        entrada_id_equipamentos.config(text= tree_lista[0])
        entrada_nome_equipamentos.insert(0, tree_lista[1])
        entrada_label_num_serie.insert(0, tree_lista[2])
        entrada_tipo_equipamento.insert(0, tree_lista[3])
        entrada_observacoes.insert(0, tree_lista[4])
        entrada_status_equipamento.insert(0, tree_lista[5])
        entrada_dt_cadastro.insert(0, tree_lista[6])

def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']
        
        valor_id = tree_lista[0]

        deletar_info([valor_id])
        messagebox.showinfo('SUCESSO', 'Os dados foram deletados! ')

        for widget in parte_exibicao.winfo_children():
            widget.destroy()

        mostrar()

    except IndexError:
        messagebox.showerror('ERRO', 'Selecione um dos dados da tabela! ')

def updata():
            treev_dados = tree.focus()
            treev_dicionario = tree.item(treev_dados)
            tree_lista = treev_dicionario['values']

            id_equipamentos = entrada_id_equipamentos.cget('text')
            nome_equipamentos = entrada_nome_equipamentos.get()
            num_serie = entrada_label_num_serie.get()
            tipo = entrada_tipo_equipamento.get()
            observacoes = entrada_observacoes.get()
            status = entrada_status_equipamento.get()
            data_cadastro = entrada_dt_cadastro.get()

            #ntrada_nome_equipamentos.insert(0, tree_lista[1])
            #entrada_label_num_serie.insert(0, tree_lista[2])
            #entrada_tipo_equipamento.insert(0, tree_lista[3])
            #entrada_observacoes.insert(0, tree_lista[4])
            #entrada_status_equipamento.insert(0, tree_lista[5])
            #entrada_dt_cadastro.insert(0, tree_lista[6])

            lista_inserir = [nome_equipamentos, num_serie, tipo, observacoes, status, data_cadastro, id_equipamentos]

            if nome_equipamentos == '':
                messagebox.showerror('ERRO', 'O nome não pode ser vazio')
            else:
                atualizar_info(lista_inserir)
                messagebox.showinfo('SUCESSO', 'Os dados foram atualizados!')

                entrada_nome_equipamentos.delete(0, 'end')
                entrada_label_num_serie.delete(0, 'end')
                entrada_tipo_equipamento.delete(0, 'end')
                entrada_observacoes.delete(0, 'end')
                entrada_status_equipamento.delete(0, 'end')
                entrada_dt_cadastro.delete(0, 'end')
                entrada_id_equipamentos.config(text= '')
            
            for widget in parte_exibicao.winfo_children():
                widget.destroy()
            mostrar()
# BOTAO DE ATUALIZAR
botao_atualizar = Button(parte_baixo, command=carregar, text='CARREGAR', font=('Ivy 10 bold'), fg=co4, bg=co2, relief='raised', width=10)
botao_atualizar.place(x=100, y=300)

# BOTAO DE INSERIR
botao_inserir = Button(parte_baixo, command=inserir, text='INSERIR', font=('Ivy 10 bold'), fg=co4, bg=co6, relief='raised', width=8, overrelief='')
botao_inserir.place(x=15, y=300)

# BOTAO DELETAR
botao_deletar = Button(parte_baixo,command=deletar, text='DELETAR', font=('Ivy 10 bold'), fg=co4, bg=co7, relief='raised', width=10)
botao_deletar.place(x=200, y=300)

# BOTAO CONFIRMAR UPDATE
botao_confirmar = Button(parte_baixo, command=updata, text='CONFIRMAR', font=('Ivy 10 bold'), fg=co4, bg=co2, relief='raised', width=10)
botao_confirmar.place(x=100, y=330)


####################### PARTE DIREITA (TABELA) #######################

def mostrar():
    global tree
    
    lista = mostrar_info()

    tabel_head = ['ID','Nome', 'N° de Série', 'Tipo','Observações', 'Status', 'Data']


    # CONFIGURAÇAO DA CABEÇA DA LISTA
    tree = ttk.Treeview(parte_exibicao, selectmode='extended', columns=tabel_head, show='headings')

    # SCROLLBAR VERTICAL
    vsb = ttk.Scrollbar(parte_exibicao, orient='vertical', command=tree.yview)

    # SCROLLBAR HORIZONTAL
    hsb = ttk.Scrollbar(parte_exibicao, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='NSEW')
    vsb.grid(column=1, row=0, sticky='NS')
    hsb.grid(column=0, row=1, sticky='EW')
    parte_exibicao.grid_rowconfigure(0, weight=12)

    hd=['nw', 'center', 'center', 'center', 'center', 'center', 'center']
    h=[30, 100, 150, 100, 300, 70, 90]
    n=0

    for col in tabel_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        #AJUSTANDO O TAMANHANHO DO TEXTO
        tree.column(col, width=h[n], anchor=hd[n])

        n+=1

    for item in lista:
        tree.insert('', 'end', values=item)

# CHAMANDO A FUNÇÃO MOSTRAR
mostrar()
janela.mainloop()