#!/usr/bin/env bash

# ESP8266 Fun!

rm boot.py

echo 'datetime = ' > boot.py
echo $(date +\(%Y,%m,%d,%H,%M,%S,%M,0,0\)) >> boot.py
echo -e "\n" >> boot.py

cat clock.py | grep -v "$(cat clock.py | head -1)" >> boot.py

ampy --port=/dev/ttyUSB0 put boot.py
ampy --port=/dev/ttyUSB0 reset
