#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = len(sys.argv) - 1
    result = 0
    if arguments == 0:
        print("0")
    else:
        for i in range(1, len(sys.argv)):
            result = result + int(sys.argv[i])
        print(result)
