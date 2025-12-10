import sys

try:
  NUMERO = int(sys.argv[1])
except:
  NUMERO = 2

tabellina = [x*NUMERO for x in range(1,11)]

[print(f"{i+1:>2}: {i+1} x {NUMERO} = {n}") for i, n in enumerate(tabellina)]
