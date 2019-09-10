#!/usr/bin/env python3

#
# SMS gateway
#
# use modem-manager with USB-dongle to activate.
# TODO: Figure out how to use this in combination with WEB-repl

import sys
import datetime

stop_cmd1='''cp /home/aloha/code/stop.py /home/aloha/code/boot.py'''
stop_cmd2='''ampy --port=/dev/ttyUSB0 put boot.py'''

start_cmd1='''cp /home/aloha/code/clock.py /home/aloha/code/boot.py'''
start_cmd2='''ampy --port=/dev/ttyUSB0 put boot.py'''

if __name__ == "__main__":
    with open('/var/log/sms.log', 'a') as fh:
        fh.write(str(sys.argv) + '\n')

    if sys.argv[2] == 'off':
        os.popen(stop_cmd1).read()
        os.popen(stop_cmd2).read()

    if sys.argv[2] == 'on':
        os.popen(start_cmd1).read()
        os.popen(start_cmd2).read()
