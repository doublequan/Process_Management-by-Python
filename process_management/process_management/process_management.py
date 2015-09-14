import Kill_process
import time


list = {'chrome','csrss'}


#main loop, check process list every 3 seconds
while True:
    print time.strftime('%Y-%m-%d %X', time.localtime())
    Kill_process.killProcess(list, Kill_process.START_WITH)   
    time.sleep(3) 