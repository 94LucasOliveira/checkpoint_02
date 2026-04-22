# main.py
from tarefas import adicionar_tarefa, listar_tarefas, concluir_tarefa, carregar_dados, excluir_tarefa

def menu():
    carregar_dados()
    while True:
        print("\n--- MENU DE TAREFAS ---")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Concluir Tarefa")
        print("4. Excluir Tarefa")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            desc = input("Descrição da tarefa: ")
            adicionar_tarefa(desc)
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            listar_tarefas()
            try:
                idx = int(input("Digite o número da tarefa para concluir: "))
                concluir_tarefa(idx)
            except ValueError:
                print("Por favor, digite um número válido.")
        elif opcao == "4":
            listar_tarefas()
            try:
                idx = int(input("Digite o número da tarefa para EXCLUIR: "))
            except ValueError:
                print("Por favor, digite um número válido.")
            break
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
