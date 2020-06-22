def calcula_dano(player):
    dano = 0
    for a, b in player.items():
        if a == 'força':
            dano += b
        if a == 'equipamentos':
            for i in player['equipamentos']:
                for x, y in i.items():
                    if x == 'força':
                        dano += y
        
    return dano



x = {'nome': 'Herói', 'força': 4, 'vida': 25, 'equipamentos':[{'nome': 'Martelo Mortal', 'força': 15}, {'nome': 'Luva Leve', 'força': 2}]}
print(calcula_dano(x))