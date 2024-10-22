#!/bin/env python3

import struct

n = 12.45

fout = open('data.bin','wb')
fout.write(struct.pack('d',n)) # pack allocate 8 bytes
fout.close()

fin = open('data.bin','rb')
# print(struct.unpack('d',fin.read())) returns a tuple
print(struct.unpack('d',fin.read())[0])
fin.close()
