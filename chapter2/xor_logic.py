def XOR(x1,x2):
    s1 = NAND(x1,x2)
    s2 = OR(x1,x2)
    y = AND(s1,s2)
    return y

XOR(0,0)
XOR(1,0)
XOR(0,1)
XOR(1,1)

