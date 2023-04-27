romano = []
i = 0
digitado = 'XLXVXXIXIVIXVLCDCMCIMD'

digitado = tuple(digitado)

while True:
    i += 0

    if i == len(digitado):
        break
    elif digitado[i] == 'I':
        if i+1 == len(digitado):
            romano.append(digitado[i])
            break
        elif digitado[i] + digitado[i+1] == 'IV':
            j = 'IV'
            romano.append(j)
            i += 2
        elif digitado[i] + digitado[i+1] == 'IX':
            j = 'IX'
            romano.append(j)
            i += 2
        else:
            romano.append(digitado[i])
            i += 1
    elif digitado[i] == 'V':
        romano.append(digitado[i])
        i+=1
    elif digitado[i] == 'X':
        if i + 1 == len(digitado):
            romano.append(digitado[i])
            break
        elif digitado[i] + digitado[i + 1] == 'XL':
            j = 'XL'
            romano.append(j)
            i += 2
        elif digitado[i] + digitado[i + 1] == 'XC':
            j = 'XC'
            romano.append(j)
            i += 2
        else:
            romano.append(digitado[i])
            i += 1
    elif digitado[i] == 'L':
        romano.append(digitado[i])
        i+=1
    elif digitado[i] == 'C':
        if i + 1 == len(digitado):
            romano.append(digitado[i])
            break
        elif digitado[i] + digitado[i + 1] == 'CD':
            j = 'CD'
            romano.append(j)
            i += 2
        elif digitado[i] + digitado[i + 1] == 'CM':
            j = 'CM'
            romano.append(j)
            i += 2
        else:
            romano.append(digitado[i])
            i += 1
    elif digitado[i] == 'D':
        romano.append(digitado[i])
        i+=1
    elif digitado[i] == 'M':
        romano.append(digitado[i])
        i+=1
    else:
        break

print(f'OIII {romano}')