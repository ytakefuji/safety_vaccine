import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

d=pd.read_csv('2021VAERSDATA.csv',encoding='cp1252')
d['DIED'].fillna("N",inplace=True)
print("total instances: ",len(d['DIED']))
print("non-deaths(N) or deaths(Y)")
print(d['DIED'].value_counts())

vax=pd.read_csv('2021VAERSVAX.csv',encoding='cp1252')

symptoms=pd.read_csv('2021VAERSSYMPTOMS.csv',encoding='cp1252')
anaphyIDs=symptoms.loc[symptoms.SYMPTOM1=="Anaphylactic reaction",'VAERS_ID']
print("No of anyphylactic reaction:",len(anaphyIDs))
cardiacIDs=symptoms.loc[symptoms.SYMPTOM1=="Cardiac arrest",'VAERS_ID']
print("No of cardiac arrests:",len(cardiacIDs))

NOVIDs=vax.loc[vax.VAX_MANU=="NOVARTIS VACCINES AND DIAGNOSTICS",'VAERS_ID']
print("NOVIDs instances: ",len(NOVIDs))

MODERNAIDs=vax.loc[vax.VAX_MANU=="MODERNA",'VAERS_ID']
print("MODERNAIDs instances: ",len(MODERNAIDs))

PFIZERIDs=vax.loc[vax.VAX_MANU=="PFIZER\BIONTECH",'VAERS_ID']
print("PFIZERIDs instances: ",len(PFIZERIDs))

anaphyMODERNA=set(MODERNAIDs).intersection(anaphyIDs)
print("anaphyMODERNA:",len(anaphyMODERNA))
cardiacMODERNA=set(MODERNAIDs).intersection(cardiacIDs)
print("cardiacMODERNA:",len(cardiacMODERNA))

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

MODERNAANAPHY=set(MODERNAIDs).intersection(anaphyIDs)
print("MODERNAanaphy:",len(MODERNAANAPHY))

maleMODERNAANAPHY=set(MODERNAANAPHY).intersection(maleIDs)
print("maleMODERNAANAPHY",len(maleMODERNAANAPHY))

femaleMODERNAANAPHY=set(MODERNAANAPHY).intersection(femaleIDs)
print("femaleMODERNAANAPHY",len(femaleMODERNAANAPHY))

deathMODERNAANAPHY=set(deathMODERNA).intersection(anaphyIDs)
print("deathMODERNAanaphy:",len(deathMODERNAANAPHY))
maledeathMODERNAanaphy=set(deathMODERNAANAPHY).intersection(maleIDs)
print("male deathMODERNAanaphy",len(maledeathMODERNAanaphy))
'''

d['AGE_YRS'].fillna("",inplace=True)
maledeathage=[]
er=0
for i in maledeathPFIZER:
 try:
  maledeathage.append(int(d.loc[d.VAERS_ID==i,'AGE_YRS']))
 except ValueError:er=er+1
print("male death age unknown =",er)
print("male death age known=",len(maledeathage))
print("min:",min(maledeathage))
print("max:",max(maledeathage))

femaledeathage=[]
er=0
for i in femaledeathPFIZER:
 try:
  femaledeathage.append(int(d.loc[d.VAERS_ID==i,'AGE_YRS']))
 except ValueError:er=er+1
print("female death age unknown=",er)
print("female death age known=",len(femaledeathage))
print("min:",min(femaledeathage))
print("max:",max(femaledeathage))

maleage=[]
er=0
for i in malePFIZER:
 try:
  maleage.append(int(d.loc[d.VAERS_ID==i,'AGE_YRS']))
 except ValueError:er=er+1
print("male age unknown=",er)
print("male age known=",len(maleage))
print("min:",min(maleage))
print("max:",max(maleage))

femaleage=[]
er=0
for i in femalePFIZER:
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
df.to_csv('pfizer.csv')
print("pfizer.csv file was successfully created")
'''
