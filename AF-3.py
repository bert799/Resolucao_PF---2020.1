def calcula_dano(atributos):
    forca_total = 0
    forca_total += atributos['força']
    if atributos['equipamentos']:
        for equipamento in atributos['equipamentos']:
            forca_total += equipamento['força']
    return forca_total