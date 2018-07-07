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


# Excel读取类
class ExcelReader:
    def __init__(self,excel,sheet=0,title_line=True):