import pandas as pd
import sys
d=pd.read_csv('Rates_of_COVID-19_Cases_or_Deaths_by_Age_Group_and_Vaccination_Status.csv')
months=d.month.unique()
days=[]
#age=18-29,30-49,50-64,65-79,80+
if len(sys.argv)==1: 
 print('18-29,30-49,50-64,65-79,80+')
 sys.exit(0)
else:
 age=sys.argv[1]
for i in months:
 for j in range(4):
  days.append(i+'.'+str(j))
 vwo=d.loc[(d.outcome=='death') & (d['Age group']==age),'Vaccinated with outcome']
 fvp=d.loc[(d.outcome=='death') & (d['Age group']==age),'Fully vaccinated population']
 v=vwo/fvp
 uwo=d.loc[(d.outcome=='death') & (d['Age group']==age),'Unvaccinated with outcome']
 up=d.loc[(d.outcome=='death') & (d['Age group']==age),'Unvaccinated population']
 u=uwo/up
#print(len(days),len(vwo),len(fvp),len(uwo),len(up))
import matplotlib.pyplot as plt
import numpy as np
plt.plot(days,v,'-k')
plt.plot(days,u,'--k')
plt.xticks(days[::4],rotation=90)
plt.legend(('vaccinated','unvaccinated'))
plt.title('COVID-19 mortality for '+age+' age group')
plt.savefig('result.png',bbox_inches='tight')
plt.show()
