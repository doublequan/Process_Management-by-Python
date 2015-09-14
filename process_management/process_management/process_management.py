import Kill_process
import time

#main loop, check process list every 3 seconds
while True:
    print time.strftime('%Y-%m-%d %X', time.localtime())
    Kill_process.killProcess("xfplay", 3)   
    time.sleep(3) 