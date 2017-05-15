import psycopg2

con = psycopg2.connect("host=localhost dbname=projeto user=admin password=4linux")


"""
Toda interacao com base de dados e feita via cursores
"""
cur = con.cursor()


"""
Toda execucao de instrucao e feita via metodo execute()
"""


try:
    cur.execute("insert into tabela(id, valor) values (5,'bla')")
    con.commit()
    print("Insercao feita com sucesso")

except Exception as e:
    print("Erro na insercao de dados")
    con.rollback()

cur.close()
con.close()


"""
Como fazer consultas no postgres
"""
cons = con.cursor()




"""
Para evitar SQL-INJECTION, o postgres so recebe strings delimitadas por '' 
"""

"""
Para deixar um campo auto-increment, necessario defini-lo como serial no banco de dados
"""


