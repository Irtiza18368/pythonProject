import time

def countdown(t: int) -> None:
    while t:
        mins: int
        secs: int
        mins, secs = divmod(t, 60)
        
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        
        time.sleep(1)
        t -= 1
    
    print("Fire in the hole!!")  

t = int(input("Enter the time in seconds"))

countdown(t)