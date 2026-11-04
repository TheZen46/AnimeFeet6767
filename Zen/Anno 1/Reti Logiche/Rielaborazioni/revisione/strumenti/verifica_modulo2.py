from itertools import product
exec(open(__file__.replace('modulo2', 'modulo1')).read().split('# 1.3 esempi')[0])
# MUX
mux=lambda SEL,S1,S0: S1 if SEL else S0
chk("mux sop", mux, lambda SEL,S1,S0: N(SEL)&S0|SEL&S1, 3)
chk("mux pos", mux, lambda SEL,S1,S0: (SEL|S0)&(N(SEL)|S1), 3)
# porta programmabile
def pp(S0,S1,A,B):
    return {(0,0):A&B,(0,1):A|B,(1,0):N(A),(1,1):None}[(S0,S1)]
f=lambda *v: pp(*v) or 0; dc=lambda S0,S1,A,B: S0==1 and S1==1
chk("pp sop", f, lambda S0,S1,A,B: S1&A|S1&B|S0&N(A)|N(S0)&A&B, 4, dc)
chk("pp pos", f, lambda S0,S1,A,B: (N(S0)|N(A))&(S0|S1|A)&(S0|S1|B)&(S0|A|B), 4, dc)
# encoder priorita'
def enc(I3,I2,I1,I0):
    if I3: return (1,1,1)
    if I2: return (1,0,1)
    if I1: return (0,1,1)
    if I0: return (0,0,1)
    return (None,None,0)
for k,g in enumerate([lambda I3,I2,I1,I0: I3|I2, lambda I3,I2,I1,I0: I3|N(I2)&I1, lambda I3,I2,I1,I0: I3|I2|I1|I0]):
    chk("enc%d"%k, lambda *v,k=k: enc(*v)[k] or 0, g, 4, lambda *v,k=k: enc(*v)[k] is None)
# alea: consenso
chk("alea", lambda A,B,C: N(A)&B|A&C, lambda A,B,C: N(A)&B|A&C|B&C, 3)
# full adder
chk("fa S", lambda a,b,c: (a+b+c)%2, lambda a,b,c: a^b^c, 3)
chk("fa C", lambda a,b,c: (a+b+c)//2, lambda a,b,c: a&b|a&c|b&c, 3)
b=lambda s:int(s,2)
assert b('01010')==10 and b('1001')==9 and b('10100110010')==1330 and bin(38)[2:]=='100110'
assert int('33',8)==27 and int('12',8)==10 and int('5E',16)==94 and hex(30)=='0x1e'
assert b('1001010')+b('110110')==b('10000000')==128 and b('1001010')==74 and b('110110')==54
assert b('1010010')-b('111111')==b('0010011')==19
assert b('1010010')+b('110010')==b('10000100')==132
assert b('1010100')-b('110001')==b('0100011')==35 and b('1010100')-b('111111')==b('0010101')==21
assert b('10110')*b('111')==b('10011010')==154 and b('10110')+b('101100')+b('1011000')==154
assert b('1010')*b('110')==b('111100')==60 and b('1010')*b('10110')==b('11011100')==220
assert b('10100')+b('101000')+b('10100000')==220
def c2(v,n):
    return v-(1<<n) if v>>(n-1) else v
assert [c2(i,3) for i in range(8)]==[0,1,2,3,-4,-3,-2,-1]
assert format((-11)&0xff,'08b')=='11110101'
for a,bb,r in [(3,4,7),(-7,3,-4),(-8,6,-2),(7,-2,5)]:
    assert c2(((a&15)+(bb&15))&15,4)==r, (a,bb)
assert c2((5+4)&15,4)==-7
assert format((-3)&0xff,'08b')=='11111101'
# overflow V = c_n xor c_{n-1}
for a in range(-8,8):
  for bb in range(-8,8):
    A,B=a&15,bb&15
    cn1=((A&7)+(B&7))>>3; cn=(A+B)>>4
    assert (cn^cn1)==int(not -8<=a+bb<=7)
# sottrattore e comparatore: borrow (carry=0) iff A<B
for A in range(16):
  for B in range(16):
    s=A+((~B)&15)+1
    assert (s&15)==((A-B)&15)
    assert (s>>4==0)==(A<B)
# parita'
assert sum(map(int,'0111010'))%2==0
print("aritmetica ok")
