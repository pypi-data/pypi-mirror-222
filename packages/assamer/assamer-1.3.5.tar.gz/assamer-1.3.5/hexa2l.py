from intelhex import IntelHex
from functools import lru_cache
import os
import struct


"""
UBYTE - 1 byte unsigned integer
SBYTE - 1 byte signed integer
UWORD - 2 byte unsigned integer
SWORD - 2 byte signed integer
ULONG - 4 byte unsigned integer
SLONG - 4 byte signed integer
FLOAT32_IEEE - 4 byte (32 bit) floating point IEEE format
FLOAT64_IEEE - 8 byte (64 bit) floating point IEEE format
FLOAT32_TASKING - 4 byte (32 bit) floating point tasking format
"""

class DataType:
    def __init__(self, byte_list):
        self.byte_list = byte_list
    def __repr__(self):
        return str(self.value)
    def __mul__(self, other):
        return [i * other for i in self.value]
    def __add__(self, other):
        return [i + other for i in self.value]
    def __sub__(self, other):
        return [i - other for i in self.value]
    def __truediv__(self, other):
        return [i / other for i in self.value]

class A2LHex:
    def __init__(self, path):
        self.path = path
        self.checkpath()
        self.super = IntelHex()
        self.super.loadhex(self.path)
    def checkpath(self):
        if not self.path.endswith(".hex"):
            raise ValueError(f"{self.path} should be a .hex file")
        if not os.path.exists(self.path):
            raise FileExistsError(f"{self.path} does not exist")
    @property
    def data(self):
        return self.super.todict()
    def readValue(self, address, datatype, shape=1):
        bytesize = shape * datatype.size
        ret = [self.data[address + i] for i in range(bytesize)]
        return datatype(ret)

class ByteSize:
    def __init__(self, size):
        self.size = size

    def __get__(self, instance, owner):
        return self.size

class UBYTE(DataType):
    size = ByteSize(1)
    @property
    def value(self):
        return [byte for byte in self.byte_list]

class SBYTE(DataType):
    size = ByteSize(1)
    @property
    def value(self):
        return [struct.unpack('b', byte.to_bytes(1, 'big', signed=True))[0] for byte in self.byte_list]

class UWORD(DataType):
    size = ByteSize(2)
    @property
    def value(self):
        return [struct.unpack('>H', bytes(self.byte_list[i:i+2]))[0] for i in range(0, len(self.byte_list), 2)]

class SWORD(DataType):
    size = ByteSize(2)
    @property
    def value(self):
        return [struct.unpack('>h', bytes(self.byte_list[i:i+2]))[0] for i in range(0, len(self.byte_list), 2)]

class ULONG(DataType):
    size = ByteSize(4)
    @property
    def value(self):
        return [struct.unpack('>I', bytes(self.byte_list[i:i+4]))[0] for i in range(0, len(self.byte_list), 4)]

class SLONG(DataType):
    size = ByteSize(4)
    @property
    def value(self):
        return [struct.unpack('>i', bytes(self.byte_list[i:i+4]))[0] for i in range(0, len(self.byte_list), 4)]

class FLOAT32_IEEE(DataType):
    size = ByteSize(4)
    @property
    def value(self):
        return [struct.unpack('>f', bytes(self.byte_list[i:i+4]))[0] for i in range(0, len(self.byte_list), 4)]

class FLOAT64_IEEE(DataType):
    size = ByteSize(8)
    @property
    def value(self):
        return [struct.unpack('>d', bytes(self.byte_list[i:i+8]))[0] for i in range(0, len(self.byte_list), 8)]

class FLOAT32_TASKING(DataType):
    size = ByteSize(4)
    @property
    def value(self):
        return [struct.unpack('<f', bytes(self.byte_list[i:i+4]))[0] for i in range(0, len(self.byte_list), 4)]


if __name__ == '__main__':
    path = r'example\blabla.hex'
    h = A2LHex(path)
    h.updateFile()
    h.readValue(0x8040CD34, FLOAT32_IEEE, 5)
    h.readValue(0x8044065E, UWORD,5)
