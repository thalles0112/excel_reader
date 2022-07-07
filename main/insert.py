import pickle
from main.create import Processador, Memoria, Placa_mae
import pickle


FILE = 'placa_mae' # CAMINHO DO ARQUIVO GERADO PELO LEITOR DE EXCEL
TABELA = Memoria # escreva aqui a classe da tabela que foi importada



a = open(f'seqs/{FILE}.pickle', 'rb')
dados = pickle.load(a)

TABELA.insert_many(dados).execute()
