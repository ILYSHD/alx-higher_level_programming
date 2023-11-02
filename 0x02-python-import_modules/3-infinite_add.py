#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    s = 0
    a = len(sys.argv)
    if (a < 2):
        print("{}".format(0))
    else:
        for i in range(1, a):
            s = s + int(sys.argv[i])
        print("{}".format(s))
