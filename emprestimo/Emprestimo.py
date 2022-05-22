from datetime import datetime, timedelta

class Emprestimo:
    def __init__(self, pessoa, equipamento, dias):
        self.pessoa = pessoa
        self.equipamnto = equipamento
        
        if(dias):
            d = datetime.today() + timedelta(dias)
            self.data_devolucao = d
        else:
            d = datetime.today() + timedelta(equipamento.tempo_locacao)
            self.data_devolucao = d
    def to_string(self):
        print(f"A pessoa {self.pessoa} alugou o {self.equipamnto} e deverá devolver no dia {self.data_devolucao}")
        