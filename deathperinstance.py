import pandas as pd
import matplotlib.pyplot as plt
import sys
f=pd.read_csv('pfizer.csv')
m=pd.read_csv('moderna.csv')
w=0.8
alph=0.4
f['age']=f['age'][0:34]
m['age']=m['age'][0:34]
plt.bar(f['age']-w,f['male death per instance'],width=w,alpha=0.3,color='blue',align='center',label='pfizer male death')
plt.bar(f['age']+3*w,f['female death per instance'],width=w,alpha=0.7,color='blue',align='center',label='pfizer female death')
plt.bar(m['age']-2*w,m['male death per instance'],width=w,alpha=0.3,color='red',align='center',label='moderna male death')
plt.bar(m['age']+9*w,m['female death per instance'],width=w,alpha=0.7,color='red',align='center',label='moderna female death')
plt.axhline(y=0.0038,linewidth=1, color='k')
plt.axhline(y=0.0031,linewidth=1, color='k')
plt.autoscale(tight=True)
plt.xlabel('age',fontsize=15)
plt.ylabel('death per instance by age group',fontsize=15)
plt.legend(loc='upper left')
plt.savefig("result.png")
plt.show()
