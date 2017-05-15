from datetime import datetime, timedelta
from datetime import date

agora = datetime.now()
# timedelta (adicionar ou retira dias)
print(agora + timedelta(7))

print(agora - timedelta(7))


print(date.today() + timedelta(1))

print(agora.date())

# Exemplo de validacao de tokens

