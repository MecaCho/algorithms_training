import os
i = 300
while i:
    i -= 1
    import time
#    time.sleep(10)
    os.system("git push origin master")
    time.sleep(30)
