# function: many decimal(<65535) output by 4-bit-hex in txt file
def DtoB16(dec):
    B16=[]
    if(dec<0):
        dec=-dec
    max=65535
    if(dec>max):
        print("out of range, max=65535")
        return -1
    else:
        for e in range(15,-1,-1):
            
            if(dec-pow(2,e))>=0:
                B16.append("1")
                dec=dec-pow(2,e)
            else:
                B16.append("0")
    return B16

def B16toStr(B16):
    s=""
    for i in range(15,-1,-1):
        s=B16[i]+s
        if(i%4==0):
            s="_"+s
    s=s[1:]
    return s

def B16toH4_STR(s):
    hs=""
    hl=[]
    ss=s.split("_")
    for i in range(0,4):
        if(ss[i]=="0000"):
            x="0"
        elif(ss[i]=="0001"):
            x="1"
        elif(ss[i]=="0010"):
            x="2"
        elif(ss[i]=="0011"):
            x="3"
        elif(ss[i]=="0100"):
            x="4"
        elif(ss[i]=="0101"):
            x="5"
        elif(ss[i]=="0110"):
            x="6"
        elif(ss[i]=="0111"):
            x="7"
        elif(ss[i]=="1000"):
            x="8"
        elif(ss[i]=="1001"):
            x="9"
        elif(ss[i]=="1010"):
            x="A"
        elif(ss[i]=="1011"):
            x="B"
        elif(ss[i]=="1100"):
            x="C"
        elif(ss[i]=="1101"):
            x="D"
        elif(ss[i]=="1110"):
            x="E"
        else:
            x="F"
        hs=hs+x
    return hs

def DecToH4(dec):
    B16=DtoB16(dec)
    s=B16toStr(B16)
    hs=B16toH4_STR(s)
    return hs

#####-----main function-----#####
dec=[4560,55004,35280]
path = 'output.txt'
f = open(path, 'w')
for d in range(0,len(dec)):
    hs=DecToH4(dec[d])
    print(hs, file=f)
f.close()
print("work is done, please check the txt file")