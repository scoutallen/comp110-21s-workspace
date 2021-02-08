"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730342553"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint
a: int = randint(1, 4)

if a == 1:
    print("Your fortune cookie says...")
    print("A very wise cat will bestow a kiss upon your weary head")
    print("Now, go spread positive vibes!")
else:
    if a == 2:
        print("Your fortune cookie says...")
        print("The sun will set upon your enemy's last day.")
        print("Now, go spread positive vibes!")
    else:
        if a == 3: 
            print("Your fortune cookie says...")
            print("Your friend's mother will make a delicious stew.")
            print("Now, go spread positive vibes!")
        else: 
            print("Your fortune cookie says...")
            print("You will witness a child wearing a rockin pair of kicks.")
            print("Now, go spread positive vibes!")

