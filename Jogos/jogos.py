import adivinhacao
import forca

print("\n")
print("Escolha o seu jogo")
print("\n")

print("(1) Adivinhação (2) Forca")

opcao_jogo = int(input("Escolha seu jogo: "))

if (opcao_jogo == 1):
    print("Escolhendo advinhação")
    adivinhacao.jogar_adivinhacao()
elif (opcao_jogo ==2):
    print("Escolhendo forca")
    forca.jogar_forca()

