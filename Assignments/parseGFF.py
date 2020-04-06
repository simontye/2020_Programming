#! /usr/bin/env python3

### Notes
## Single vs. multiple records
# SeqIO.parse (multiple records)
# SeqIO.read (single recrods)

## Print methods or functions or a given variable type
# print(dir(genome))

## Tests
# print(genome.description)
# print(len(genome.seq))
# print(genome.seq)

# Import modules
import argparse
import csv
from Bio import SeqIO

# Create argument parser object
parser = argparse.ArgumentParser(description = "This script parses a GFF file")

# Add positional arguments
parser.add_argument("gff",   help = "Name of the GFF file")
parser.add_argument("fasta", help = "Name of the FASTA file")

# Parse the arguments
args = parser.parse_args()

# Read and parse the fasta file
genome = SeqIO.read(args.fasta, "fasta")
genome_seq = genome.seq

# Create function
with open(args.gff, "r") as gff_file:
    reader = csv.reader(gff_file, delimiter = "\t")
    for line in reader:
        if line[2] != "CDS":
            # Define start and end positions
            start = line[3]
            end   = line[4]
            # Find substrings in genome_seq
            substring = genome_seq[(start - 1):(end - 1)]
            # Calculate GC content
            g_count = substring.count("G")
            c_count = substring.count("C")
            length  = len(substring)
            # Print output
            print((g_count + c_count)/length)