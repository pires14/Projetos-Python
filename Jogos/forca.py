def jogar_forca():
    
    print("*******************************")
    print("\nBem vindo ao jogo da forca!\n")
    print("*******************************")

    arquivo = open("Jogos/palavras.txt", "r") #R = apenas read (ler) o arquivo
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
                                                         
    arquivo.close()

    palavra_secreta = "processador"
    letras_acertadas = ["_" for letra in palavra_secreta]

    # for letra in palavra_secreta:
        #letras_acertadas.append("_")
    
    perdeu = False
    acertou = False
    erros = 0

    #Enquanto não acertar a palavra secreta e não perder, o jogador pode jogar.
    while not perdeu and not acertou:
        chute = input("\nEscreva uma letra: ")
        chute = chute.strip().lower() 

        # Se o chute estiver na palavra, preenchemos as posições corretas
        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            #Se não estiver, adicionamos APENAS 1 erro nesta rodada
            erros += 1 
        # Verifica se o jogador perdeu
        perdeu = erros == 6

        acertou = "_"not in letras_acertadas
        if acertou:
            print(f'Você acertou a palavra secreta que era {palavra_secreta}')
        print(letras_acertadas)


if(__name__ == "__main__"):
    jogar_forca()