'''
libs.py

some functions


'''
import wmi

def checkProcessNum(processName):
    ''' return the number of the running input process
        if none, return 0
    '''
    p = wmi.WMI().Win32_Process(name = processName)
    return len(p)
    
    

def createProcess(processName):
    ''' create a process by the input processName
    '''
    c = wmi.WMI()
    c.Win32_Process.Create(CommandLine = processName)