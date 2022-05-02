import time
while True:
    
        input("Press Enter to continue and ctrl+C to exit the stopwatch")
        start_time=time.time()
        print("Stopwatch has started")
        while True:
            print("Time elapsed:",round(time.time()-start_time,0),'secs',end='\n')
            time.sleep(1)
            
            