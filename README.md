# safety_vaccine 

This is under review.

The latest data of VAERS (Vaccine Adverse Event Reporting System) dataset is 
available at:

https://vaers.hhs.gov/eSubDownload/index.jsp?fn=2021VAERSData.zip

# set operations
vaers.py shows a good example of intersection operation. 
The following figure shows what is intersection operation.

<img src="set.jpg" width=700 height=560 >

# How to run vaers.py

<pre>
1. Unzip 2021VAERSData.zip file
2. Run vaers.py program
$ python vaers.py
total instances:  677514
total deaths 8926
NOVIDs instances:  1202
NOVIDs deaths:  4
NOV death per instance 0.003328
MODERNAIDs instances:  310812
MODERNA deaths 3652
MODERNA 0.01175
PFIZERIDs instances:  298225
PFIZER deaths 3973
PFIZER 0.013322
MODERNA+PFIZER: 905
MODERNA+PFIZER death: 4
MODERNA+PFIZER death per instance: 0.00442
MODERNAIDs instances:  299195
MODERNA deaths 3648
MODERNA 0.012193
PFIZERIDs instances:  283061
PFIZER deaths 3969
PFIZER 0.014022
</pre>
# How to run pfizerAge.py to generate a pfizer.csv file.
<pre>
$ python pfizerAge.py
</pre>

# How to run modernaAge.py to generate a moderna.csv file.
<pre>
$ python modernaAge.py
</pre>

# How to calculate safety thresholds of PFIZER and MODERNA vaccines by age
<pre>
$ python deathperinstance.py
</pre>

# Subtraction operation

set(A).difference(B)

# Union operation

set(A).union(B)

# Symmetric difference (ExclusiveOR)

set(A).symmetric_difference(B)

