def mais_medalhas (dic_atletas):
    paises_ouros = {}
    mais_ouros = 0
    for atleta in dic_atletas:
        nacionalidade = atleta['nacionalidade']
        medalha_ouro = atleta['ouro']
        if nacionalidade in paises_ouros:
            paises_ouros[nacionalidade] += medalha_ouro
        else:
            paises_ouros[nacionalidade] = medalha_ouro
    for pais, num_ouro in paises_ouros.items():
        if num_ouro > mais_ouros:
            mais_ouros = num_ouro
            pais_dourado = pais
    return pais_dourado