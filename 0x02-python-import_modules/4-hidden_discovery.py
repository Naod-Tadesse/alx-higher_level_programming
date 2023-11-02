#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    dnames = dir(hidden_4)
    for name in dnames:
        if name[0:2] != "__":
            print(name)
