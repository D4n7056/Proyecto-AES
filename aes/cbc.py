#=================#
#       CBC       #
#=================#

from aes.options import encryptBlock, decryptBlock
from aes.keyExpansionF import keyExpansion

#------------------------#
# apply padding          #
#------------------------#
def applyPadding(data):
    pad = 16 - (len(data) % 16)
    return data + b'\x01' + b'\x00'*(pad-1)

#------------------------#
# remove padding         #
#------------------------#
def removePadding(data):
    i = len(data) - 1
    while i > 0 and data[i] == 0: i -= 1
    if data[i] != 1:
        raise ValueError("Padding inválido")
    return data[:i]

#------------------------#
# cbc encrypt            #
#------------------------#
def cbcEncrypt(data, key):
    rk = keyExpansion(key)
    data = applyPadding(data)
    out = b''
    prev = b'\x00' * 16
    for i in range(0, len(data), 16):
        block = bytes(data[i+j] ^ prev[j] for j in range(16))
        enc = encryptBlock(block, rk)
        out += enc; prev = enc
    return out

#------------------------#
# cbc decrypt            #
#------------------------#
def cbcDecrypt(data, key):
    if len(data) % 16 != 0:
        raise ValueError("Archivo inválido")
    rk = keyExpansion(key)
    out = b''
    prev = b'\x00' * 16
    for i in range(0, len(data), 16):
        block = data[i:i+16]
        dec = decryptBlock(block, rk)
        out += bytes(dec[j] ^ prev[j] for j in range(16))
        prev = block
    return removePadding(out)
