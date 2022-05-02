import time

print("This is printed immediately.")
time.sleep(2.4)
print("This is printed after 2.4 seconds.")
import time
seconds = time.time()
print("Seconds since epoch =", seconds)	
import time

result = time.localtime(1545925769)
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)