#!/usr/bin/env python3

import sys
# import this

ords = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

print("Here is your flag:")
print("".join(chr(o) for o in ords))
