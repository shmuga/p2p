#!/usr/bin/python
import daemon
import parser

with daemon.DaemonContext():
    parser.parse_file_infite()