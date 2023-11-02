#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    content = dir(hidden_4)
    for names in content:
        if names[:2] != "__":
            print("{}".format(names))
