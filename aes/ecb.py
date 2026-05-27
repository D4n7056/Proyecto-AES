#=================#
#       ECB       #
#=================#
from aes.options import encryptBlock, decryptBlock
from aes.keyExpansionF import keyExpansion

def applyPadding(data):
    pad = 16 - (len(data) % 16)
    return data + bytes([pad] * pad)

def removePadding(data):
    pad_val = data[-1]
    if pad_val < 1 or pad_val > 16:
        raise ValueError("Padding inválido")
    return data[:-pad_val]

def ecbEncrypt(data, key):
    rk   = keyExpansion(key)
    data = applyPadding(data)
    out  = b''
    for i in range(0, len(data), 16):
        out += encryptBlock(data[i:i+16], rk)
    return out

def ecbDecrypt(data, key):
    if len(data) % 16 != 0:
        raise ValueError("Archivo inválido")
    rk  = keyExpansion(key)
    out = b''
    for i in range(0, len(data), 16):
        out += decryptBlock(data[i:i+16], rk)
    return removePadding(out)
