#!/usr/bin/env python
import base64,sys

while True:
    line = sys.stdin.readline()
    if line == "":
        break
    line = line.rstrip("\n")
    print "$SHA256$" + base64.b64decode(line).encode("hex")
