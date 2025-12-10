import sys

try:
  NUMERO = int(sys.argv[1])
except:
  NUMERO = 2

tabellina = [x*NUMERO for x in range(1,11)]

[print(f"{indice:>2}: {n}") for n, indice in enumerate(tabellina)]
