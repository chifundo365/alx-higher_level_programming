#!/usr/bin/python3
a = ord('a')
for i in range(26):
    if chr(a) == 'e' or chr(a) == 'q':
        a += 1
        continue
    print("{}".format(chr(a)), end="")
    a += 1
