#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_len = len(sys.argv)
    print("{}: {}".format(arg_len - 1, "arguments" if arg_len == 0 or arg_len > 1 else "argument"))
    for i in range(1, len(sys.argv)):
        print("{} {}".format(i, sys.argv[i]))
