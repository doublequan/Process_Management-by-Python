import win32com.client
import wmi
import time

#kill the Process that CONTAINS the input $name
def killProcessContain(name):
    WMI = win32com.client.GetObject('winmgmts:')     
    p_list = WMI.ExecQuery('select * from Win32_Process where Name LIKE "'+name+'%"')
    c = wmi.WMI()
    for p in p_list:
            # filter commandline from java processes
            if p.Properties_("CommandLine").Value.find("IndexAgent"):
                      # get PID	
                      ia_pid = p.Properties_("ProcessId").Value
                      # get processes from PID
                      for process in c.Win32_Process(ProcessId=ia_pid):
                          #TODO:
                          #write log
                          print 'Killed ' + str(process.ProcessId) + str(process.Name)
                          process.Terminate()
                          #print process.ProcessId, process.Name
                      #for ia_p in ia_process:
                            # Terminate process
                             #r = ia_p.Terminate()

#main loop, check process list every 3 seconds
while True:
    print time.strftime('%Y-%m-%d %X', time.localtime())
    killProcessContain("xfplay")   
    time.sleep(3) 