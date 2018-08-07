import os
import pandas as pd
from openpyxl import load_workbook

class MyUtils:
    def __init__(self):
        self.name = 'myUnits'

    def mkdir(self,path):
        # 去除首位空格
        path = path.strip()
        # 去除尾部 \ 符号
        path = path.rstrip("\\")
        # 判断路径是否存在
        isExists = os.path.exists(path)
        # 判断结果
        if not isExists:
            os.makedirs(path)
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            return False

    def checkFileName(self,filename):
        invalidCharacter = ['\\', '/', ':', '*', '?', '"', '>', '<', '|']
        for cha in invalidCharacter:
            if cha in filename:
                filename = filename.replace(cha, '')
        return filename

    def creatBlankExcel(self,filePath):
        isExists = os.path.exists(filePath)
        if not isExists:
            writer = pd.ExcelWriter(filePath)
            pd.DataFrame().to_excel(writer, 'default')
            writer.save()
            return True
        else:
            return False

    def getExcelWriter(self, pageListFilePath):
        return pd.ExcelWriter(pageListFilePath,engine='openpyxl')

    # excel中新增sheet表
    def excelAddSheet(self, excelWriter, dataframe, sheet_name):
        book = load_workbook(excelWriter.path)
        excelWriter.book = book
        dataframe.to_excel(excel_writer=excelWriter, sheet_name=sheet_name, index=None)
        excelWriter.close()

    def getDataFromExcel(self, path, sheetName):
        rsDF = None
        isExists = os.path.exists(path)
        if isExists:
            rsDF = pd.read_excel(path, sheetName)
        return rsDF
    
    def DF2TXT(self, DF,TXT,seq):
        file = open(TXT, "a",encoding='utf8')  ## "w"表示重新写
        file.write(seq.join(DF.columns)+'\n')
        for i in range(DF.shape[0]):
            line = seq.join(list(DF.iloc[i,:]))
            file.write(line+'\n')
        file.close()
        
    def TXT2DF(self, TXT,seq):
        f = open(TXT,encoding='utf8')
        DF = pd.read_table(f,sep='|')
        f.close()
        return DF