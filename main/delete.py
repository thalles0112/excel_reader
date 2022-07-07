from main.create import Placa_mae

placa = Placa_mae.get(Placa_mae.modelo == 'a320m')
placa.delete_instance()

