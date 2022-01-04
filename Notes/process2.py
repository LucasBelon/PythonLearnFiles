def main():
    class FixedFloat:
        def __init__(self, amount):
            self.amount = amount

        def __repr__(self):
            return f'<FixedFloat {self.amount:.2f}>'

        @classmethod
        def from_sum(cls, value1, value2):
            return cls(value1 + value2)

    '''
    PELO JEITO ESSE CLASSMETHOD FAZ COM QUE POSSAMOS ACESSAR
    TUDO DA CLASSE COMO SE FOSSEM PARÂMETROS DE UMA FUNÇÃO
    numero = FixedFloat.from_sum(123.113,132453.5643)
    print(numero)
    #print(type(numero))
    '''

    class Libra(FixedFloat):
        # Aqui temos um caso de herança de classe
        def __init__(self, amount):
            super().__init__(amount)
            # Usamos o super pra acessar características da superclasse
            # Puxamos tudo que tinha dentro do FixedFloat
            # e colocamos no init do Libra
            # ACHO que sobrescrevemos o __repr__ logo abaixo
            self.symbol = '£'

        def __repr__(self):
            return f'<Libra {self.symbol}{self.amount:.2f}>'

    money = Libra.from_sum(15.234, 12.4212)
    print(money)
