#! /usr/bin/env python3

# Import modules
import argparse
import csv

# Import watermelon.gff
input = open("watermelon.gff", "r")

# Method 1: Old school

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

# Import files
gff_file   = 'watermelon.gff'
fasta_file = 'watermelon.fsa'

# Create empty list for genes
# gene_names = []

# Open the GFF file
gff = open(gff_file, 'r')

# Create argument
parse = argparse.ArgumentParser()
parse.add_argument('gff')
arg = parse.parse_args()

# Create function
with open(arg.gff) as input:
    input.read = csv.reader(input, delimiter = "\t")
    gene_names = []
    for line in input.read:
        print(line[8])
        
# Close the GFF file
gff.close()