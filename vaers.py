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
print("NOV death per instance",round(len(deathNOV)/len(NOVIDs),6))

MODERNAIDs=vax.loc[vax.VAX_MANU=="MODERNA",'VAERS_ID']
#print("MODERNAIDs instances: ",len(MODERNAIDs))
deathMODERNA=set(IDs).intersection(MODERNAIDs)
#print("MODERNA deaths",len(deathMODERNA))
#print("MODERNA",round(len(deathMODERNA)/len(MODERNAIDs),6))

PFIZERIDs=vax.loc[vax.VAX_MANU=="PFIZER\BIONTECH",'VAERS_ID']
#print("PFIZERIDs instances: ",len(PFIZERIDs))
deathPFIZER=set(IDs).intersection(PFIZERIDs)
#print("PFIZER deaths",len(deathPFIZER))
#print("PFIZER",round(len(deathPFIZER)/len(PFIZERIDs),6))

M_P=set(MODERNAIDs).intersection(PFIZERIDs)
M_Pdeath=set(deathMODERNA).intersection(deathPFIZER)
print('MODERNA+PFIZER:',len(M_P))
print('MODERNA+PFIZER death:',len(M_Pdeath))
print('MODERNA+PFIZER death per instance:',round(len(M_Pdeath)/len(M_P),6))

MODERNAIDs=set(MODERNAIDs).difference(M_P)
print("MODERNAIDs instances: ",len(MODERNAIDs))
deathMODERNA=set(IDs).intersection(MODERNAIDs)
print("MODERNA deaths",len(deathMODERNA))
print("MODERNA",round(len(deathMODERNA)/len(MODERNAIDs),6))

PFIZERIDs=set(PFIZERIDs).difference(M_P)
print("PFIZERIDs instances: ",len(PFIZERIDs))
deathPFIZER=set(IDs).intersection(PFIZERIDs)
print("PFIZER deaths",len(deathPFIZER))
print("PFIZER",round(len(deathPFIZER)/len(PFIZERIDs),6))


