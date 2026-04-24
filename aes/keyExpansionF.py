#======================#
#    KEY EXPANSION     #
#======================#

#------------------------#
# imports                #
#------------------------#

from aes.tables import SBOX, RCON

#------------------------#
# key_expansion          #
#------------------------#
def keyExpansion(key):
    w = list(key)
    for i in range(4, 44):
        t = w[(i-1)*4 : i*4]
        if i % 4 == 0:
            t = t[1:] + t[:1]
            t = [SBOX[b] for b in t]
            t[0] ^= RCON[i // 4]
        prev = w[(i-4)*4 : (i-3)*4]
        w += [prev[j] ^ t[j] for j in range(4)]
    return w
