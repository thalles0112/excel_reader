from utils import ExcelTools


tool = ExcelTools('dados.xlsx', 'memoria')

tool.save_seq(tool.readExcel(), 'dados_exemplo')