from itertools import count

contador = count(start = 1)

for v in contador:
    print(v)

    if v >= 10:
        break