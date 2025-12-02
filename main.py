import sys

from src import *


def main():
    if len(sys.argv) < 2:
        print("day not specified. exiting.")
        sys.exit(0)
    run = sys.argv[1]
    match run:
        case "day1" | "1":
            day1.entry()
        case "day2" | "2":
            day2.entry()
        case _:
            print("day not available yet.")


if __name__ == "__main__":
    main()
