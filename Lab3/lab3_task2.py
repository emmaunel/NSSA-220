import sys

def main():
    filename = sys.argv[1]
    with open(filename) as f:
        for l in f:
            line = l.strip().split(" ")
            print(line)


if __name__ == "__main__":
    main()