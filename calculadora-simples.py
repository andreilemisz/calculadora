# Calculadora que identifique os números e o operador, faz a conta #
# e retorna um erro caso algum valor seja incorreto ou a divisão seja por zero. #
# No final, deixa o usuario sair ou repetir #
import os
calculadora_ativada = True
numero_1 = 0
numero_2 = 0
numeros_validados = None
operadores_validos = "+-/*"
operador_validado = None
sair = ""
resultado = 0

""" Verificação dos valores iniciais dentro do loop """

while calculadora_ativada:
    while numeros_validados == None:
        numero_1 = input("Digite o primeiro valor: ")
        numero_2 = input("Digite o segundo valor: ")
        try:
            numero_1 = numero_1.replace(",", ".")
            numero_2 = numero_2.replace(",", ".")
            
            numero_1 = float(numero_1)
            numero_2 = float(numero_2)
            numeros_validados = True
            print("Os números inseridos são válidos!")
        except:
            print("Um ou ambos os números digitados não são válidos. Tente novamente!")

    """ Verificação do operador, barrando divisão por 0 """

    while operador_validado == None:
        operador = input("Digite um operador (+-/*): ")
        
        if operador not in operadores_validos or len(operador) != 1:
            print("Você não inseriu um operador válido. Tente novamente.")
        else:
            if operador == "/" and numero_2 == 0:
                print("Você não pode tentar dividir por zero! Tente novamente!")
                numeros_validados = None
                operador_validado = None
                break
            else:
                print("Você inseriu um operador válido!")
                operador_validado = True

        
    """ Operação """
    
    if numeros_validados == True and operador_validado == True:
        resultado = eval(f"{numero_1} {operador} {numero_2}")
        print("O resultado da operação é", resultado)
    else:
        pass

    """ Finalização """

    sair = input("Gostaria de sair do programa? Digite [s]im para sair: ").lower()
    if sair == "s":
        print("Você finalizou o programa.")
        calculadora_ativada = False
        sair = ""
        break
    else:
        numeros_validados = None
        operador_validado = None
        resultado = 0
        os.system("cls")