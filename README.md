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
$ sudo apt-get install python-mysqldb python-daemon lighttpd
$ mysql -u root -p password test < setup.sql
```
