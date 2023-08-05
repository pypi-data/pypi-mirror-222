import time
from taglogger import tlog
from os import environ


def tlog_line(debug_mode: str):
    environ["DEBUG"] = debug_mode   
    tlog("traffic", "There is a traffic jam")
    tlog("weather", "Rain is coming")


def test_tlog():
    tlog_line("traffic")
    tlog_line("traffic:l") # location
    tlog_line("traffic:t") # time
    time.sleep(1)
    tlog_line("traffic:e") # elapsed time
    tlog_line("traffic:tel") # elapsed time
    tlog_line("weather:tel") # elapsed time
    
if __name__ == "__main__":
    test_tlog()
