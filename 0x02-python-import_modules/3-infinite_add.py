#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_len = len(sys.argv)
    result = 0
    for i in range(1, arg_len):
        result += int(sys.argv[i])
print("{}".format(result))
