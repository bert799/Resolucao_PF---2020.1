def mais_medalhas(lista):
    medalhas = {}
    count = 0
    for i in range(len(lista)):
        for a, b in lista[i].items():
            if a == 'nacionalidade':
                medalhas[b] = count
            if a == 'ouro' or a == 'prata' or a == 'bronze':
                count += b
    for i, j in medalhas.items():
        if j == max(medalhas.values()):
            return i
   
            





x = [{
    'nome': ' Michael Phelps',
    'nacionalidade': 'Norte Americano',
    'ouro': 23, 'prata': 3, 'bronze': 2,
},
{
    'nome': 'Larisa Latynina',
    'nacionalidade': 'Russo',
    'ouro': 9, 'prata': 5, 'bronze': 4,
},
{
    'nome': 'Nikolai Andrianov',
    'nacionalidade': 'Russo',
    'ouro': 7, 'prata': 5, 'bronze': 3,
},
{
    'nome': 'Boris Shakhlin',
    'nacionalidade': 'Russo',
    'ouro': 7, 'prata': 4, 'bronze': 2,
},
{
    'nome': 'Jenny Thompson',
    'nacionalidade': 'Norte Americano',
    'ouro': 8, 'prata': 3, 'bronze': 1,
}]
print(mais_medalhas(x))