clogger
===========

Description
----------
Python-based colorful logger for command line. 
It outputs colorful logs to stdout + the same log to syslog output file (ex. /var/log/syslog)
Output color depends on the log level. 
For syslog output you can also set syslog tag using `-t` option (see picture below)

Install
--------
```
cp clogger.py /usr/bin/clogger
```

Usage (see picture)
------
![pipeline10](https://raw.githubusercontent.com/xmementoit/clogger/master/clogger.png)

Options
------
```
-t (--tag)   - set syslog tag (default: colorlog)
-l (--level) - set log level from this list: DEBUG, INFO, WARN, ERR, CRIT (default: INFO)
```

Enjoy!
-------

