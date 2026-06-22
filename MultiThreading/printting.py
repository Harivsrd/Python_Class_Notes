import threading 
import time 

def f1():
    print("Hello")
    time.sleep(5)
    print("Hai")
    
def f2():
    print("Welcome")
    time.sleep(5)
    print("Bye Bye")
    
t1 = threading.Thread(target=f1)
t2 = threading.Thread(target=f2)

t1.start()
t2.start()

t1.join()
t2.join()