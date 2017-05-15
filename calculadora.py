# !/usr/bin/python

a = 1 + 1

operacao =raw_input("Qual e a operacao? \n 1-adicao 2-subtracao 3-divisao 4-multiplicacao")
print(operacao)

primeiro = int(raw_input("Qual e o primeiro valor?"))

segundo = int(raw_input("Qual e o segundo valor?"))

resultado = 0
op = int(operacao)
if(op == 1):
    resultado = primeiro + segundo    
elif (op == 2):
    resultado = primeiro - segundo
elif (op == 3):
    resultado = primeiro / segundo
elif(op == 4):
    resultado = primeiro * segundo

print(resultado)

