#!/usr/bin/env python3

# Simple script to play around with the ord and chr functions

char = input("Please type in any character: ")
print("The UTF-8 value of " + char + " is " + str(ord(char)) + "\n")

utf = input("Please type in a whole number value: ")
print("The UTF-8 character with a value of " + str(utf) + " is " + chr(int(utf)) + "\n")
