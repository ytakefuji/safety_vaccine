import pandas as pd

d=pd.read_csv('2021VAERSDATA.csv',encoding='cp1252')
d['DIED'].fillna("N",inplace=True)
print("total instances: ",len(d['DIED']))
print("non-deaths(N) or deaths(Y)")
print(d['DIED'].value_counts())

vax=pd.read_csv('2021VAERSVAX.csv',encoding='cp1252')

NOVIDs=vax.loc[vax.VAX_MANU=="NOVARTIS VACCINES AND DIAGNOSTICS",'VAERS_ID']
print("NOVIDs instances: ",len(NOVIDs))

MODERNAIDs=vax.loc[vax.VAX_MANU=="MODERNA",'VAERS_ID']
print("MODERNAIDs instances: ",len(MODERNAIDs))

PFIZERIDs=vax.loc[vax.VAX_MANU=="PFIZER\BIONTECH",'VAERS_ID']
print("PFIZERIDs instances: ",len(PFIZERIDs))

d['DIED'].fillna("N",inplace=True)
IDs=d.loc[d.DIED=='Y','VAERS_ID']

matchedNOV=set(IDs).intersection(NOVIDs)
d['AGE_YRS'].fillna("",inplace=True)
age=[]
er=0
for i in NOVIDs:
 try:
  age.append(int(d.loc[d.VAERS_ID==i,'AGE_YRS']))
#  print(int(d.loc[d.VAERS_ID==i,'AGE_YRS']))
 except ValueError:er=er+1
print("er=",er)
mean=sum(age)/len(age)
d['AGE_YRS'].fillna(mean,inplace=True)

import matplotlib.pyplot as plt 
import numpy as np
print(len(age))
print("mean:",mean)
print("min:",min(age))
print("max:",max(age))
print(age)
plt.xlabel('age',fontsize=15)
plt.ylabel('the number of instances',fontsize=15)
counts,bins,bars=plt.hist(age,bins=50,color="gray")
df=pd.DataFrame({'age':bins[:-1],'deaths':counts})
df.to_csv('nov.csv')
plt.savefig('nov.png')
plt.show()
