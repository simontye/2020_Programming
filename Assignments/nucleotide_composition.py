#! /usr/bin/env python3

# Open file
dna = open("/Users/simontye/Documents/Research/Courses/Programming/Assignments/dna.txt")
dna2 = dna.read()
dna2.upper()

# Create prefixes
prefix_a = "Percent A:"
prefix_t = "Percent T:"
prefix_c = "Percent C:"
prefix_g = "Percent G:"

# Calculate length of dna
length = len(dna3)

# Calculate percentages
percent_a = dna2.count("A") / length
percent_t = dna2.count("T") / length
percent_c = dna2.count("C") / length
percent_g = dna2.count("G") / length

# Print output
print(prefix_a, round(percent_a,2))
print(prefix_t, round(percent_t,2))
print(prefix_c, round(percent_c,2))
print(prefix_g, round(percent_g,2))