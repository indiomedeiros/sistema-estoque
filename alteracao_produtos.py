def alterar_produtos(lista):
    
    acertou = False
    while (acertou == False):
        indice = int(input("Qual o indice do produto? "))
        comprimento_lista = len(lista)

        if(indice >= comprimento_lista or indice < 0):
            print("Esse indice não existe. Verifique a lista.")
        else:
          novo_produto = input("QUal nome do novo produto?")

          for i in range(comprimento_lista):
              if(indice == i):
                  lista[i] = novo_produto
          acertou = True


