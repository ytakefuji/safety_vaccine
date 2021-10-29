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
total instances:  596615
total deaths 7652
NOVIDs instances:  617
NOVIDs deaths:  3
NOV death per instance 0.005
MODERNAIDs instances:  287768
MODERNA deaths 3234
MODERNA 0.011
PFIZERIDs instances:  261371
PFIZER deaths 3377
PFIZER 0.013
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



