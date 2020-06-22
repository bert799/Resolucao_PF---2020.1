def lista_celulares(num):
    saida = []
    for i in num:
        if len(i) == 14:
            saida.append(i[5:])
        elif len(i) == 11:
            saida.append(i[2:])
        elif len(i) == 9:
            saida.append(i)
        
    return saida

x = ['+5511912345678', '1155556666', '77778888', '+551133334444', '918273645', '11987654321']
print(lista_celulares(x))