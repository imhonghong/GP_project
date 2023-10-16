import csv

def remove_topic(list2D):
    for row in range(0,len(list2D)):
        del list2D[row][0]
    del list2D[0]
    long=len(list2D)
    width=len(list2D[0])
    return [list2D,long,width]

def transverse(data,long,width):
    ap=[]
    for property in range(0,width,1):
        av=[]
        for index in range(0,long,1):
            av.append(data[index][property])
        ap.append(av)
    #ap is data in transverse
    return ap

def CAV(ap,long,width):
    cnt=[]
    for pro in range(0,width-1,1): #width is class
        cl=[]
        for ele in range(0,long,1):
            if(ap[pro][ele] not in cl):
                cl.append(ap[pro][ele])
        cl.append(len(cl))
        cnt.append(cl[-1])
    return cnt

def countListByDict(lst):
    stats = {}
    for i in lst:
        if i in stats:
            stats[i] += 1
        else:
            stats[i] = 1
    return stats

def testing(datafile):
    for i in range(0,len(datafile),1):
        data_ori = list(csv.reader(open(datafile[i])))
        [data,long,width]=remove_topic(data_ori)
        ap=transverse(data,long,width)
        cnt=CAV(ap,long,width)
        stats=countListByDict(cnt)
        print(f"for {datafile[i]} , has {width-1} attributes")
        print(f"it's attribute value is like {stats}")

####### main function #####
datafile=['Phishing Websites Data Set.csv',
          'Website Phishing Data Set.csv',
          'Phishing_Legitimate_full.csv',
          'breast-cancer.csv',
          'fourclass.csv',
          'iris.csv',
          'Obfuscated-MalMem2022.csv']
testing(datafile)

