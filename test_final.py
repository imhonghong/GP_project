import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import random
import os
import csv

# count E
# function of Entropy 
def Calculate_Entropy(dataproperty):
    entropy = 0
    label_count = {}
    for row in dataproperty:
        if row in label_count:
            label_count[row] += 1
        else:
            label_count[row] = 1
            
    for key in label_count:
        probability = label_count[key] / len(dataproperty)
        entropy -= probability * math.log2(probability)

    return entropy

#transform data
def TF(data):

    data_numpro = [[]]
    proaxis = len(data.columns)-1
    store_pro = data[proaxis][0]
    re_pro_value=1 # replace property value
    insertlist=[]
    convertlist=[]
    convertlist.insert(0,data[proaxis][0])
    d=1
    
    for i in range(0,len(data),1):
        for k in range(0,len(convertlist),1):
            if(data[proaxis][i] == convertlist[k]):
                for j in range(0,proaxis,1):
                    insertlist.insert(j,data[j][i])    
                insertlist.insert(proaxis,k+1) #insert property value to insertlist    
                data_numpro.insert(i,insertlist)
                insertlist=[] #empty the insert array
                d=1
            else:
                d=d                
        if(d==1):
            d=0
        else:
            store_pro = data[proaxis][i]
            convertlist.insert(re_pro_value,store_pro)
            re_pro_value = re_pro_value + 1
            for j in range(0,proaxis,1):
                insertlist.insert(j,data[j][i])    
            insertlist.insert(proaxis,re_pro_value) #insert property value to insertlist    
            data_numpro.insert(i,insertlist)
            insertlist=[] #empty the insert array
            d=1
    
    pd.DataFrame(data_numpro).to_csv('data_numpro.csv')
    a = pd.read_csv('data_numpro.csv',header=None);

    a = a.drop([len(a)-1])
    
    for i in range(0,len(a.columns)-1,1):
        a[i]=a[i+1]

    a = a.drop(columns=len(a.columns)-1)

    for i in range(0,len(a)-1,1):
        a.iloc[i]=a.iloc[i+1]
        
    a = a.drop([len(a)-1])
    os.remove('data_numpro.csv')

    return [a,convertlist]


# distributor 
def distributor(train_data,testproperty,decisionvalue):
    s1=[]
    s2=[]
    j1=0
    j2=0
    for i in range(0,train_data.shape[0],1):
        if(decisionvalue >= train_data[testproperty][i]):
            s1.insert(j1,i)
            j1=j1+1
        else:
            s2.insert(j2,i)
            j2=j2+1
            
    return [s1,s2]

# convertor
def convertor(train_data,s1,s2):
    s1_1=[]
    s2_1=[]
    j1=0
    j2=0
    proaxis=len(train_data.columns)-1
    
    for i in s1:
        s1_1.insert(j1,train_data[proaxis][i])
        j1=j1+1
        
    for i in s2:
        s2_1.insert(j2,train_data[proaxis][i])
        j2=j2+1
        
    return [s1_1 ,s2_1]

#decoder
def DEC(train_data,codelist):
    node=[[]]
    k=0
    for i in codelist:
        ROW=[]
        for j in range(0,len(train_data.columns),1):
            ROW.insert(j,train_data[j][i])
        node.insert(k,ROW)
        k=k+1
        
    pd.DataFrame(node).to_csv('NODE.csv')
    a = pd.read_csv('NODE.csv',header=None);

    a = a.drop([len(a)-1])
    
    for i in range(0,len(a.columns)-1,1):
        a[i]=a[i+1]

    a = a.drop(columns=len(a.columns)-1)

    for i in range(0,len(a)-1,1):
        a.iloc[i]=a.iloc[i+1]
        
    a = a.drop([len(a)-1])
    os.remove('NODE.csv')
   
    return a

#matrix_decoder
def MDEC(train_data):
        
    pd.DataFrame(train_data).to_csv('data.csv')

    a = pd.read_csv('data.csv',header=None);
    a = a.drop([len(a)-1])
    
    for i in range(0,len(a.columns)-1,1):
        a[i]=a[i+1]

    a = a.drop(columns=len(a.columns)-1)

    for i in range(0,len(a)-1,1):
        a.iloc[i]=a.iloc[i+1]
        
    a = a.drop([len(a)-1])
    os.remove('data.csv')
    
    return a

#information gain
def IG(train_data,testproperty,decisionvalue):
    proaxis=len(train_data.columns)-1
    
    [S1,S2] = distributor(train_data,testproperty,decisionvalue)
    [S1_1, S2_1] = convertor(train_data,S1,S2)

    train_e = Calculate_Entropy(train_data[proaxis])
    S1_e = Calculate_Entropy(S1_1)
    S2_e = Calculate_Entropy(S2_1)

    IG = train_e - S1_e*(len(S1_1)/len(train_data)) - S2_e*(len(S2_1)/len(train_data))
    return [IG,S1,S2]

#get max property
def APM(classlist):    
    in_list=[]
    
    for i in range(0,len(classlist),1):
        in_list.insert(i,classlist[i])
   
    new=1
    convert_list=[]
    convert_list.insert(0,[in_list[0],1])
    for i in range(1,len(in_list),1):
        for j in range(0,len(convert_list),1):
            if(convert_list[j][0]==in_list[i]):
                convert_list[j][1]+=1
                new=0
            else:
                new=new
        if(new==1):
            new=1
            convert_list.insert(i,[in_list[i],1])
        else:
            new=1            

    max_num=convert_list[0][1]
    MAX=convert_list[0][0]
    for i in range(0,len(convert_list),1):
        if(max_num<convert_list[i][1]):
            max_num=convert_list[i][1]
            MAX=convert_list[i][0]
        else:
            MAX=MAX
            
    return MAX
#delete
def delete(classlist,del_value):    
    del_list=[]
    j=0
    
    for i in range(0,len(classlist),1):
        if(classlist[i]!=del_value):
            del_list.insert(j,classlist[i])
            j=j+1
        else:
            j=j
            
    return del_list

#maxize_IG
def MIG(train_data):

    DV=0
    pro=0
    [IG_max,s1,s2] = IG(train_data,0,train_data[0][0])
            
    for j in range(0,len(train_data.columns)-1,1):#最後一個column是data的類別
        pass_value=[]
        D2=[]
        pass_count=[0,0]
        pass_key=0
        pass_key_2=0
        pass_value.insert(0,APM(train_data[j]))
        D2 = delete(train_data[j],pass_value[0])
        if(len(D2)!=0):                         #not only one property
            pass_value.insert(1,APM(D2))
        else:
            pass_key=0
            
        for i in range(0,len(train_data),1):
            if(train_data[j][i]==pass_value[0]):#create key value
                if(pass_count[0]==0):
                    pass_count[0]=1
                    pass_key=0
                else:
                    pass_key=1
            elif(train_data[j][i]==pass_value[1]):
                if(pass_count[1]==0):
                    pass_count[1]=1
                    pass_key=0
                else:
                    pass_key=1
            else:
                pass_key=0

            if(pass_key==1):#find IG
                pass_key=0
            else:
                [IG_get,s1_t,s2_t] = IG(train_data,j,train_data[j][i])
                if(IG_max < IG_get):
                    IG_max=IG_get
                    s1=s1_t
                    s2=s2_t
                    DV=train_data[j][i]
                    pro=j
                
    return[DV,pro,s1,s2]

#node generator
def NG(S):
    [DV,pro,s_1,s_2] = MIG(S)
    sleft = DEC(S,s_1)
    sright = DEC(S,s_2)
    return [DV,pro,sleft,sright]

#tree_maker
def tree_maker(train_data,test_data,convertlist,const):
    pointer=[]
    nodedata_1=[]
    nodedata_2=[]
    p=0
    p1=[]
    p2=[]
    pointer=[]
    j_range=2
    dv1=[]
    dv2=[]
    L1=[]
    L2=[]
    pointer=[]
    proaxis=len(train_data.columns)-1
    #root
    nodedata_1.insert(0,train_data)
    p1.insert(0,0)
    KEY=0
    key_link=0
    n=0
    count=0
    end=0
    i=0
    while(end==0):
        
        n=0
        if(i%2==0):
            j_range = len(nodedata_1)
        else:
            j_range = len(nodedata_2)
            
        if(j_range<=0):
            end=1
        else:
            end=0

        for j in range(0,j_range,1):
            if(i%2==0):
                if(Calculate_Entropy(nodedata_1[j][proaxis])<=const or i==7):
                    dv1.insert(KEY,0)
                    dv2.insert(KEY,0)
                    L1.insert(KEY,1)
                    L2.insert(KEY,APM(nodedata_1[j][proaxis]))
                    p=p+1
                    #print("information of leaf",KEY,"is")
                    #print("number of data=",len(nodedata_1[j]))
                    #print("class is:",nodedata_1[j][proaxis][0])
                    #print("")
                else:
                    [DV,pro,sleft,sright] = NG(nodedata_1[j])
                    dv1.insert(KEY,DV)
                    dv2.insert(KEY,pro)
                    L1.insert(KEY,0)
                    L2.insert(KEY,0)
                    nodedata_2.insert(n,sleft)
                    nodedata_2.insert(n+1,sright)
                    n=n+2
                    P=p1[p]
                    p2.insert(n,P*2)
                    p2.insert(n+1,P*2+1)
                    p=p+1
                    count=count+1
                    #print("information of node",KEY,"is")
                    #print("number of data=",len(nodedata_1[j]))
                    #print("[determinevalue,deterprorerty]=",decision_matrix[KEY])
                    #print("")
            else:
                if(Calculate_Entropy(nodedata_2[j][proaxis])<=const or i==7):
                    dv1.insert(KEY,0)
                    dv2.insert(KEY,0)
                    L1.insert(KEY,1)
                    L2.insert(KEY,APM(nodedata_2[j][proaxis]))
                    p=p+1
                    #print("information of leaf",KEY,"is")
                    #print("number of data=",len(nodedata_2[j]))
                    #print("class is:",nodedata_2[j][proaxis][0])
                    #print("")
                else:
                    [DV,pro,sleft,sright] = NG(nodedata_2[j])
                    dv1.insert(KEY,DV)
                    dv2.insert(KEY,pro)
                    L1.insert(KEY,0)
                    L2.insert(KEY,0)
                    nodedata_1.insert(n,sleft)
                    nodedata_1.insert(n+1,sright)
                    n=n+2
                    P=p2[p]
                    p1.insert(n,P*2)
                    p1.insert(n+1,P*2+1)
                    p=p+1
                    count=count+1
                    #print("information of node",KEY,"is") 
                    #print("number of data=",len(nodedata_2[j]))
                    #print("[determinevalue,deterprorerty]=",decision_matrix[KEY])
                    #print("")           
            KEY=KEY+1
            
        if(i%2==0):
            nodedata_1=[]
            p1=[]
            pointer=p2
        else:
            nodedata_2=[]
            p2=[]
            pointer=p1
            
        if(i==0):
            dv0_1=dv1
            dv0_2=dv2
            L0_1=L1
            L0_2=L2
            p_1=pointer
        elif(i==1):           
            dv1_1=dv1
            dv1_2=dv2
            L1_1=L1
            L1_2=L2
            p_2=pointer 
        elif(i==2):
            dv2_1=dv1
            dv2_2=dv2
            L2_1=L1
            L2_2=L2
            p3=pointer
        elif(i==3):
            dv3_1=dv1
            dv3_2=dv2
            L3_1=L1
            L3_2=L2
            p4=pointer
        elif(i==4):
            dv4_1=dv1
            dv4_2=dv2
            L4_1=L1
            L4_2=L2
            p5=pointer
        elif(i==5):
            dv5_1=dv1
            dv5_2=dv2
            L5_1=L1
            L5_2=L2
            p6=pointer
        elif(i==6):
            dv6_1=dv1
            dv6_2=dv2
            L6_1=L1
            L6_2=L2
            p7=pointer
        elif(i==7):
            dv7_1=dv1
            dv7_2=dv2
            L7_1=L1
            L7_2=L2
            p8=pointer
        else:
            p9=pointer
            
        dv1=[]
        dv2=[]
        L1=[]
        L2=[]
        pointer=[]
        KEY=0
        p=0
        i=i+1
                       
    return [dv0_1,dv0_2,L1_1,L1_2,dv1_1,dv1_2,L2_1,L2_2,dv2_1,dv2_2,L3_1,L3_2,dv3_1,dv3_2,L4_1,L4_2,dv4_1,dv4_2,L5_1,L5_2,dv5_1,dv5_2,L6_1,L6_2,dv6_1,dv6_2,L7_1,L7_2,p_1,p_2,p3,p4,p5,p6,p7]

#data_processor
def DP(data):
    [data_1,convertlist] = TF(data)
    train_data = data_1.sample(frac=7/10, random_state=1);
    test_data = data_1.drop(train_data.index);

    train_data = train_data.reset_index(level=None)
    train_data = train_data.drop("index", axis=1)
    test_data = test_data.reset_index(level=None)
    test_data = test_data.drop("index", axis=1)

    return [train_data,test_data,convertlist]

#data_processor_2
def DP2(a):
    for i in range(0,len(a.columns)-1,1):
        a[i]=a[i+1]
    a = a.drop(columns=len(a.columns)-1)

    for i in range(0,len(a)-1,1):
        a.iloc[i]=a.iloc[i+1]
    a=a.drop([len(a)-1])
    return a

#main function

#data=pd.read_csv('csv_result-PhishingData.csv',header=None);
data=pd.read_csv('csv_result-PhishingData.csv',header=None);
   
data_1=DP2(data)

[train_data,test_data,convertlist]=DP(data_1)

list_out = tree_maker(train_data,test_data,convertlist,0.05)
#print(test_data.iloc[0])

#to look output
j=0
for i in list_out[0:28]:
    if(j%4==0):
        print("")
        print("level",j/4)
    print(i)
    j=j+1

print("")
for i in list_out[28:36]:
    print(i)

#output to csv
pd.DataFrame(test_data).to_csv('output_tree\\testdata.csv',header=None,index=False)    
pd.DataFrame(list_out[0]).to_csv('output_tree\\dv0_1.csv',header=None,index=False)
pd.DataFrame(list_out[1]).to_csv('output_tree\\dv0_2.csv',header=None,index=False)
pd.DataFrame(list_out[2]).to_csv('output_tree\\L1_1.csv',header=None,index=False)
pd.DataFrame(list_out[3]).to_csv('output_tree\\L1_2.csv',header=None,index=False)

pd.DataFrame(list_out[4]).to_csv('output_tree\\dv1_1.csv',header=None,index=False)
pd.DataFrame(list_out[5]).to_csv('output_tree\\dv1_2.csv',header=None,index=False)
pd.DataFrame(list_out[6]).to_csv('output_tree\\L2_1.csv',header=None,index=False)
pd.DataFrame(list_out[7]).to_csv('output_tree\\L2_2.csv',header=None,index=False)

pd.DataFrame(list_out[8]).to_csv('output_tree\\dv2_1.csv',header=None,index=False)
pd.DataFrame(list_out[9]).to_csv('output_tree\\dv2_2.csv',header=None,index=False)
pd.DataFrame(list_out[10]).to_csv('output_tree\\L3_1.csv',header=None,index=False)
pd.DataFrame(list_out[11]).to_csv('output_tree\\L3_2.csv',header=None,index=False)

pd.DataFrame(list_out[12]).to_csv('output_tree\\dv3_1.csv',header=None,index=False)
pd.DataFrame(list_out[13]).to_csv('output_tree\\dv3_2.csv',header=None,index=False)
pd.DataFrame(list_out[14]).to_csv('output_tree\\L4_1.csv',header=None,index=False)
pd.DataFrame(list_out[15]).to_csv('output_tree\\L4_2.csv',header=None,index=False)

pd.DataFrame(list_out[16]).to_csv('output_tree\\dv4_1.csv',header=None,index=False)
pd.DataFrame(list_out[17]).to_csv('output_tree\\dv4_2.csv',header=None,index=False)
pd.DataFrame(list_out[18]).to_csv('output_tree\\L5_1.csv',header=None,index=False)
pd.DataFrame(list_out[19]).to_csv('output_tree\\L5_2.csv',header=None,index=False)

pd.DataFrame(list_out[20]).to_csv('output_tree\\dv5_1.csv',header=None,index=False)
pd.DataFrame(list_out[21]).to_csv('output_tree\\dv5_2.csv',header=None,index=False)
pd.DataFrame(list_out[22]).to_csv('output_tree\\L6_1.csv',header=None,index=False)
pd.DataFrame(list_out[23]).to_csv('output_tree\\L6_2.csv',header=None,index=False)

pd.DataFrame(list_out[24]).to_csv('output_tree\\dv6_1.csv',header=None,index=False)
pd.DataFrame(list_out[25]).to_csv('output_tree\\dv6_2.csv',header=None,index=False)
pd.DataFrame(list_out[26]).to_csv('output_tree\\L7_1.csv',header=None,index=False)
pd.DataFrame(list_out[27]).to_csv('output_tree\\L7_2.csv',header=None,index=False)

pd.DataFrame(list_out[28]).to_csv('output_tree\\pointer1.csv',header=None,index=False)
pd.DataFrame(list_out[29]).to_csv('output_tree\\pointer2.csv',header=None,index=False)
pd.DataFrame(list_out[30]).to_csv('output_tree\\pointer3.csv',header=None,index=False)
pd.DataFrame(list_out[31]).to_csv('output_tree\\pointer4.csv',header=None,index=False)
pd.DataFrame(list_out[32]).to_csv('output_tree\\pointer5.csv',header=None,index=False)
pd.DataFrame(list_out[33]).to_csv('output_tree\\pointer6.csv',header=None,index=False)
pd.DataFrame(list_out[34]).to_csv('output_tree\\pointer7.csv',header=None,index=False)



