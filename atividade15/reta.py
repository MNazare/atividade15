# Exercício Python 15: Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo. 
#DICA: PESQUISE E ENTENDA SOBRE DESIGUALDADE TRIANGULAR

reta1 = float(input("comprimento da reta1: "))
reat2 = float(input("comprimento da reta2: "))
reta3 = float(input("comprimento da reta3: "))

if reta1 + reat2 < reta3:
    print("com estas retas podesse formas um triângulo ")
else:
    print("não é possivel fromar um triângulo com estas retas")