tabellina = [x*2 for x in range(1,11)]
output = "Hello World! Hello World! Hello World!"
[print(f"{n:>2}: {output[:n]}") for n in tabellina]
