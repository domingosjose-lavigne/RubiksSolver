import re

movimentos = "R U2 F' L B2 D' R' F2"

# Expressão regular:
# ([RUF LDB])  → captura uma letra válida
# (['2]?)       → captura opcionalmente ' ou 2
pattern = r"[RUFLDB]['2]?"

resultado = re.findall(pattern, movimentos)
print(resultado)
print(type(resultado))
