import random as rd

def jogar_adivinhacao():
    print("\n ")
    print("\n Bem vindo ao jogo de adivinhação!")
    print("\n ")

    #Declaração de variáveis
    n_secreto = rd.randrange(1,11)
    tentativas = 0
    rodada = 1
    pontuacao = 1000

    print("Níveis de dificuldade")
    print("\n(1) Fácil (2) Médio 3(Difícil) 4(Aleatório)\n")
    nivel = int(input("Por favor, selecione um nível: "))

    if(nivel == 1):
        tentativas = 12
    elif(nivel == 2):
        tentativas = 8
    elif(nivel == 3):
        tentativas = 5
    else:
        tentativas = rd.randrange(1,13)
    for rodada in range(1,tentativas +1): 
        print(f"Tentativa {rodada} de {tentativas}")
        entrada = int(input("Digite um número de 1 a 10: "))  
        if (entrada >  100 or entrada < 1): 
            print("VOCÊ NÃO SABE LER???? O valor digitado não é permitido")
            continue
        acerto = entrada ==  n_secreto
        numero_maior = entrada > n_secreto
        numero_menor = entrada < n_secreto

        #Digitar o número
        print(f"Você digitou o número: {entrada}")
        print("\n")

        #Condicional de acerto ou erro
        if (acerto):
            print("PARABÉNS!!!! Você acertou o número secreto")
            print(f'PARABÉNS!! (ou não). Você fez {pontuacao} pontos')
            break
        else:
            if(numero_maior):
                print("O número digitado foi MAIOR do que o número secreto")
            if(numero_menor):                                           
                print("O número digitado foi MENOR do que o número secreto")
        pontuacao_perdida = abs(n_secreto - entrada)
        pontuacao = pontuacao - pontuacao_perdida
        rodada = rodada + 1

    print("\n")
    print("GAME OVER!!!")