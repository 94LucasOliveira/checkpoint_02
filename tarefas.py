'''
A Lista: No tarefas.py, crie uma lista vazia chamada lista_tarefas = [].
Adicionar: Crie a função adicionar_tarefa(descricao). Ela monta o dicionário (com concluida: False) e dá o
.append() na lista.
Listar: Crie a função listar_tarefas(). Use um for para percorrer a lista e imprimir as descrições.
O Menu: No main.py, importe as funções e crie o while True com as opções: Adicionar, Listar ou Sair.
'''

'''
Melhorando a Listagem: Na função listar_tarefas(), altere para imprimir o Índice numérico e um símbolo
visual (ex: [X] se True, [ ] se False).
A Atualização: Crie a função concluir_tarefa(indice). Ela acessa a lista naquele índice específico e muda a
chave "concluida" para True.
A Interface: No main.py, crie a opção 3 no menu. Peça o número ao usuário, converta para inteiro e chame a
função!

Dica de Segurança: Usem try/except IndexError na função concluir!
'''

'''
A Biblioteca: No topo do tarefas.py, importe a biblioteca json.
Salvando: Crie a função salvar_dados(). Use with open("dados.json", "w") e json.dump() para gravar a lista
inteira.
Carregando: Crie a função carregar_dados(). Use o modo leitura ("r") e json.load() com um try/except
FileNotFoundError.
A Integração: Chame carregar_dados() no início do main.py, e chame salvar_dados() toda vez que uma tarefa
for adicionada ou concluída!
'''

# tarefas.py
import json

lista_tarefas = []

def adicionar_tarefa(descricao):
    tarefa = {"descricao": descricao, "concluida": False}
    lista_tarefas.append(tarefa)
    salvar_dados()

def listar_tarefas():
    if not lista_tarefas:
        print("\nNenhuma tarefa cadastrada.")
        return
    
    print("\n--- Lista de Tarefas ---")
    for i, tarefa in enumerate(lista_tarefas):
        status = "[X]" if tarefa["concluida"] else "[ ]"
        print(f"{i} - {status} {tarefa['descricao']}")

def concluir_tarefa(indice):
    try:
        lista_tarefas[indice]["concluida"] = True
        salvar_dados()
        print("Tarefa concluída com sucesso!")
    except IndexError:
        print("Erro: Índice da tarefa inválido!")

def salvar_dados():
    with open("dados.json", "w") as f:
        json.dump(lista_tarefas, f)

def carregar_dados():
    global lista_tarefas
    try:
        with open("dados.json", "r") as f:
            lista_tarefas = json.load(f)
    except FileNotFoundError:
        lista_tarefas = []
