import pandas as pd
list1=[]
data=pd.read_excel('aa.xlsm',skiprows=2,usecols='A:AX',sheet_name='Livrable_lot0')


df = pd.DataFrame(data)

id=pd.unique(df['Id'].to_list())

id=pd.unique(df['Id'].to_list())
role=df['role'].to_list()
Related_ASPICE_Sub_Process=df['Related_ASPICE_Sub_Process'].to_list()
Activity_category_TOPIC_CLEM1=df['Activity_category_TOPIC_CLEM1'].to_list()
Activity_Description_ASWP1=df['Activity_Description_ASWP1'].to_list()
Related_ASWP_Sub_Process1=df['Related_ASWP_Sub_Process1'].to_list()
CO1=df['CO1'].to_list()
Workproduct1=df['Workproduct1'].to_list()
Activity_category_TOPIC_CLEM2=df['Activity_category_TOPIC_CLEM2'].to_list()
Activity_Description_ASWP2=df['Activity_Description_ASWP2'].to_list()
Related_ASWP_Sub_Process2=df['Related_ASWP_Sub_Process2'].to_list()
CO2=df['CO2'].to_list()
Workproduct2=df['Workproduct2'].to_list()
tous=[id ,role,Related_ASPICE_Sub_Process,Activity_category_TOPIC_CLEM1,Activity_category_TOPIC_CLEM1,
  Activity_Description_ASWP1,Related_ASWP_Sub_Process1,CO1,Workproduct1,Activity_category_TOPIC_CLEM2,
  Activity_Description_ASWP2,Related_ASWP_Sub_Process2,CO2,Workproduct2]

from pandass import bd
from pandass.bd import *

go=bd.sitedb()
go.ctable1()

for i in range(len(id)):
      ls_id.clear()
      go.lsid()
      if id[i] not in ls_id:
          go.itable1(id[i] ,role[i],Related_ASPICE_Sub_Process[i],Activity_category_TOPIC_CLEM1[i],
          Activity_Description_ASWP1[i],Related_ASWP_Sub_Process1[i],CO1[i],Workproduct1[i],Activity_category_TOPIC_CLEM2[i],
          Activity_Description_ASWP2[i],Related_ASWP_Sub_Process2[i],CO2[0],Workproduct2[i])

      else:
          go.utable1(id[i], role[i], Related_ASPICE_Sub_Process[i], Activity_category_TOPIC_CLEM1[i],
                     Activity_Description_ASWP1[i], Related_ASWP_Sub_Process1[i], CO1[i], Workproduct1[i],
                     Activity_category_TOPIC_CLEM2[i],
                     Activity_Description_ASWP2[i], Related_ASWP_Sub_Process2[i], CO2[i], Workproduct2[i])

k="id ,role,Related_ASPICE_Sub_Process,Activity_category_TOPIC_CLEM,Activity_category_TOPIC_CLEM1," \
  "Activity_Description_ASWP1,Related_ASWP_Sub_Process1,CO1,Workproduct1,Activity_category_TOPIC_CLEM2" \
  ",Activity_Description_ASWP2,Related_ASWP_Sub_Process2,CO2,Workproduct2"

