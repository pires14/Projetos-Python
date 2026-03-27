def jogar_forca():
    print("*******************************")
    print("\nBem vindo ao jogo da forca!\n")
    print("*******************************")

    palavra_secreta = "processador"
    letras_acertadas = ["_","_","_","_","_","_","_","_","_","_","_"]
    perdeu = False
    acertou = False

    #Enquanto não acertar a palavra secreta, o jogador pode jogar.

    while not perdeu and not acertou:
        chute = input("Escreva uma letra: ")
        chute = chute.strip()
        #Strip remove a quebra de linha

        #index define a posição da letra
        index = 0

        for letra in palavra_secreta:
            if chute.lower() == letra.lower():
                letras_acertadas[index] = letra
            index = index + 1
        print(letras_acertadas)

if(__name__ == "__main__"):
    jogar_forca()
