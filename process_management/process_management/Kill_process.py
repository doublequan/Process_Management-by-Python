﻿import win32com.client
import wmi
import time


NORMAL = 1
CONTAINS = 2
START_WITH = 3

def killProcess(name, flag = NORMAL):
    ''' kill the Process by the input @name
    the flag CONTAINS : kill all the precesses that contain @name
             START_WITH : kill all the precesses that start with @name
             NORMAL : kill all the precesses that has the exactly same name with the argument @name
    '''
    WMI = win32com.client.GetObject('winmgmts:')
    if flag == 1:
        query = 'select * from Win32_Process where Name LIKE "'+name+'"'   
    elif flag == 2:
        query = 'select * from Win32_Process where Name LIKE "%'+name+'%"'
    elif flag == 3:
        query = 'select * from Win32_Process where Name LIKE "'+name+'%"'
    p_list = WMI.ExecQuery(query)
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
