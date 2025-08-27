# 1.  Crie um programa que aceite pedidos de um e-commerce até que o cliente digite sair.
print("Faça seu pedido ou digite 'sair' para encerrar: ")
pedido = "" # String pq 'sair' é um texto.
lista = ["smartphone", "smarttv", "geladeira", "videogame", "fogão", "relógio", "notebook"]

while pedido.lower() != 'sair': 
    pedido = input("Digite um produto da lista: ")
    if pedido in lista:
        print(f"{pedido}.capitalize adicionado ao seu carrinho")
    elif pedido.lower() == "sair":
        print("Pedido encerrado")
    else:
        print("Esse produto não está disponível. Escolha outro")