import pandas as pd
import sys
import subprocess as sp
ages=['18-29','30-49','50-64','65-79','80+']
for i in ages:
 sp.call('python vuv.py '+i,shell=True) 
import cv2

for i in ages:
 cv2.imshow(i,cv2.imread(i+'.png'))
cv2.waitKey(0)
