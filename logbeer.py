#!/usr/bin/env python
#version 2.0 
import logging
from datetime import date, datetime
from daemon import runner
import MySQLdb

class Logbeer():
   
    def __init__(self):
        self.delay = 120
        self.path_sensor = "/sys/bus/w1/devices/28-000004953d8b/w1_slave"
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/null'
        self.stderr_path = '/dev/null'
        self.pidfile_path =  '/var/run/logbeer.pid'
        self.pidfile_timeout = 5
        self.getTemp = False
        self.temp = 0
           
    def run(self):
        while True:
            try:#sensor polling
                fi = open(self.path_sensor,'r')
                lines = fi.readlines()
                crcLine = lines[0]
                tempLine = lines[1]
                result_list = tempLine.split("=")
                if crcLine.find("NO") > -1:
                    logger.error("CRC error")
                    self.getTemp = False
                else:
                    self.temp = float(result_list[-1].strip())/1000
                    self.getTemp = True
                    #logger.debug("Sensor found")
                    #logger.debug("Temperature=%s" %(self.temp))
            except IOError:
                logger.error("Sensor not found")
                print("Sensor not found")
            except Exception as e:
                logger.error(e.message)
            ###db query
            try:
                db = MySQLdb.connect(host="localhost",  user="root", passwd="password",db="test")
                cursor = db.cursor()
                cursor.execute("SELECT * FROM Settings WHERE ID=0")
                row = cursor.fetchall()[0]
                self.delay = row[1]
                correction = row[2]
                logger.debug("Correction=%s" %(correction))
                if self.getTemp:
                    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    cursor.execute("INSERT INTO Logtemp(Data, Temp) VALUES(%s,%s)",(now, self.temp))
                    db.commit()
                    db.close()
            except MySQLdb.Error as e:
                self.delay = 120
                logger.error("Db error")
                print("db error:",e.args[0])
            except Exception as e:
                logger.error(e.message)
            logger.debug("Polling delay=%s" %(self.delay))
            time.sleep(self.delay)

logbeer = Logbeer()
#
logger = logging.getLogger("Logbeer")
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler = logging.FileHandler("/var/log/logbeer.log")
handler.setFormatter(formatter)
logger.addHandler(handler)
##
daemon_runner = runner.DaemonRunner(logbeer)
daemon_runner.daemon_context.files_preserve=[handler.stream]
daemon_runner.do_action()
