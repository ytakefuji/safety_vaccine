import pandas as pd

d=pd.read_csv('2021VAERSDATA.csv',encoding='cp1252')
d['DIED'].fillna("N",inplace=True)
IDs=d.loc[d.DIED=='Y','VAERS_ID']
print("total instances: ",len(d['DIED']))
print("total deaths",len(IDs))

vax=pd.read_csv('2021VAERSVAX.csv',encoding='cp1252')

NOVIDs=vax.loc[vax.VAX_MANU=="NOVARTIS VACCINES AND DIAGNOSTICS",'VAERS_ID']
print("NOVIDs instances: ",len(NOVIDs))
deathNOV=set(IDs).intersection(NOVIDs)
print("NOVIDs deaths: ",len(deathNOV))
print("NOV death per instance",round(len(deathNOV)/len(NOVIDs),3))

MODERNAIDs=vax.loc[vax.VAX_MANU=="MODERNA",'VAERS_ID']
print("MODERNAIDs instances: ",len(MODERNAIDs))
deathMODERNA=set(IDs).intersection(MODERNAIDs)
print("MODERNA deaths",len(deathMODERNA))
print("MODERNA",round(len(deathMODERNA)/len(MODERNAIDs),3))

PFIZERIDs=vax.loc[vax.VAX_MANU=="PFIZER\BIONTECH",'VAERS_ID']
print("PFIZERIDs instances: ",len(PFIZERIDs))
deathPFIZER=set(IDs).intersection(PFIZERIDs)
print("PFIZER deaths",len(deathPFIZER))
print("PFIZER",round(len(deathPFIZER)/len(PFIZERIDs),3))

