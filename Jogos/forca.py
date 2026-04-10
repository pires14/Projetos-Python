import random as rd

def  mensagem_inicial():
    print("*******************************")
    print("\nBem vindo ao jogo da forca!\n")
    print("*******************************")

def selec_palavra_aleatoria(): 
    arquivo = open("Jogos/palavras.txt", "r") #R = apenas read (ler) o arquivo
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
                                                         
    arquivo.close()
    posicao = rd.randrange(0,len(palavras))

    palavra_secreta = palavras[posicao].lower()
    return palavra_secreta
    
def letras_corretas(palavra_secreta):
    return ["_" for letra in palavra_secreta]

def entrada_dados():
    chute = input("\nEscreva uma letra: ")
    chute = chute.strip().lower() 
    return chute

def chute_correto(chute, palavra_secreta, letras_acertadas):
    index = 0

    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1
    return letras_acertadas    
def jogar_forca():
    mensagem_inicial()

    palavra_secreta = selec_palavra_aleatoria()
    letras_acertadas = letras_corretas(palavra_secreta)

    # for letra in palavra_secreta:
        #letras_acertadas.append("_")
    
    perdeu = False
    acertou = False
    erros = 0

    while not perdeu and not acertou:
        chute = entrada_dados()

      
        if (chute in palavra_secreta):
            chute_correto(chute, palavra_secreta, letras_acertadas)
        # Se o chute estiver na palavra, preenchemos as posições corretas

        else:
            #Se não estiver, adicionamos APENAS 1 erro nesta rodada: erros = erros + 1
            erros += 1 
        # Verifica se o jogador perdeu
        perdeu = erros == 6

        acertou = "_"not in letras_acertadas
        if acertou:
            print(f'Você acertou a palavra secreta que era {palavra_secreta}')
        print(letras_acertadas)


if(__name__ == "__main__"):
    jogar_forca()