#! /usr/bin/env python3

input = open("watermelon.gff", "r")

for line in input:
    value = line.split("\t", 8) # Split by tab
    value = value[8] # Only save 9th column
    value = value.split(";", 5) # Split by semicolon
    value = value[0] # Only save 1st column
    value = value.split(" ", 1) # Split by space
    value = value[1] # Only save 2nd column
    print(value)