#! /usr/bin/env python3

# Import modules
import argparse
import csv

# Method 1: Old school

# Import watermelon.gff
#input = open("watermelon.gff", "r")

# Create function
#for line in input:
#    value = line.split("\t", 8) # Split by tab
#    value = value[8] # Only save 9th column
#    value = value.split(";", 5) # Split by semicolon
#    value = value[0] # Only save 1st column
#    value = value.split(" ", 1) # Split by space
#    value = value[1] # Only save 2nd column
#    print(value)

# Method 2: New school

# Specify input files
gff_file   = 'watermelon.gff'
fasta_file = 'watermelon.fsa'

# Create empty list for genes
gene_names = []

# Create function
with open(gff_file, "r") as gff:
	reader = csv.reader(gff, delimiter = "\t")
	for line in reader:
	if not line:
		continue
	else:
		print(line[3], line[4])

# Close the GFF file
gff.close()