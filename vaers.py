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
print("intersect NOV ",len(matchedNOV))
print("NOV",round(len(matchedNOV)/len(NOVIDs),3))
matchedMODERNA=set(IDs).intersection(MODERNAIDs)
print("intersect MODERNA ",len(matchedMODERNA))
print("MODERNA",round(len(matchedMODERNA)/len(MODERNAIDs),3))
matchedPFIZER=set(IDs).intersection(PFIZERIDs)
print("intersect PFIZER ",len(matchedPFIZER))
print("PFIZER",round(len(matchedPFIZER)/len(PFIZERIDs),3))

