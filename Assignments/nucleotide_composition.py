#! /usr/bin/env python3

# Change working directory
import os
os.chdir(/Users/simontye/Documents/Research/Courses/Programming/Assignments/)

# Open file
dna = "dna.txt"
dna2 = open(dna, "r")
dna3 = dna2.read()
dna3.upper()

# Create prefixes
prefix_a = "Percent A:"
prefix_t = "Percent T:"
prefix_c = "Percent C:"
prefix_g = "Percent G:"

# Calculate length of dna
length = len(dna3)

# Calculate percentages
percent_a = dna3.count("A") / length
percent_t = dna3.count("T") / length
percent_c = dna3.count("C") / length
percent_g = dna3.count("G") / length

# Print output
print(prefix_a, round(percent_a,2))
print(prefix_t, round(percent_t,2))
print(prefix_c, round(percent_c,2))
print(prefix_g, round(percent_g,2))