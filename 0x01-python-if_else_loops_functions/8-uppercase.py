#!/usr/bin/python3
def uppercase(str):

    upp = ''
    for crt in str:
        if ord(crt) >= 97 and ord(crt) <= 122:
            crt = chr(ord(crt) - 32)
        upp = upp + crt
    print("{}".format(upp))
