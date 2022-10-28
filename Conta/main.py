from Conta.models.conta import Conta

conta1 = Conta(1, 'Alex', 1000, 2000)
conta1.saca(200)
conta1.extrato()

print(Conta.codigos_bancos()['Bradesco'])