webalert
========

Simple python client for `webalert.davidsingleton.org`

```
from webalert import WebAlert

class DemoListener(object):

    def __init__(self):
        pass

    def hit(self):
        print "Hit!"


listener = DemoListener()
w = WebAlert("Your webalert client token", listener)
w.loop()

```

Each time your get a website visit:
```
Hit!
```