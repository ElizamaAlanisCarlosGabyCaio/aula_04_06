class Produto:
    def __init__(self, preco):
        self.preco = preco  
    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, novo_preco):
        if novo_preco <= 0:
            raise ValueError("O preço deve ser maior que zero.")
        else:
          self._preco = novo_preco
