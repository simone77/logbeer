logbeer
=======

A simple temperature monitor for the beer fermentation, but also for many others purpose.

###Requirements

* Raspberry Pi
* Raspbian OS
* DS18B20 1-Wire Digital Thermometer sensor


###Setup

```sh
$ sudo apt-get update
$ sudo apt-get install mysql-server python-mysqldb python-daemon lighttpd
$ mysql -u root -p password test < setup.sql
$ sudo lighttpd-enable-mod cgi
```
Configure the webserver to enable python cgi

```sh
$ sudo nano /etc/lighttpd/lighttpd.conf
```

```sh 
index-file.names            = ( "index.php", "index.html", "index.py" )
static-file.exclude-extensions = ( ".php", ".pl", ".fcgi",".py" )
```

```sh                
$ sudo nano /etc/lighttpd/conf-enabled/10-cgi.conf  
```

```sh 
cgi.assign      = (
        ".py"  => "/usr/bin/python",
)
```
