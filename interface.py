import tkinter as tk
from calculadora import Calculadora # Lembra de ter o arquivo calculadora.py na mesma pasta!

def calcular(operacao):
    try:
        n1 = float(entrada_num1.get())
        n2 = float(entrada_num2.get())
    except ValueError:
        label_resultado.config(text="Erro: Digite apenas números!", fg="red")
        return

    calc = Calculadora(n1, n2)

    if operacao == '+':
        res = calc.somar()
    elif operacao == '-':
        res = calc.subtrair()
    elif operacao == '*':
        res = calc.multiplicar()
    elif operacao == '/':
        res = calc.dividir()

    label_resultado.config(text=f"Resultado: {res}", fg="blue")

# --- Configuração da Janela ---
janela = tk.Tk()
janela.title("Calculadora Simples")
janela.geometry("320x250")
janela.config(padx=20, pady=20) # Dá um respiro nas bordas da janela toda

# --- Linha 0: Título ---
# columnspan=2 significa que o título vai ocupar o espaço de duas colunas
titulo = tk.Label(janela, text="Calculadora Python", font=("Arial", 14, "bold"))
titulo.grid(row=0, column=0, columnspan=2, pady=(0, 15)) 

# --- Linha 1: Primeiro Número ---
tk.Label(janela, text="Número 1:", font=("Arial", 10)).grid(row=1, column=0, sticky="e")
entrada_num1 = tk.Entry(janela, width=15, font=("Arial", 10))
entrada_num1.grid(row=1, column=1, pady=5)

# --- Linha 2: Segundo Número ---
# sticky="e" alinha o texto à direita (East/Leste)
tk.Label(janela, text="Número 2:", font=("Arial", 10)).grid(row=2, column=0, sticky="e")
entrada_num2 = tk.Entry(janela, width=15, font=("Arial", 10))
entrada_num2.grid(row=2, column=1, pady=5)

# --- Criando um "Frame" (uma caixa invisível) só para os botões ---
# Isso ajuda a organizar os botões juntos na Linha 3
frame_botoes = tk.Frame(janela)
frame_botoes.grid(row=3, column=0, columnspan=2, pady=15)

# Colocando os botões dentro do frame (lado a lado)
tk.Button(frame_botoes, text="+", width=5, bg="#d9d9d9", command=lambda: calcular('+')).grid(row=0, column=0, padx=3)
tk.Button(frame_botoes, text="-", width=5, bg="#d9d9d9", command=lambda: calcular('-')).grid(row=0, column=1, padx=3)
tk.Button(frame_botoes, text="*", width=5, bg="#d9d9d9", command=lambda: calcular('*')).grid(row=0, column=2, padx=3)
tk.Button(frame_botoes, text="/", width=5, bg="#d9d9d9", command=lambda: calcular('/')).grid(row=0, column=3, padx=3)

# --- Linha 4: O Resultado ---
label_resultado = tk.Label(janela, text="Resultado aparecerá aqui", font=("Arial", 11, "bold"))
label_resultado.grid(row=4, column=0, columnspan=2, pady=10)

janela.mainloop()