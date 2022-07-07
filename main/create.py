import peewee as pw
import os
'''
if not os.path.exists('database.db'):
    a = open('main/database.db', 'wb')
    a.close()
'''
db = pw.SqliteDatabase('main/database.db')


class BaseModel(pw.Model):
    class Meta:
        database = db

class Processador(BaseModel):
    marca = pw.CharField(5)
    modelo = pw.CharField(20)
    nucleos = pw.IntegerField()
    clock = pw.FloatField()
    preco = pw.FloatField()
    #id = pw.IntegerField(unique=True) ID tirado devido ao erro not Null constraint error

class Memoria(BaseModel):
    marca = pw.CharField(10)
    tecnologia = pw.CharField(4)
    clock = pw.FloatField()
    capacidade = pw.IntegerField()
    preco = pw.FloatField()
    #id = pw.AutoField(unique=True) ID tirado devido ao erro not Null constraint error

class Placa_mae(BaseModel):
    marca = pw.CharField(15)
    chipset = pw.CharField(10)
    modelo = pw.CharField(30)
    tamanho = pw.CharField(5)
    marca_cpu = pw.CharField(5)
    preco = pw.FloatField()
    #id = pw.AutoField(unique=True) ID tirado devido ao erro not Null constraint error


if __name__ == '__main__':
    try:
        Processador.create_table()
        print('Tabela Processador criada com exito.')
    except pw.OperationalError:
        print('Tabela Processador ja existe.')
    
    try:
        Memoria.create_table()
        print('Tabela Memoria criada com exito.')
    except pw.OperationalError:
        print('Tabela Memoria ja existe.')
    
    try:
        Placa_mae.create_table()
        print('Tabela Placa_Mae criada com exito.')
    except pw.OperationalError:
        print('Tabela Memoria ja existe.')