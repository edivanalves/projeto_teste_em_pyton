equipamentos = {}

while True:
    print("Bem-vindo ao sistema de entrada e saída de equipamentos da VOIP NORDESTE")
    print("Selecione uma opção:")
    print("1 - Adicionar equipamento")
    print("2 - Remover equipamento")
    print("3 - Listar equipamentos")
    print("4 - Sair do programa")
    
    opcao = int(input())
    
    if opcao == 1:
        nome_equipamento = input("Digite o nome do equipamento: ")
        quantidade = int(input("Digite a quantidade: "))
        equipamentos[nome_equipamento] = equipamentos.get(nome_equipamento, 0) + quantidade
        print("Equipamento adicionado com sucesso!")
        
    elif opcao == 2:
        nome_equipamento = input("Digite o nome do equipamento que deseja remover: ")
        if nome_equipamento in equipamentos:
            quantidade = int(input("Digite a quantidade que deseja remover: "))
            if equipamentos[nome_equipamento] < quantidade:
                print("Não há equipamentos suficientes para remover.")
            else:
                equipamentos[nome_equipamento] -= quantidade
                print("Equipamento removido com sucesso!")
        else:
            print("O equipamento não está na lista.")
        
    elif opcao == 3:
        print("Lista de equipamentos:")
        for equipamento, quantidade in equipamentos.items():
            print(equipamento, "-", quantidade)
        
    elif opcao == 4:
        print("Encerrando o programa...")
        break
        
    else:
        print("Opção inválida. Digite novamente.")