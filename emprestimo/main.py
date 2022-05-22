from Equipamento import Equipamento
from Pessoa import Pessoa
from Emprestimo import Emprestimo

equipamentos = []

equipamentos.append(Equipamento("Lança foguete", 30))
equipamentos.append(Equipamento("M1 Abrams", 60))
equipamentos.append(Equipamento("Little Bid", 10))

douglas = Pessoa("Douglas")
geri = Pessoa("Xeri Natalio Tutra")
anderson = Pessoa("Andinho")

emprestimos = []

emprestimos.append(Emprestimo(douglas.nome_pessoa, equipamentos[1],100))
emprestimos.append(Emprestimo(geri.nome_pessoa, equipamentos[2], 365))

for emprestimo in emprestimos:
    emprestimo.to_string()