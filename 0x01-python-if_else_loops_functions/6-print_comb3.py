#!/usr/bin/python3
for i in range(9):
    for j in range(i+1, 10):
        if i == 8:
            print("{}{}".format(i, j))
        else:
            if int(str(i) + str(j)) < int(str(j) + str(i)):
                print("{}{}".format(i, j), end=", ")
            else:
                print("{}{}".format(j, i), end=", ")
