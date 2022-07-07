import pickle
import os
import pandas as pd

#================================================================#
class ExcelTools:
    '''
    Excel tools é um modulo destinado a ler planilhas e gerar dados para posteriormente
    serem inseridos em um banco de dados automaticamente
    '''
    def __init__(self, excel_file, sheet):

        self.excel_file = excel_file
        self.sheet = sheet
        self.data = {}

    def printData(data):
        '''
        Essa funcao nao retorna nada, e apenas uma ferramenta para visualizar os
        dados lidos pela funcao readExcel. Use o retorno da readExcel nessa funcao
        '''



    def readExcel(self): # retorna um dicionario da leitura do excel
        '''
        Esta funcao lê todas as colunas de uma planilha e gera um arquivo
        com os dados formatados prontos para serem inseridos em um banco de dados
        '''
        try:
            plan = pd.read_excel(self.excel_file, self.sheet)
        except Exception as e:
            print(f'Erro:{e}\nProvavelmente o caminho do arquivo excel ou nome da planilha foi/foram escritos errados')
        

        values = []
        data = {}

        for k in plan.keys(): # mapear todas as colunas
            for i in plan[k]: # mapear todas linhas da coluna atual
                values.append(i) # inserir esses dados numa lista temporaria
            data[k] = values[:] # inserir os dados da lista temporaria no dicionario principaç
            values.clear() # limpar dados da lista temporaria
        
        print('Dados lidos:')
        for d in data:
            print(f'{d}: {data[d]}')
        
        # até aqui foram lidos os dados e armazenados em um dicionario
        #======================================#
        # aqui será gerada a sequencia compativel com o metodo insert_many() do peewee (tictac)
        tmp_dict = {}
        tmp_list = []
        key_list = []
        va_list  = []

        idx = 0

        for va in data.values():
            va_list.append(va)

        for ke in data.keys():
            key_list.append(ke)


        for v in range(len(va_list[0])):
            for k in key_list:
                tmp_dict[k] = va_list[idx][v]
                
                idx += 1
            idx = 0
            tmp_list.append(tmp_dict.copy())
            tmp_dict.clear()
        
        return tmp_list

    @staticmethod
    def save_seq(data, outputFile="dados"): # salvar sequencia
        EXT = '.pickle'
        DIR = 'seqs'
        
        if not os.path.exists('seqs'):
            os.mkdir('seqs')
        
        file_ = open(os.path.join(DIR, outputFile+EXT), 'wb')
        try:
            pickle.dump(data, file_)
        except:
            print('Erro ao escrever mudanças.')
        else:
            print('Arquivo salvo com sucesso na pasta "seqs".')

