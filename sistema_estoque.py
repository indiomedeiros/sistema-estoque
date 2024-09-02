from lista_produtos import listar_produtos
from alteracao_produtos import alterar_produtos

def executar_sistema_estoque():
    produtos = ["Macarrão", "Arroz", "Feijão"]
    acertou = False
    print("Bem vindo ao Sistema estoque!")
    while(acertou == False):
        try:
            print("\nO que você deseja fazer?")
            print("1 - Listar produtos")
            print("2 - Alterar produto")
            print("3 - Fechar o sistema")
            opcao_escolhida = int(input("Digite o número da opção: "))

            if(opcao_escolhida == 1):
                print("\nLista de produtos:")
                listar_produtos(produtos)

            elif(opcao_escolhida == 2):
                alterar_produtos(produtos)

            elif(opcao_escolhida == 3):
                print("Obrigado por utilizar o Sistema estoque!")
                acertou = True
            else:
                print("Digite uma opção válida.")
             
        except:
            print("\nDigite um número inteiro.")

executar_sistema_estoque()