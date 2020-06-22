class Foguete:
    def __init__(self, speed):
        self.speed = speed
        self.list = []
    
    def atualizar(self, tempo):
        self.tempo = tempo/(3600)
        x = self.tempo * self.speed
        self.list.append(x)
        return sum(self.list)

foguete = Foguete(10000)
print(foguete.atualizar(9))
print(foguete.atualizar(18))
