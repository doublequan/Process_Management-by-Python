import Kill_process
import time
import logging
import logging.handlers

#log file
LOG_FILE = 'p_m_log.log'
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 1024*1024, backupCount = 5)
fmt = '%(asctime)s - %(message)s'
formatter = logging.Formatter(fmt)
handler.setFormatter(formatter)

logger = logging.getLogger('p_m_log')
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

#use set to store the key words
list = {'xfplay','xfp2p'}

logger.info('Process_Management.exe START------')
#main loop, check process list every 3 seconds
while True:
#    print time.strftime('%Y-%m-%d %X', time.localtime())
    Kill_process.killProcess(list, Kill_process.START_WITH, logger)   
    time.sleep(3) 