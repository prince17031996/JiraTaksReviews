import openpyxl

class TestData:
    def Links(self):
        workbook = openpyxl.load_workbook("C:\\Users\\PRaj7\\PycharmProjects\\DORUserStory\\Config\\DOR_Check.xlsx")
        sheet = workbook["URL"]
        total_rows = sheet.max_row
        total_colmns = sheet.max_column
        l = []
        for r in range(2, total_rows + 1):
            for c in range(1, total_colmns + 1):
                l.append(sheet.cell(r, c).value)
        return l



obj=TestData()

class TestScriptData:
    def Links(self):
        workbook = openpyxl.load_workbook("C:\\Users\\PRaj7\\PycharmProjects\\DORUserStory\\Config\\script_Check.xlsx")
        sheet = workbook["URL"]
        total_rows = sheet.max_row
        total_colmns = sheet.max_column
        l = []
        for r in range(2, total_rows + 1):
            for c in range(1, total_colmns + 1):
                l.append(sheet.cell(r, c).value)
        return l

class TestDataBug:
    def Links(self):
        workbook = openpyxl.load_workbook("C:\\Users\\PRaj7\\PycharmProjects\\DORUserStory\\Config\\Bug_Check.xlsx")
        sheet = workbook["URL"]
        total_rows = sheet.max_row
        total_colmns = sheet.max_column
        l = []
        for r in range(2, total_rows + 1):
            for c in range(1, total_colmns + 1):
                l.append(sheet.cell(r, c).value)
        return l


