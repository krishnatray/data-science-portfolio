"""
   datetime_time.py
   
"""
#import numpy as np
from datetime  import datetime


t0 = datetime.now()

print("Begin", t0)
# loop 
for i in range(100000000):
    pass


print( "Time Taken:", datetime.now() - t0)
