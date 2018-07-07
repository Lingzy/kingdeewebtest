import yaml
import os
from xlrd import open_workbook


# Yaml读取类
class YamlReader:
    def __init__(self, yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileNotFoundError('File not exist')
        self._data = None

    @property
    def data(self):
        if not self._data:
            with open(self.yamlf,'rb') as f:
                self._data = list(yaml.safe_load_all(f))
        return self._data


class SheetTypeError(Exception):
    pass


# Excel读取类
class ExcelReader:
    def __init__(self,excel,sheet=0,title_line=True):
        if os.path.exists(excel):
            self.excel = excel
        else:
            raise FileNotFoundError('test data file not exist')
        self.sheet = sheet
        self.title_line = title_line
        self._data = list()

    @property
    def data(self):
        if not self._data:
            workbook = open_workbook(self.excel)
            if type(self.sheet) not in [int,str]:
                raise SheetTypeError('Please pass in <type int> or <type str>,not {}'.format(type(self.sheet)))
            elif type(self.sheet) == int:
                s = workbook.sheet_by_index(self.sheet)
            else:
                s = workbook.sheet_by_name(self.sheet)

            if self.title_line:
                title = s.row_values(0) #首行为title
                for col in range(1, s.nrows):
                    # 依次遍历其余行，与首行组成dict,拼接到self._data中
                    self._data.append(dict(zip(title, s.row_values(col))))
            else:
                for col in range(0,s.nrows):
                    # 遍历所有行，拼接到self._data中
                    self._data.append(s.row_values(col))
        return self._data


if __name__ == '__main__':
    y = 'D:/Project/PythonProject/Autotest/kingdee/kingdeewebtest/webtest/data/test.xlsx'
    reader = ExcelReader(y,title_line=True)
    print(reader.data)