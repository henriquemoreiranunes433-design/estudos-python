class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor


    def get_cor (self):
        return self.cor_tinta
    

caneta = Caneta('Preta')
print(caneta.get_cor())
