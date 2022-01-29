import pandas as pd

d=pd.read_csv('2021VAERSDATA.csv',encoding='cp1252')
d['DIED'].fillna("N",inplace=True)
deathIDs=d.loc[d.DIED=='Y','VAERS_ID']
print("total instances: ",len(d['DIED']))
print("total deaths",len(deathIDs))

maleIDs=d.loc[d.SEX=="M",'VAERS_ID']
femaleIDs=d.loc[d.SEX=="F",'VAERS_ID']

vax=pd.read_csv('2021VAERSVAX.csv',encoding='cp1252')

NOVIDs=vax.loc[vax.VAX_MANU=="NOVARTIS VACCINES AND DIAGNOSTICS",'VAERS_ID']
print("NOVIDs instances: ",len(NOVIDs))
deathNOV=set(deathIDs).intersection(NOVIDs)
print("NOVIDs deaths: ",len(deathNOV))
print("NOV death per instance",round(len(deathNOV)/len(NOVIDs),6))

MODERNAIDs=vax.loc[vax.VAX_MANU=="MODERNA",'VAERS_ID']
deathMODERNA=set(deathIDs).intersection(MODERNAIDs)

PFIZERIDs=vax.loc[vax.VAX_MANU=="PFIZER\BIONTECH",'VAERS_ID']
deathPFIZER=set(deathIDs).intersection(PFIZERIDs)

M_P=set(MODERNAIDs).intersection(PFIZERIDs)
M_Pdeath=set(deathMODERNA).intersection(deathPFIZER)
print('MODERNA+PFIZER:',len(M_P))
print('MODERNA+PFIZER death:',len(M_Pdeath))
print('MODERNA+PFIZER death per instance:',round(len(M_Pdeath)/len(M_P),6))

MODERNAIDs=set(MODERNAIDs).difference(M_P)
print("MODERNAIDs instances: ",len(MODERNAIDs))
deathMODERNA=set(deathIDs).intersection(MODERNAIDs)
print("MODERNA deaths",len(deathMODERNA))
print("MODERNA",round(len(deathMODERNA)/len(MODERNAIDs),6))
deathMODERNAmaleIDs=set(deathMODERNA).intersection(maleIDs)
print("deathMODERNAmaleIDs",len(deathMODERNAmaleIDs))
deathMODERNAfemaleIDs=set(deathMODERNA).intersection(femaleIDs)
print("deathMODERNAfemaleIDs",len(deathMODERNAfemaleIDs))
MODERNAfemaleIDs=set(MODERNAIDs).intersection(femaleIDs)
print("MODERNAfemaleIDs:",len(MODERNAfemaleIDs))
MODERNAmaleIDs=set(MODERNAIDs).intersection(maleIDs)
print("MODERNAmaleIDs:",len(MODERNAmaleIDs))
print("MODERNA female death",round(len(deathMODERNAfemaleIDs)/len(MODERNAfemaleIDs),6))
print("MODERNA male death",round(len(deathMODERNAmaleIDs)/len(MODERNAmaleIDs),6))

PFIZERIDs=set(PFIZERIDs).difference(M_P)
print("PFIZERIDs instances: ",len(PFIZERIDs))
deathPFIZER=set(deathIDs).intersection(PFIZERIDs)
print("PFIZER deaths",len(deathPFIZER))
print("PFIZER",round(len(deathPFIZER)/len(PFIZERIDs),6))
PFIZERfemaleIDs=set(PFIZERIDs).intersection(femaleIDs)
print("PFIZERfemaleIDs:",len(PFIZERfemaleIDs))
PFIZERmaleIDs=set(PFIZERIDs).intersection(maleIDs)
print("PFIZERmaleIDs:",len(MODERNAmaleIDs))
deathPFIZERmaleIDs=set(deathPFIZER).intersection(maleIDs)
deathPFIZERfemaleIDs=set(deathPFIZER).intersection(femaleIDs)
print("PFIZER female death",round(len(deathPFIZERfemaleIDs)/len(PFIZERfemaleIDs),6))
print("PFIZER male death",round(len(deathPFIZERmaleIDs)/len(PFIZERmaleIDs),6))


