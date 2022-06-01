#!/bin/bash

echo 'starts'

echo `ssh -i id_ed25519 -p 50000 fumiya@raspberrypi.local python test/dht11-test.py`
echo 'in raspi'
