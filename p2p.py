#!/usr/bin/python
import daemon
import parser

if __name__ == '__main__':
# with daemon.DaemonContext():
    parser.parse_file_infite()