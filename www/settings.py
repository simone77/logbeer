#!/usr/bin/env python

import cgitb
import cgi
import MySQLdb
##
cgitb.enable()
print('Content-Type: text/html\n')
form = cgi.FieldStorage()
if(form):
    update_polling = form.getvalue("polling")
    update_correction = form.getvalue("correction")
    db2 = MySQLdb.connect(host="localhost",  user="root", passwd="password",db="test")
    cursor = db2.cursor()
    cursor.execute("""UPDATE Settings set polling=%s, correction=%s where ID=0""",(update_polling,update_correction))
    db2.commit()
    print("settings updated!")
    db2.close()


db = MySQLdb.connect(host="localhost",  user="root", passwd="password",db="test")
cursor = db.cursor()
cursor.execute("SELECT * from Settings")
#print('Content-Type: text/html\n')

row = cursor.fetchall()[0]
polling = row[1]
correction = row[2]
    
db.close()

###begin html
#print('Content-Type: text/html\n')

print("""
<html>

<head><title>Settings</title></head>

<body>
  <form method="get" action="settings2.py">
    <p>Intervallo polling: <input type="text" name="polling" value="%s"/> secondi</p>
    <p>Correzione: <input type="text" name="correction" value="%s"/> gradi</p>
    <input type="submit" value="Submit"> 
 </form>
<a href="index.html">Home</a>
</body>
</html>
""" % (polling, correction))
