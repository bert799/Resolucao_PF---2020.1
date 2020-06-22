def lista_celulares(lista_numeros):
    lista_celphones = []
    for numero in lista_numeros:
        if numero[0] == '+':
            if numero[5] == '9':
                numero = numero[5:]
                lista_celphones.append(numero)
        elif len(numero) <= 11 and len(numero) >= 10:
            if numero[2] == '9':
                numero = numero[2:]
                lista_celphones.append(numero)
        elif len(numero) <= 9 and len(numero) >= 8:
            if numero[0] == '9':
                lista_celphones.append(numero)
    return lista_celphones



