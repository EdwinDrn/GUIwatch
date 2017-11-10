#This program will print actual current time, and only the time.

import datetime
from datetime import datetime

class Time():

    def __init__(self, time):

        self.time = time

    def currentTime(self):
        print "%s" % self.time

variable = Time(datetime.now().time())

variable.currentTime()
