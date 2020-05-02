import pandas as pd
import matplotlib.pyplot as plt

from pandass.test2 import *

df1=pd.read_csv('book.txt',sep='-',index_col='id')
print(df1)
'''df1=pd.read_excel('books2.xlsx',skiprows=2,usecols='B:I',index_col='dec',sheet_name='Feuil1')
df2=pd.read_excel('books2.xlsx',index_col='title',sheet_name='Feuil2')
#table=df1.merge(df2,how='left',on='title')
#table=df1.merge(df2,how='left',on='title').fillna(0)
#table=df1.merge(df2,how='left',left_on=df1.index,right_on=df2.index).fillna(0)
table=df1.merge(df2,how='left',on='id').fillna(0)
table.total=table.total.astype(int)
a=df1.transpose()
print(a)
print(df2)
print(table)'''


'''df=pd.read_excel('books2.xlsx',skiprows=2,usecols='B:I',index_col='title')
#df.plot(y=['oct','spt','dec'])
#df.plot.area(y=['oct','spt','dec'])
#df.plot.bar(y=['oct','spt','dec'],stacked=True)
#df.plot.scatter(x='dec',y='oct')
#df.dec.plot.hist(bins=100)
df.dec.plot.kde()
plt.show()'''

'''df=pd.read_excel('books2.xlsx',skiprows=2,usecols='B:I',index_col='title')
df['number'].sort_values(ascending=True).plot.pie(startangle=90)
plt.show()'''
'''df=pd.read_excel('books2.xlsx',skiprows=2,usecols='B:I')
df.plot.barh(x='title',y=['spt','oct','dec'],stacked=True,title='title with month')
plt.tight_layout()
plt.show()'''



'''def add1(x):

    return x+2
def add(x):

    return 13<=x<=17
def add2(x):

    return 50<=x<=80
df=pd.read_excel('books2.xlsx',skiprows=2,usecols='B:E')
#df.set_index('id',inplace=True)
df.sort_values(by='number',inplace=True,ascending=False)
#df.sort_values(by='id',inplace=True,ascending=False)
#df.sort_values(by=['id','price'],inplace=True,ascending=[True,False])
#df['price']=df['price'].apply(add1)
#df=df.loc[df['price'].apply(add)]

df['total']=df['price']*df['number']
#df=df.loc[df['total'].apply(add2)]

#df.plot.bar(x='title',y='number',color='orange',title='numbers of books')
df.plot.bar(x='title',y=['number','price'],color=['orange','red'])

#plt.bar(df.title,df.number,color='red')
#plt.xticks(df.title,rotation='70')

#plt.tight_layout()

#plt.xlabel('title',fontweight='bold')
#plt.ylabel('number')
ax=plt.gca()
ax.set_xticklabels(df['title'],rotation=45,ha='right')

f=plt.gcf()
f.subplots_adjust(left=0.5,bottom=0.45)
plt.show()
df.to_excel('books2_1.xlsx')

print(df)'''


'''from datetime import date ,timedelta
date1=date(2020,12,2)
#df=pd.read_excel('books.xlsx',skiprows=8,usecols='C:F',index_col='id',dtype={'id':str,'date':str})
df=pd.read_excel('books.xlsx',dtype={'id':str,'date':str})
df['name'].at[1]='you are here'
#df['date'].at[2]=date1

for i in df.index:
    df['date'].at[i] = date(date1.year+1,date1.month,date1.day)
#df.set_index('id',inplace=True)
df.to_excel('books.xlsx')
print(df)

print(df['name'])'''





#import data from database to excelfile

'''
go=sitedb()
go.lspeople()

ls_fname=[]
ls_lname=[]
ls_age=[]
ls_title=['id','fname','lname','age']

for i in range(len(ls_people)):
    ls_fname.append(ls_people[i][0])
    ls_lname.append(ls_people[i][1])
    ls_age.append(ls_people[i][2])

print(ls_lname)
print(ls_fname)
print(ls_age)
s1=pd.Series(ls_fname,index=ls_people_index,name='fname')
s2=pd.Series(ls_lname,index=ls_people_index,name='lname')
s3=pd.Series(ls_age,index=ls_people_index,name='age')
df = pd.DataFrame({s1.name: s1,s2.name:s2,s3.name:s3})
df.to_excel('test4.xlsx')

'''

s1=pd.Series([1,2,3],index=[1,2,3],name='A')
s2=pd.Series([10,20,30],index=[1,2,3],name='B')
s3=pd.Series([100,200,300],index=[1,2,3],name='C')
df=pd.DataFrame({s1.name:s1,s2.name:s2,s3.name:s3})
df.plot.bar(x=s1,y=s2)
plt.show()
df.to_excel('test3.xlsx')

#for i in range(len(ls_people)-1):
   #df=pd.Series(ls_people[i],index=ls_people_index[i])
   #print(df)


#df.to_excel('people2.xlsx')




#create other table output2 with output
'''df=pd.read_excel('output.xlsx',index_col='ID')
df.to_excel('output2.xlsx')'''


#create outtable with people table
'''
people=pd.read_excel('people.xlsx',header=1)
print(people.shape)
print(people.columns)
print(people.head(3))
print('-----------')
print(people.tail(3))
people.set_index('ID',inplace=True)
people.to_excel('output.xlsx')'''





#create table excel test1
'''df=pd.DataFrame({'id':['1','2','3','4'],'name':['sami','kadi','lb','lll']})
df.to_excel('test1.xlsx')'''