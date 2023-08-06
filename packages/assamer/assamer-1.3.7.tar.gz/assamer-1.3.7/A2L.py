import re
import os
import numpy as np
from functools import lru_cache, cached_property

class ITEMArea:
    _words_regex = re.compile(r"([\w.]+)\s")
    def __init__(self, rawcontent:str):
        self.rawcontent = rawcontent
        self.content = rawcontent.strip()
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    @property
    def contents(self):
        return [i.strip() for i in self.content.strip().split("\n")]
    @property
    def name(self):
        return self._words_regex.findall(self.content)[0]
    @property
    def desc(self):
        return self.contents[1]

"""
TAB_INTP - table with interpolation.
TAB_NOINTP - table without interpolation.
TAB_VERB - verbal conversion table.
RAT_FUNC - fractional rational function f(x)=(axx + bx + c)/(dxx + ex + f), where coefficients 'a' through 'f' are specified properties.
FORM - formula as specified in the Formula property.
"""
class COMPU_METHOD(ITEMArea):
    TabName = "COMPU_METHOD"
    _format_regex = re.compile(r"%[\d+]\.[\d.]", re.DOTALL)
    _coeffs_regex = re.compile(r"COEFFS([\s{+,-}\d+\.\d.e{+,-}\d]+)+")
    @property
    def type(self) -> str:
        return self.contents[2]
    @property
    def format(self) -> str:
        _format = self._format_regex.findall(self.content)
        return _format[0] if len(_format)>0 else ""
    @property
    def unit(self) -> str:
        if self.type == 'RAT_FUNC':
            return self.contents[4]
        return "-"
    @property
    def coeffs(self) -> list[float]:
        coeffs = self._coeffs_regex.findall(self.content)[0].strip().split(" ")
        return list(map(float,coeffs))
    @property
    def referance(self) -> list[str]:
        return re.findall(r"REF\s(.*?)[\n]", self.rawcontent, re.DOTALL)
    def calculate(self, x):
        if self.type == 'RAT_FUNC':
            return np.polyval(self.coeffs[:3], x) / np.polyval(self.coeffs[3:], x)
        elif self.type == 'TAB_VERB':
            if x in self.compu_vtab:
                return self.compu_vtab[x]
            else:
                return x
        elif self.type == 'FORM':
            # Implement the logic for FORM conversion
            # Example: If the formula is "X1+4", you can evaluate it as:
            return eval(self.formula.replace("X1", str(x)))
        elif self.type == 'TAB_INTP':
            # Implement the logic for TAB_INTP conversion
            # Example: Assuming the COMPU_TAB_REF is defined and contains input-output value pairs, you can interpolate the output value based on the input value
            return interpolate(x, self.compu_tab_ref)
        elif self.type == 'TAB_NOINTP':
            # Implement the logic for TAB_NOINTP conversion
            # Example: Assuming the COMPU_TAB_REF is defined and contains input-output value pairs, you can find the closest matching output value based on the input value
            return find_closest_value(x, self.compu_tab_ref)
        else:
            return x

class RECORD_LAYOUT(ITEMArea):
    TabName = "RECORD_LAYOUT"
    _values_regex = re.compile(r"VALUES\s*(\d*)\s(\w*)\s(\w*)\s(\w*)")
    @property
    def subContent(self) -> list:
        return self._values_regex.findall(self.content)
    @property
    def unit(self) -> ITEMArea:
        return self.subContent[0][1]
    
class AXIS_DESCR(ITEMArea):
    TabName = "AXIS_DESCR"
    _format_regex = re.compile(r"%[\d+]\.[\d.]", re.DOTALL)
    @property
    def compuMethod(self):
        return self.contents[2]
    @property
    def shape(self):
        return int(self.contents[3])
    @property
    def minimum(self):
        return self.contents[4]
    @property
    def maximum(self):
        return self.contents[5]
    @property
    def format(self):
        _format = self._format_regex.findall(self.content)
        return _format[0] if len(_format)>0 else ""
    @property
    def deposit(self):
        return "DEPOSIT ABSOLUTE" in self.rawcontent

class FUNCTION(ITEMArea):
    TabName = "FUNCTION"
    _characteristic_regex = re.compile(f"/begin\s+DEF_CHARACTERISTIC(.*?)/end\s+DEF_CHARACTERISTIC", re.DOTALL)
    _in_measurement_regex = re.compile(f"/begin\s+IN_MEASUREMENT(.*?)/end\s+IN_MEASUREMENT", re.DOTALL)
    _out_measurement_regex = re.compile(f"/begin\s+OUT_MEASUREMENT(.*?)/end\s+OUT_MEASUREMENT", re.DOTALL)
    _sub_function_regex = re.compile(f"/begin\s+SUB_FUNCTION(.*?)/end\s+SUB_FUNCTION", re.DOTALL)
    @cached_property
    def DEF_CHARACTERISTIC(self):
        cont = None
        _ = [cont := i for i in self._characteristic_regex.findall(self.content)]
        if cont:
            return self._words_regex.findall(cont)
        return []
    @cached_property
    def IN_MEASUREMENT(self):
        cont = None
        _ = [cont := i for i in self._in_measurement_regex.findall(self.content)]
        if cont:
            return self._words_regex.findall(cont)
        return []
    @cached_property
    def OUT_MEASUREMENT(self):
        cont = None
        _ = [cont := i for i in self._out_measurement_regex.findall(self.content)]
        if cont:
            return self._words_regex.findall(cont)
        return []
    @cached_property
    def SUB_FUNCTION(self):
        cont = None
        _ = [cont := i for i in self._sub_function_regex.findall(self.content)]
        if cont:
            return self._words_regex.findall(cont)
        return []

class CHARACTERISTIC(ITEMArea):
    TabName = "CHARACTERISTIC"
    _format_regex = re.compile(r"%[\d+]\.[\d.]", re.DOTALL)
    _matrix_dim_regex = re.compile(r"MATRIX_DIM\s([\d\s+]+)", re.DOTALL)
    _number_regex = re.compile(r"NUMBER (\d+)", re.DOTALL)
    _axis_regex = re.compile(r"/begin AXIS_DESCR(.*?)/end AXIS_DESCR", re.DOTALL)
    @property
    def type(self):
        return self.contents[2]
    @property
    def address(self):
        address = int(self.contents[3],16)
        for axis in self.axisInfo:
            if axis.deposit:
                address += axis.shape + 1
        return address
    @property
    def recorder(self):
        return self.contents[4]
    @property
    def maximum(self):
        return self.contents[8]
    @property
    def minimum(self):
        return self.contents[7]
    @property
    def compuMethod(self):
        return self.contents[6]
    @property
    def format(self):
        _format = self._format_regex.findall(self.content)
        return _format[0] if len(_format)>0 else ""
    @property
    def shape(self):
        if self.type == 'VALUE':
            return [1]
        if len(self.axisInfo) != 0:
            return [axis.shape for axis in self.axisInfo]
        if 'MATRIX_DIM' in self.content:
            return self._matrix_dim_regex.findall(self.content)[0].split(" ")
        if 'NUMBER' in self.content:
            return self._number_regex.findall(self.content)
    @property
    def axisInfo(self):
        if self.type == 'VALUE':
            return []
        axises = self._axis_regex.findall(self.content)
        return [AXIS_DESCR(content) for content in axises]

class A2L:
    def __init__(self, path):
        self.path = path
        self.checkpath()
        self.parsedData = {}
        self.hexobj = None
    def checkpath(self) -> bool:
        if not self.path.endswith(".a2l"):
            raise ValueError(f"{self.path} should be a .a2l file")
        if not os.path.exists(self.path):
            raise FileExistsError(f"{self.path} is not exists")
        with open(self.path, 'r') as f:
            for _ in range(10):
                if 'ASAP2' in f.readline():
                    break
            else:
                raise TypeError("The File is not in ASAP2 Format")
        return True
    @property
    @lru_cache
    def data(self):
        with open(self.path, 'r') as f:
            data = f.read()
        return data
    @lru_cache
    def getArea(self, itemType: ITEMArea) -> str:
        if itemType in self.parsedData.keys():
            return self.parsedData[itemType]
        areaName = itemType.TabName
        contents = re.findall(f"/begin\s+{areaName}(.*?)/end\s+{areaName}", self.data, re.DOTALL)
        self.parsedData[itemType] = [itemType(content) for content in contents]
        return self.parsedData[itemType]

if __name__ == '__main__':
    path = r'example\ASAP2_Demo_V161.a2l'
    a2l = A2L(path)
    funcs = a2l.getArea(FUNCTION)
