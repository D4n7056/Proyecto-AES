#======================#
#      OPERATIONS      #
#======================#

#------------------------#
# imports                #
#------------------------#
from aes.tables import SBOX, INV_SBOX
from aes.multiplicationGF import gf

#------------------------#
# bytes to state         #
#------------------------#
def bytesToState(b):
    return list(b)

#------------------------#
# state to bytes         #
#------------------------#
def stateToBytes(s):
    return bytes(s)

#------------------------#
# add round key          #
#------------------------#
def addRoundKey(s, rk, r):
    off = r * 16
    for c in range(4):
        for row in range(4):
            s[row + 4*c] ^= rk[off + c*4 + row]

#------------------------#
# sub bytes              #
#------------------------#
def subBytes(s):
    for i in range(16):
        s[i] = SBOX[s[i]]

#------------------------#
# inv sub bytes          #
#------------------------#
def invSubBytes(s):
    for i in range(16):
        s[i] = INV_SBOX[s[i]]

#------------------------#
# shift rows             #
#------------------------#
def shiftRows(s):
    for row in range(1, 4):
        tmp = [s[row + 4*c] for c in range(4)]
        tmp = tmp[row:] + tmp[:row]
        for c in range(4):
            s[row + 4*c] = tmp[c]

#------------------------#
# inv shift rows         #
#------------------------#
def invShiftRows(s):
    for row in range(1, 4):
        tmp = [s[row + 4*c] for c in range(4)]
        tmp = tmp[-row:] + tmp[:-row]
        for c in range(4):
            s[row + 4*c] = tmp[c]

#------------------------#
# mix columns            #
#------------------------#
def mixColumns(s):
    for c in range(4):
        a = [s[r + 4*c] for r in range(4)]
        s[0 + 4*c] = gf(2,a[0]) ^ gf(3,a[1]) ^ a[2]         ^ a[3]
        s[1 + 4*c] = a[0]         ^ gf(2,a[1]) ^ gf(3,a[2])  ^ a[3]
        s[2 + 4*c] = a[0]         ^ a[1]          ^ gf(2,a[2])  ^ gf(3,a[3])
        s[3 + 4*c] = gf(3,a[0]) ^ a[1]          ^ a[2]          ^ gf(2,a[3])

#------------------------#
# inv mix columns        #
#------------------------#
def invMixColumns(s):
    for c in range(4):
        a = [s[r + 4*c] for r in range(4)]
        s[0 + 4*c] = gf(0xe,a[0]) ^ gf(0xb,a[1]) ^ gf(0xd,a[2]) ^ gf(0x9,a[3])
        s[1 + 4*c] = gf(0x9,a[0]) ^ gf(0xe,a[1]) ^ gf(0xb,a[2]) ^ gf(0xd,a[3])
        s[2 + 4*c] = gf(0xd,a[0]) ^ gf(0x9,a[1]) ^ gf(0xe,a[2]) ^ gf(0xb,a[3])
        s[3 + 4*c] = gf(0xb,a[0]) ^ gf(0xd,a[1]) ^ gf(0x9,a[2]) ^ gf(0xe,a[3])

