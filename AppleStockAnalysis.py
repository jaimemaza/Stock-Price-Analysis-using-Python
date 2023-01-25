#!/usr/bin/env python
# coding: utf-8

# In[12]:


fileName = 'AppleStock.csv'
def getDataAsList(fileName):
    dataFile = open(fileName, "r")
    stockList = []
    for line in dataFile:
        stockList.append(line.strip().split(','))
    del stockList[0]
    return stockList

data1 = getDataAsList(fileName)



range(len(data1))


def getMonthlyAverage1(stockList):
    new_list = []
    for i in stockList:
        month=i[0].split('/')[0]
        new_list.append(month)
        year=i[0].split('/')[2]
        new_list.append(year)
        close=float(i[6])
        new_list.append(close)
        volume=float(i[5])
        new_list.append(volume)

    

    my_list = new_list

    n = 4

    final = [my_list[i * n:(i + 1) * n] for i in range((len(my_list) + n - 1) // n )] 
    m ='7'
    n='2017'
    monthlyAverageList=[]
    numerator=0.0
    denominator=0.0   
    
    for i in final:    
        month=i[0]  
        year=i[1]        
        close=float(i[2])
        volume=float(i[3])        
        if month!=m:            
            averag=numerator/denominator  
            average = "{:.2f}".format(averag)
            a_tuple=(month, year, average)
            monthlyAverageList.append(a_tuple)
            
        numerator+=close*volume
        denominator+=volume
        m=month
        n=year
    return monthlyAverageList

def printTopBottom5(monthlyAverageList): 
    top5=[]
    top5 = sorted(monthlyAverageList, key=lambda t: t[2], reverse=True)[:5]
    print("Top 5:")
    for data in top5:
        month,year, averages=data
        print(month,"/", year," - ",  averages)

    bottom5=[]
    bottom5 = sorted(monthlyAverageList, key=lambda t: t[2], reverse=False)[:5]
    print("\nBottom 5:")
    for data in bottom5:
        month,year, averages=data
        print(month,"/", year, " - ", averages)

monthlyAverageList = getMonthlyAverage1(data1)
printTopBottom5(monthlyAverageList)


# In[ ]:




