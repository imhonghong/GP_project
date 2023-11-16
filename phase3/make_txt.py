# function: many decimal(<65535) output by 4-bit-hex in txt file
# function: given an 2D array, output a txt file
#read csv convert to 2D number list
#constrain: number only, string is prohibitted

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
        hs=hs+x #hs is string
    return hs

def DecToH4(dec):
    B16=DtoB16(dec)
    s=B16toStr(B16)
    hs=B16toH4_STR(s)
    return hs


import csv

def csvTO2d(path):
    with open(path,newline='') as f:
        ad=[]
        csvreader = csv.reader(f)
        for row in csvreader:
            ad.append(row[1:]) #cut id
        ad=ad[1:] #cut title row
        for ins in range(0,len(ad)):
            ad[ins]=list(map(float, ad[ins]))
    return ad

def findMin(ad):
    minList=[]
    for att in range(0,len(ad[1])):
        min=ad[0][att]
        for ins in range(0,len(ad)):
            if(ad[ins][att]<min):
                min=ad[ins][att]
        minList.append(min)

    return minList

def bias_ad(ad,minList):
    for att in range(0,len(minList)):
        if(att==(len(minList)-1)): #giving class bias, reserve 0 for not-leaf
            for ins in range(0,len(ad)):
                ad[ins][att]=ad[ins][att]-minList[att]+1            
        else:
            for ins in range(0,len(ad)):
                ad[ins][att]=ad[ins][att]-minList[att]

    return ad

#####-----main function-----#####

path=r"D:\onedrive同步資料夾\OneDrive - 國立中山大學\中山05\0_GP專題\phase3\csv_result-Training Dataset.csv"
ad=csvTO2d(path)
minList=findMin(ad)
dec=bias_ad(ad,minList)

path = 'PI.txt'
f = open(path, 'w')
for ins in range(0,len(dec)):
    a_instr=""
    for att in range(0,len(minList)):
        a_instr=a_instr+DecToH4(dec[ins][att])+" "
    a_instr=a_instr[0:-1]
    print(a_instr,file=f)
    
f.close()
print("work is done, please check the txt file")




