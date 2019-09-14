#!/usr/bin/env bash

# ===================================
# ESP8266 Fun!
# ===================================

cp apa102.py boot.py

ampy --port=/dev/ttyUSB0 ls
ampy --port=/dev/ttyUSB0 put boot.py
ampy --port=/dev/ttyUSB0 reset

