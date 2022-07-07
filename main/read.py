from main.create import Processador, Placa_mae, Memoria

Single_mode = True

mobo = Placa_mae.get(Placa_mae.modelo == "B550F")
print(f'preço da {mobo.modelo}: R$ {mobo.preco}')


cpus = Processador.select()
mobo = Placa_mae.select()
Memo = Memoria.select()


for cpu in cpus:
    print(cpu.modelo)


