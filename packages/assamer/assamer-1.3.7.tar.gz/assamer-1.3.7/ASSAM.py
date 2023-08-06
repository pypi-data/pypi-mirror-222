from A2L import *
from hexa2l import *
from warnings import warn
from functools import lru_cache
import numpy as np

class ASSAM:
    _instance = None

    def __new__(cls, **kwargs):
        if cls._instance:
            warn(f"{cls} was already defined as {cls._instance}")
        cls._instance = cls
        return super().__new__(cls)

    def __init__(self, **kwargs):
        self.a2l = None
        self.hex = None
        if "A2LPath" in kwargs:
            self.readA2LFile(kwargs["A2LPath"])
        elif "A2L_Object" in kwargs:
            self.readA2LObject(kwargs["A2L_Object"])
        else:
            raise ValueError("You need to define A2L as \"A2LPath\" or \"A2L_Object\"")

        if "HEXPath" in kwargs:
            self.readHEXFile(kwargs["HEXPath"])
        elif "HEX_Object" in kwargs:
            self.readHEXObject(kwargs["HEX_Object"])
        else:
            raise ValueError("You need to define HEX as \"HEXPath\" or \"HEX_Object\"")

    def readA2LFile(self, a2lpath):
        self.a2l = A2L(a2lpath)

    def readA2LObject(self, a2lobject):
        self.a2l = a2lobject

    def readHEXFile(self, hexpath):
        self.hex = A2LHex(hexpath)

    def readHEXObject(self, hexobject):
        self.hex = hexobject

    @property
    def hexState(self):
        self.hex.updateFile()
        return True

    @lru_cache
    def searchCal(self, name):
        listofCHARA = self.a2l.getArea(CHARACTERISTIC)
        names = [cal.name for cal in listofCHARA]

    @lru_cache
    def readValue(self, name):
        if not self.hexState or not self.hex:
            raise ValueError("You need to \"AssignHex ( HexObject )\"")

        cal = [cal for cal in self.a2l.getArea(CHARACTERISTIC) if name in cal.name]
        if not cal:
            return -1

        cal = cal[0]
        compuMethod = [cm for cm in self.a2l.getArea(COMPU_METHOD) if cal.compuMethod == cm.name][0]
        recorder = [rec for rec in self.a2l.getArea(RECORD_LAYOUT) if cal.recorder == rec.name][0]

        size = 1
        for i in cal.shape:
            size *= int(i)

        buf = self.hex.readValue(cal.address, eval(recorder.unit), size)
        buf = np.array(compuMethod.calculate(buf.value)).reshape(cal.shape)

        return {"CHARACTERISTIC": cal, "COMPU_METHOD": compuMethod, "RECORD_LAYOUT": recorder, "Value": buf}

if __name__ == '__main__':
    a2lpath = 'patha2l.a2l'
    hexpath = 'hexa2lpath.hex'
    assam = ASSAM(A2LPath=a2lpath, HEXPath=hexpath)
    print(assam.readValue("aCharacteristicName"))
