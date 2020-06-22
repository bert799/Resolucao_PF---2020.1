with open('criptografado.txt', 'r') as enigma:
    conteudo = enigma.readlines()
    for linha in conteudo:
        cracked = linha.replace('s', 'Z')
        cracked = cracked.replace('a', 'E')
        cracked = cracked.replace('r', 'B')
        cracked = cracked.replace('b', 'R')
        cracked = cracked.replace('e', 'A')
        cracked = cracked.replace('z', 'S')
        print(cracked.lower())
        
