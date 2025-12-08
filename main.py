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
        case "day3" | "3":
            day3.entry()
        case "day4" | "4":
            day4.entry()
        case "day5" | "5":
            day5.entry()
        case "day6" | "6":
            day6.entry()
        case "day7" | "7":
            day7.entry()
        case _:
            print("day not available yet.")


if __name__ == "__main__":
    main()
