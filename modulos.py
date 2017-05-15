# !/usr/bin/python

# modulos externos
"""
Instalacao de modulos externos e feito via easy_install e pip.

pipreqs -- Pacote que permite visualizar quais sao os pacotes utilizados em determinado projeto.
"""

from wget import download


try:
    
    download("http://www.bol.com.br")
except Exception as e:
    print(e)


