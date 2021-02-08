"""An exercise in remainders and boolean logic."""

__author__ = "730342553"

wonder: int = int(input("Enter an int: "))
if ((wonder % 7) == 0) and ((wonder % 2) == 0):
    print("TAR HEELS")
else:
    if ((wonder % 7) == 0):
        print("HEELS")
    else: 
        if ((wonder % 2) == 0):
            print("TAR")
        else:
            print("CAROLINA")

