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
print("No of anaphylactic reaction:",len(anaphyIDs))
print(symptoms.SYMPTOM1.value_counts())

cardiacarrIDs=symptoms.loc[symptoms.SYMPTOM1=="Cardiac arrest",'VAERS_ID']
print("No of cardiac arrests:",len(cardiacarrIDs))
cardiacfailIDs=symptoms.loc[symptoms.SYMPTOM1=="Cardiac failure",'VAERS_ID']
print("No of cardiac failures:",len(cardiacfailIDs))

NOVIDs=vax.loc[vax.VAX_MANU=="NOVARTIS VACCINES AND DIAGNOSTICS",'VAERS_ID']
print("NOVIDs instances: ",len(NOVIDs))

MODERNAIDs=vax.loc[vax.VAX_MANU=="MODERNA",'VAERS_ID']
print("MODERNAIDs instances: ",len(MODERNAIDs))

PFIZERIDs=vax.loc[vax.VAX_MANU=="PFIZER\BIONTECH",'VAERS_ID']
print("PFIZERIDs instances: ",len(PFIZERIDs))

anaphyPFIZER=set(anaphyIDs).intersection(PFIZERIDs)
print("anaphyPFIZER:",len(anaphyPFIZER))
cardiacarrPFIZER=set(cardiacarrIDs).intersection(PFIZERIDs)
print("cardiac arrests PFIZER:",len(cardiacarrPFIZER))
cardiacfailPFIZER=set(cardiacfailIDs).intersection(PFIZERIDs)
print("cardiac failures PFIZER:",len(cardiacfailPFIZER))

anaphyMODERNA=set(anaphyIDs).intersection(MODERNAIDs)
print("anaphyMODERNA:",len(anaphyMODERNA))
cardiacarrMODERNA=set(cardiacarrIDs).intersection(MODERNAIDs)
print("cardiac arrests MODERNA:",len(cardiacarrMODERNA))
cardiacfailMODERNA=set(cardiacfailIDs).intersection(MODERNAIDs)
print("cardiac failures MODERNA:",len(cardiacfailMODERNA))

d['DIED'].fillna("N",inplace=True)
DEATHIDs=d.loc[d.DIED=='Y','VAERS_ID']

deaths=symptoms.loc[symptoms.VAERS_ID.isin(DEATHIDs)]
print(deaths.SYMPTOM1.value_counts())

maleIDs=d.loc[d.SEX=="M",'VAERS_ID']
femaleIDs=d.loc[d.SEX=="F",'VAERS_ID']

malePFIZER=set(PFIZERIDs).intersection(maleIDs)
femalePFIZER=set(PFIZERIDs).intersection(femaleIDs)
print("male PFIZER",len(malePFIZER))
print("female PFIZER",len(femalePFIZER))


deathPFIZER=set(DEATHIDs).intersection(PFIZERIDs)
maledeathPFIZER=set(deathPFIZER).intersection(maleIDs)
femaledeathPFIZER=set(deathPFIZER).intersection(femaleIDs)

print("male death per instance:",len(maledeathPFIZER)/len(malePFIZER))
print("female death per instance:",len(femaledeathPFIZER)/len(femalePFIZER))

PFIZERANAPHY=set(PFIZERIDs).intersection(anaphyIDs)
print("PFIZERanaphy:",len(PFIZERANAPHY))
malePFIZERANAPHY=set(PFIZERANAPHY).intersection(maleIDs)
print("malePFIZERANAPHY",len(malePFIZERANAPHY))

femalePFIZERANAPHY=set(PFIZERANAPHY).intersection(femaleIDs)
print("femalePFIZERANAPHY",len(femalePFIZERANAPHY))

deathPFIZERANAPHY=set(deathPFIZER).intersection(anaphyIDs)
print("deathPFIZERanaphy:",len(deathPFIZERANAPHY))
maledeathPFIZERanaphy=set(deathPFIZERANAPHY).intersection(maleIDs)
print("male deathPFIZERanaphy",len(maledeathPFIZERanaphy))


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
