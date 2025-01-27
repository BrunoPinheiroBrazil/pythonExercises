
def calculadora():
operação=input('''
 selecione uma operação matematica
 + para soma 
 - para diminuir
 / para dividir
 * para multiplica.
     ''')
numero_1=int(input("escolha o primeiro numero:  "  ))
numero_2=int(input("escolha o segundo numero:  "))
if operação=='+':
  print("{}+{}=". format(numero_1,numero_2))
  print(numero_1+numero_2)
if operação=="-":
    print("{}-{}=". format(numero_1,numero_2))
    print(numero_1-numero_2)
if operação=="/":
    print("{}/{}=".format(numero_1,numero_2))
    print(numero_1/numero_2)
if operação=="*":
    print("{}*{}=". format(numero_1,numero_2))
    print(numero_1*numero_2)