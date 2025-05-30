from datetime import datetime

now = datetime.now()
print("Time:", now.strftime("%d-%m-%Y %H:%M:%S")) 
#here d, D, m, M like these input have different working 
"""from datetime import datetime
today = datetime.now()
print(f"Today is {today:%Y-%m-%d %H:%M}")"""

import time

start = time.time()

# Simulate task
time.sleep(2)

end = time.time()
print(end, start)
print("Execution time:", end - start, "seconds")
