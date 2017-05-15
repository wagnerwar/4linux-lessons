# !/usr/bin/python
def  vixi():
    global treta
    oi.append("quatro")
    treta = "muita treta"

oi = ["um", "dois", "tres"]
treta = "treta"
print(treta)
print(oi)

vixi()
print(oi)
print(treta)

# Observe que, voce precisa definir uma variavel como global, para alterar o mesmo dentro da funcao, com excecao da variavel do tipo "lista"

def argumentos(*args):
    print(args)

argumentos("2","3", 1, 2)

def kargumentos(**kw):
    print(kw)
    print(kw["nome"])

kargumentos(nome="wawa", valor=2)


# LAMBDA
var = lambda x: x*2
print var(2)
