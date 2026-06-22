import threading
import time 
import concurrent.futures 

def multiply(x):
    return 2 * x 

l = [10, 20, 30, 40] 

with concurrent.futures.ThreadPoolExecutor(max_workers=2) as e:
    res = e.map(multiply,l)
    
    
for x in res:
    print(x)