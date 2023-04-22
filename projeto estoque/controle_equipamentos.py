import tkinter as tk

equipamentos = {}

def adicionar_equipamento():
    nome_equipamento = nome_equipamento_entry.get()
    quantidade = int(quantidade_entry.get())
    equipamentos[nome_equipamento] = equipamentos.get(nome_equipamento, 0) + quantidade
    resultado_label.config(text="Equipamento adicionado com sucesso!")

def remover_equipamento():
    nome_equipamento = nome_equipamento_entry.get()
    if nome_equipamento in equipamentos:
        quantidade = int(quantidade_entry.get())
        if equipamentos[nome_equipamento] < quantidade:
            resultado_label.config(text="Não há equipamentos suficientes para remover.")
        else:
            equipamentos[nome_equipamento] -= quantidade
            resultado_label.config(text="Equipamento removido com sucesso!")
    else:
        resultado_label.config(text="O equipamento não está na lista.")

def listar_equipamentos():
    lista_equipamentos = ""
    for equipamento, quantidade in equipamentos.items():
        lista_equipamentos += equipamento + " - " + str(quantidade) + "\n"
    resultado_label.config(text=lista_equipamentos)

root = tk.Tk()
root.title("Entrada e Saída de Equipamentos - VOIP NORDESTE")

nome_equipamento_label = tk.Label(root, text="Nome do equipamento:")
nome_equipamento_label.grid(row=0, column=0, padx=10, pady=10)

nome_equipamento_entry = tk.Entry(root)
nome_equipamento_entry.grid(row=0, column=1, padx=10, pady=10)

quantidade_label = tk.Label(root, text="Quantidade:")
quantidade_label.grid(row=1, column=0, padx=10, pady=10)

quantidade_entry = tk.Entry(root)
quantidade_entry.grid(row=1, column=1, padx=10, pady=10)

adicionar_button = tk.Button(root, text="Adicionar equipamento", command=adicionar_equipamento)
adicionar_button.grid(row=2, column=0, padx=10, pady=10)

remover_button = tk.Button(root, text="Remover equipamento", command=remover_equipamento)
remover_button.grid(row=2, column=1, padx=10, pady=10)

listar_button = tk.Button(root, text="Listar equipamentos", command=listar_equipamentos)
listar_button.grid(row=3, column=0, padx=10, pady=10)

resultado_label = tk.Label(root, text="")
resultado_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

sair_button = tk.Button(root, text="Sair", command=root.quit)
sair_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
