import pandas as pd
import tkinter
list1=['a','b','c']
list_repeat=[]
data=pd.read_excel('amin.xlsx',skiprows=2,usecols='B:E')
df=pd.DataFrame(data)

x=df.shape[0]//3
y=df.shape[0]%3

for i in range(x):
    for j in list1:
       list_repeat.append(j)

for i in range(y):
        list_repeat.append(list1[i])

df["repeat"]=list_repeat
df.to_excel("amin2.xlsx")