import tkinter as tk

def calcular_imc():
    altura = float(altura_entry.get())
    peso = float(peso_entry.get())
    imc = peso / (altura ** 2)
    resultado_label.config(text=f"Seu IMC é: {imc:.2f}")

# cria a janela
janela = tk.Tk()
janela.title("Calculadora de IMC")

# cria as labels e entrys
tk.Label(janela, text="Altura (m)").grid(row=0, column=0)
altura_entry = tk.Entry(janela)
altura_entry.grid(row=0, column=1)
tk.Label(janela, text="Peso (kg)").grid(row=1, column=0)
peso_entry = tk.Entry(janela)
peso_entry.grid(row=1, column=1)

# cria o botão para calcular o IMC
calcular_button = tk.Button(janela, text="Calcular IMC", command=calcular_imc)
calcular_button.grid(row=2, column=0)

# cria a label para exibir o resultado
resultado_label = tk.Label(janela)
resultado_label.grid(row=2, column=1)

# inicia o loop principal do Tkinter
janela.mainloop()
