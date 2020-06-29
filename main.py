def computador_escolhe_jogada(n,m):
    if n<=m:
        print(f"O computador tirou {n} peças.")
        return n
    elif m==1:
        return m
    else:
        c=n % (m + 1)
        if c > 0:
            print(f"O computador tirou {c} peças.")
            return c
        else:
            print(f"O computador tirou {m} peças.")
            return m

def usuario_escolhe_jogada(n,m):
    print(f"Quantas pecas voce vai tirar?")
    pecas_usuario=int(input())
    if pecas_usuario<=m and pecas_usuario>0 and pecas_usuario<=n:
        u=pecas_usuario
        print(f"Voce tirou {u} peças.")
        return u
    else:
        while True:
            print("Oops! Jogada invalida! Tente de novo.")
            pecas_usuario=int(input())
            if pecas_usuario <= m and pecas_usuario>0:
                u = pecas_usuario
                print(f"Voce tirou {u} peças.")
                False
                return u

def partida():
    n=int(input("Quantas pecas? "))
    m=int(input("Limite de pecas por jogada? "))
    is_computer_turn = True
    if n%(m+1)==0:
        print("Você começa")
        is_computer_turn = False
    else:
        print("Computador começa")
        is_computer_turn = True
    while n > 0:
        if is_computer_turn:
            jogada = computador_escolhe_jogada(n, m)
            n = n - jogada
            is_computer_turn = False
        else:
            jogada =usuario_escolhe_jogada(n, m)
            n =n-jogada
            is_computer_turn = True
        if n>0:
            print(f"Agora restam {n} peças.")
    if is_computer_turn == True:
        resultado="Fim do jogo! Você ganhou!"
        placar=1
        print("Fim do jogo! Você ganhou!")
        return resultado
    else:
        resultado="Fim do jogo! O computador ganhou!"
        placar = 0
        print("Fim do jogo! O computador ganhou!")
        return resultado

def campeonato():
    usuario = 0
    computador = 0
    for _ in range(3):
        vencedor = partida()
        if vencedor == "Fim do jogo! Você ganhou!":
            usuario = usuario + 1
        else:
            computador = computador + 1
    print("Placar final: Você  {} x {}  Computador".format(usuario, computador))


print("Bem-vindo ao jogo do NIM! Escolha:","1 - para jogar uma partida isolada","2 - para jogar um campeonato", sep="\n")
jogo_ou_campeonato=int(input())
while jogo_ou_campeonato!=1 or jogo_ou_campeonato!=2:
    if jogo_ou_campeonato==1:
        print("Voce escolheu uma partida isolada")
        break
    elif jogo_ou_campeonato==2:
        print("Voce escolheu um campeonato!")
        break
    else:
        print("Por favor escolha 1 ou 2")
        jogo_ou_campeonato=int(input())
