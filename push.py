import os
i = 3
while i:
    i -= 1
    import time
    time.sleep(30)
    os.system("git push origin master")
