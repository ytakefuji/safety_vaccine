import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

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
DEATHIDs=d.loc[d.DIED=='Y','VAERS_ID']

maleIDs=d.loc[d.SEX=="M",'VAERS_ID']
femaleIDs=d.loc[d.SEX=="F",'VAERS_ID']

maleMODERNA=set(MODERNAIDs).intersection(maleIDs)
femaleMODERNA=set(MODERNAIDs).intersection(femaleIDs)
print("male MODERNA",len(maleMODERNA))
print("female MODERNA",len(femaleMODERNA))


deathMODERNA=set(DEATHIDs).intersection(MODERNAIDs)
maledeathMODERNA=set(deathMODERNA).intersection(maleIDs)
femaledeathMODERNA=set(deathMODERNA).intersection(femaleIDs)

print("male death per instance:",len(maledeathMODERNA)/len(maleMODERNA))
print("female death per instance:",len(femaledeathMODERNA)/len(femaleMODERNA))

d['AGE_YRS'].fillna("",inplace=True)
maledeathage=[]
er=0
for i in maledeathMODERNA:
 try:
  maledeathage.append(int(d.loc[d.VAERS_ID==i,'AGE_YRS']))
 except ValueError:er=er+1
print("male death age unknown =",er)
print("male death age known=",len(maledeathage))
print("min:",min(maledeathage))
print("max:",max(maledeathage))

femaledeathage=[]
er=0
for i in femaledeathMODERNA:
 try:
  femaledeathage.append(int(d.loc[d.VAERS_ID==i,'AGE_YRS']))
 except ValueError:er=er+1
print("female death age unknown=",er)
print("female death age known=",len(femaledeathage))
print("min:",min(femaledeathage))
print("max:",max(femaledeathage))

maleage=[]
er=0
for i in maleMODERNA:
 try:
  maleage.append(int(d.loc[d.VAERS_ID==i,'AGE_YRS']))
 except ValueError:er=er+1
print("male age unknown=",er)
print("male age known=",len(maleage))
print("min:",min(maleage))
print("max:",max(maleage))

femaleage=[]
er=0
for i in femaleMODERNA:
 try:
  femaleage.append(int(d.loc[d.VAERS_ID==i,'AGE_YRS']))
 except ValueError:er=er+1
print("female age unknown=",er)
print("female age known=",len(femaleage))
print("min:",min(femaleage))
print("max:",max(femaleage))

counts,bins,bars=plt.hist([maleage,femaleage,maledeathage,femaledeathage],bins=50,alpha=0.5,label=['male','female','male death','female death'])
df=pd.DataFrame({'age':bins[:-1],'male':counts[0],'female':counts[1],'male death':counts[2],'female death':counts[3]})
counts,bins,bars=plt.hist([maleage,maledeathage],bins=50,alpha=0.5,label=['male','male death'])
df['male death per instance']=df['male death']/df['male']
df['female death per instance']=df['female death']/df['female']
df.to_csv('moderna.csv')
print("moderna.csv file was successfully created")
