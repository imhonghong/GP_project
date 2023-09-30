import numpy as np
import pandas as pd
import math
import random
import os

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
    a = pd.read_csv('data_numpro.csv',header=None)

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
    a = pd.read_csv('NODE.csv',header=None)

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

    a = pd.read_csv('data.csv',header=None)
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
def APM(classlist):    #need to rewrite
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
        if(len(D2)==0):#it's a leaf, only one property
            pass_key_2=1
        else:
            pass_value.insert(1,APM(D2))
            
        for i in range(0,len(train_data),1):
            if(pass_key_2==1):#it's a leaf
                pass_key_2==0
            elif(train_data[j][i]==pass_value[0]):#create key value
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
def tree_maker(train_data,test_data,convertlist):
    nodedata_1=[[]]
    nodedata_2=[[]]
    decision_matrix=[[]]
    leaf_matrix=[[]]
    key_link_array=[[]]
    proaxis=len(train_data.columns)-1
    loss_key_count=0
    #root
    nodedata_1.insert(0,train_data)
    KEY=0
    key_link=0
    n=0
    count=0
    end=0
    i=0
    while(end==0):
        #print("depth of tree=",i)
        #print("")
        loss_key_count=loss_key_count*2
        n=0
        for j in range(0,2**i-loss_key_count,1):#also can be replaced by (i%2==0)?(len(nodedata_1)-1):(len(nodedata_2)-1)
            if(i%2==0):
                if(Calculate_Entropy(nodedata_1[j][proaxis])==0):
                    decision_matrix.insert(KEY,0)#useless
                    leaf_matrix.insert(KEY,[1,i,nodedata_1[j][proaxis][0]])
                    loss_key_count=loss_key_count+1
                    #print("information of leaf",KEY,"is")
                    #print("number of data=",len(nodedata_1[j]))
                    #print("class is:",nodedata_1[j][proaxis][0])
                    #print("")
                else:
                    [DV,pro,sleft,sright] = NG(nodedata_1[j])
                    decision_matrix.insert(KEY,[DV,pro])
                    leaf_matrix.insert(KEY,[0,i,APM(nodedata_1[j][proaxis])])#useless
                    nodedata_2.insert(n,sleft)
                    nodedata_2.insert(n+1,sright)
                    n=n+2
                    key_link_array.insert(count,[KEY,key_link+1,key_link+2])
                    key_link=key_link+2
                    count=count+1
                    #print("information of node",KEY,"is")
                    #print("number of data=",len(nodedata_1[j]))
                    #print("[determinevalue,deterprorerty]=",decision_matrix[KEY])
                    #print("")
            else:
                if(Calculate_Entropy(nodedata_2[j][proaxis])==0):
                    loss_key_count=loss_key_count+1
                    decision_matrix.insert(KEY,0)#useless
                    leaf_matrix.insert(KEY,[1,i,nodedata_2[j][proaxis][0]])
                    #print("information of leaf",KEY,"is")
                    #print("number of data=",len(nodedata_2[j]))
                    #print("class is:",nodedata_2[j][proaxis][0])
                    #print("")
                else:
                    [DV,pro,sleft,sright] = NG(nodedata_2[j])
                    decision_matrix.insert(KEY,[DV,pro])
                    leaf_matrix.insert(KEY,[0,i,APM(nodedata_2[j][proaxis])])#useless
                    nodedata_1.insert(n,sleft)
                    nodedata_1.insert(n+1,sright)
                    n=n+2
                    key_link_array.insert(count,[KEY,key_link+1,key_link+2])
                    key_link=key_link+2
                    count=count+1
                    #print("information of node",KEY,"is") 
                    #print("number of data=",len(nodedata_2[j]))
                    #print("[determinevalue,deterprorerty]=",decision_matrix[KEY])
                    #print("")           
            KEY=KEY+1
        if(i%2==0):
            nodedata_1=[[]]
        else:
            nodedata_2=[[]]
        #cut
        if(i==0):
            S=0
            S_count=0
            SOL_DEEP=0
        else:
            [success,fail]=tester(test_data,convertlist,decision_matrix,leaf_matrix,i,key_link_array)
            print("results of test data in depth",i)
            print("success:",success)
            print("fail:",fail)
            print("")
            if(success>S): # trade_off
                SOL_DEEP=i
                S=success
                S_count=0
            elif(S_count==1):
                SOL_DEEP=SOL_DEEP-1
                end=1
            elif(success==S):
                SOL_DEEP=i
                S=success
                S_count=1
            else:
                SOL_DEEP=SOL_DEEP
                end=1
        i=i+1
                        
    return [decision_matrix,leaf_matrix,key_link_array,SOL_DEEP]

#tester
def tester(test_data,convertlist,D0,L0,testdepth,key_link_array):
    success=0
    fail=0
    proaxis=len(test_data.columns)-1

    for i in range(0,len(test_data),1):
        KEY=0
        KEY_1=0
        end=0
        d=0
        while(end==0):
            testaxis = D0[KEY][1]
            if(D0[KEY][0] >= test_data[testaxis][i]):
                for k in range(0,len(key_link_array)-1,1):
                    if(key_link_array[k][0]==KEY):
                        KEY_1=key_link_array[k][1] #left
                    else:
                        KEY_1=KEY_1
            else:
                for k in range(0,len(key_link_array)-1,1):
                    if(key_link_array[k][0]==KEY):
                        KEY_1=key_link_array[k][2] #right
                    else:
                        KEY_1=KEY_1
            KEY=KEY_1   
            if(L0[KEY][0]==1 or L0[KEY][1]==testdepth):
                d=1
                if(L0[KEY][2]==test_data[proaxis][i]):
                    success=success+1
                    KEY=0
                else:
                    fail=fail+1
                    KEY=0
            else:
                d=d
                    
            if(d==1):
                d=0
                end=1
            else:
                end=0
                
    return [success,fail]

#data_processor
def DP(data):
    [data_1,convertlist] = TF(data)
    train_data = data_1.sample(frac=1/200, random_state=1)
    test_data = data_1.drop(train_data.index)

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
acc=[]
for count in range(10):
    #data=pd.read_csv('csv_result-Training Dataset.csv',header=None)
    #data=pd.read_csv('Phishing_Legitimate_full.csv',header=None)
    #data=pd.read_csv('csv_result-PhishingData.csv',header=None)
    data=pd.read_csv('Obfuscated-MalMem2022.csv',header=None,low_memory=False)
    #encoding only for Obfuscated-MalMem2022.csv
    code_dict = {}
    next_code = 0
    for i in range(1,len(data),1):
        for col in [0, len(data.columns) - 1]:
            string = data.iloc[i, col]
            if string in code_dict:
                data.iloc[i, col] = code_dict[string]
            else:
                code_dict[string] = next_code
                data.iloc[i, col] = next_code
                next_code += 1

    data_1=DP2(data)

    [train_data,test_data,convertlist]=DP(data_1)

    [D0,L0,key_link_array,SOL_DEEP]=tree_maker(train_data,test_data,convertlist)

    [success,fail]=tester(test_data,convertlist,D0,L0,SOL_DEEP,key_link_array)

    print("final results of test data in DT")
    print("number of test data",len(test_data))
    print(f"it\'s {count} time")
    print("success:",success)
    print("fail:",fail)
    acc.append(fail)

total=0
for a in acc:
    total=total+acc[a]
avg=100-((total/10)/58303)
print(f"average accuracy={avg}%")    
