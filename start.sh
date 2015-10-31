#!/bin/bash
kill $(ps aux | grep 'p2p.py' | awk '{print $2}'| head -n 1)
./p2p.py