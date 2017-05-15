# !/usr/bin/python

animais =  ["gato","cachorro", "passarinho"]
print(animais)
animais.append("boi")
print(animais)
animais.insert(2,"lagarto")
print(animais)
animais.remove("gato")
print(animais)
animais.pop()
print(animais)
animais.pop(1)
print(animais)
print(animais.count("ppp"))

print(animais.index("passarinho"))

animais.reverse()
print(animais)
