'''
libs.py

some functions


'''
import wmi

def checkProcessNum(processName):
    ''' return the number of the running input process
        if none, return 0
    '''
    num = 0
    c = wmi.WMI()
    for process in c.Win32_Process(name = processName):
        num += 1
    return num

def createProcess(processName):
    ''' create a process by the input processName
    '''
    c = wmi.WMI()
    c.Win32_Process.Create(CommandLine = processName)