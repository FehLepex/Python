import tkinter as tk

def clique_no_botao():
    valor1=campo_de_entrada1.get()
    valor2=campo_de_entrada2.get()
    
    try:
        n1= int(valor1)
        n2= int(valor2)
        resultado = n1 + n2
    
        label.config(text=f"Adeus, Mundo! {resultado}")
    except ValueError:
        label.config(text="coloca os numero certo senhor INTEIROS")



janela = tk.Tk()
janela.title("Minha tela em Python")
janela.geometry("800x400")
janela.configure(bg= "black")

label = tk.Label(janela,text="Olá, Mundo!")
label.pack()    

campo_de_entrada1=tk.Entry(janela)
campo_de_entrada2=tk.Entry(janela)
campo_de_entrada1.pack()
campo_de_entrada2.pack()

botao = tk.Button(janela,text="Clique aqui", command=clique_no_botao)
botao.pack()

janela.mainloop()