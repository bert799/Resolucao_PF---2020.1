class Foguete():
    def __init__(self, speed):
        self.speed = speed / 3.6
        self.distance = 0
    def atualizar(self, time):
        self.distance += (self.speed * time)/1000
        return self.distance
