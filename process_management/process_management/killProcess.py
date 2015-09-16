import win32com.client
import wmi
import time


NORMAL = 1
CONTAINS = 2
START_WITH = 3 

def killProcess(list, flag = NORMAL, logger = None):
    ''' kill the Process by the input @name
        flag   CONTAINS : kill all the precesses that contain @name
             START_WITH : kill all the precesses that start with @name
                 NORMAL : kill all the precesses that has the exactly same name with the argument @name
        return the processID and precessName of the killed process
    '''
    #form the sql query  
    names = list.copy()
    query = 'select * from Win32_Process where '
    if flag == 1:
        while len(names) != 0:
            query += 'Name LIKE "'+names.pop()+'"'
            if len(names) != 0 :
                query += ' or '   
    elif flag == 2:
        while len(names) != 0:
            query += 'Name LIKE "%'+names.pop()+'%"'
            if len(names) != 0 :
                query += ' or ' 
    elif flag == 3:
        while len(names) != 0:
            query += 'Name LIKE "'+names.pop()+'%"'
            if len(names) != 0 :
                query += ' or ' 
    else:
        return False

    #find all the process required by the query
    WMI = win32com.client.GetObject('winmgmts:')
    p_list = WMI.ExecQuery(query)

    c = wmi.WMI()
    for p in p_list:
            # filter commandline from java processes
            if p.Properties_("CommandLine").Value.find("IndexAgent"):
                      # get PID	
                      ia_pid = p.Properties_("ProcessId").Value
                      # get processes from PID
                      for process in c.Win32_Process(ProcessId = ia_pid):
                          #TODO:
                          #write log
                   #       print 'Killed ' + str(process.ProcessId) + str(process.Name)
                          if(logger != None):
                              logger.info('Killed ' + str(process.ProcessId) + '||' + str(process.Name));
                          process.Terminate()
                          #return process.ProcessId, process.Name


