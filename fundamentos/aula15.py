from abc import ABC, abstractmethod


class AbstractFoo(ABC):
    def __init__(self,nome):
        self._nome = None
        self.nome = nome 

    
    @property
    @abstractmethod
    def nome(self): ...




class Foo(AbstractFoo):
    def __init__(self, nome):
        super().__init__(nome)

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,nome):
        self._nome = nome
        


foo = Foo ('Bar')
print(foo.nome)