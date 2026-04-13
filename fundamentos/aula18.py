class Ponto:
    def __init__(self,x ,y):
        self.x = x
        self.y = y

    
    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}(x={self.x}, y={self.y})'


p1 = Ponto(1, 20)
p2 = Ponto(10, 20)
print(p1)
print(p2)