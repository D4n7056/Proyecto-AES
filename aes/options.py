#=================#
#     OPTIONS     #
#=================#

#------------------------#
# imports                #
#------------------------#
from aes.operations import (subBytes, invSubBytes, 
                            shiftRows, invShiftRows,
                            mixColumns, invMixColumns,
                            addRoundKey,
                            bytesToState, stateToBytes)
from aes.keyExpansionF import keyExpansion

#------------------------#
# encrypt_block          #
#------------------------#
def encryptBlock(b, rk):
    s = bytesToState(b)
    addRoundKey(s, rk, 0)
    for r in range(1, 10):
        subBytes(s); shiftRows(s); mixColumns(s)
        addRoundKey(s, rk, r)
    subBytes(s); shiftRows(s); addRoundKey(s, rk, 10)
    return stateToBytes(s)

#------------------------#
# decrypt_block          #
#------------------------#
def decryptBlock(b, rk):
    s = bytesToState(b)
    addRoundKey(s, rk, 10)
    for r in range(9, 0, -1):
        invShiftRows(s); invSubBytes(s)
        addRoundKey(s, rk, r); invMixColumns(s)
    invShiftRows(s); invSubBytes(s); addRoundKey(s, rk, 0)
    return stateToBytes(s)