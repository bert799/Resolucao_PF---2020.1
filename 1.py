with open('criptografado.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()
    for i in conteudo:
        i = i.strip()
        letra = [char for char in i]
        for e in range(len(letra)): 
            if letra[e] == 's':
                letra[e] = 'z'
            elif letra[e] == 'a':
                letra[e] = 'e'
            elif letra[e] == 'r':
                letra[e] = 'b'
            elif letra[e] == 'b':
                letra[e] = 'r'
            elif letra[e] == 'e':
                letra[e] = 'a'
            elif letra[e] == 'z':
                letra[e] = 's'
        new = ''.join(letra)
        print(new)
    
    
