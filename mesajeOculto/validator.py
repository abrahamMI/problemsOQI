import sys

def main():
    caseName = sys.argv[1]

    # Read Input
    with open("data.in", "r") as handle:
        original_input = handle.read()
    lines = original_input.split("\n")
    val = lines[0].split()
    n = int(val[0])
    m = int(val[1])
    s = 0
    for i in range(1, len(lines)):
        parts = lines[i].split()
        if len(parts) < 2:
            continue
        length = int(parts[0])
        s += length

    #n, m = [int(value) for value in lines[0].split()]

    # Contestant's Output
    messageLenght, getLenghtTimes, validation = map(int, sys.stdin.readline().split())

    if "sub1" in caseName:
        if validation == 1 and getLenghtTimes<=n and messageLenght <= n*m:
            print(1)
            sys.exit(0)
        else:
            print(0)
            sys.exit(0)

    if "sub2" in caseName and messageLenght <= n*m:
        if validation == 1 :
            print(1)
            sys.exit(0)
        else:
            print(0)
            sys.exit(0)
    
    if "sub3" in caseName:
        if validation == 1 and getLenghtTimes <= 2*n and messageLenght <= n*m:
            print(1)
            sys.exit(0)
        else:
            print(0)
            sys.exit(0)

    if "sub4" in caseName:
        if validation == 1 and getLenghtTimes<=n and messageLenght == n+s:
            print(1)
            sys.exit(0)
        else:
            print(0)
            sys.exit(0)

    if "sub5" in caseName:
        if validation == 1 and getLenghtTimes == 0 and messageLenght == n+s:
            print(1)
            sys.exit(0)
        else:
            print(0)
            sys.exit(0)

if __name__ == '__main__':
    main()