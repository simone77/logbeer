#!/usr/bin/env python

import json
import cgitb
from datetime import datetime
import calendar
import MySQLdb

##
cgitb.enable() 
<<<<<<< HEAD
db = MySQLdb.connect(host="localhost",  user="root", passwd="brewingbad",db="test")
=======
db = MySQLdb.connect(host="localhost",  user="root", passwd="password",db="test")
>>>>>>> 7427f1d5d9f063c1e828d4e757f988fd3843e51f
serie = []
cursor = db.cursor()
cursor.execute("SELECT * FROM Logtemp")

for row in cursor:
        #date_object = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
        date_object = row[0]
        dt = calendar.timegm(date_object.utctimetuple())
        lista = [dt*1000,row[1]]#moltiplicato per 1000 per avere millisecondi
        serie.append(lista)
db.close()
a = json.dumps(serie)
print('Content-Type: text/html\n')
print(a)
#{name: 'Winter 2009-2010',data: [[Date.UTC(1970,  9,  9), 0   ],[Date.UTC(1970,  9, 14), 0.15],]}]
