from main.create import Processador, Placa_mae, Memoria

new_price = 400
placa     = Placa_mae.get(Placa_mae.modelo == 'a320m')
#placa.preco = new_price


placa.preco = new_price
placa.save()

print(placa.preco)
