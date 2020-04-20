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
import re
from Bio import SeqIO

# Function to parse command line
def get_args():

	# Create argument parser object
	parser = argparse.ArgumentParser(description = "This script parses a GFF file")

	# Add positional arguments
	parser.add_argument("gff",   help = "Name of the GFF file")
	parser.add_argument("fasta", help = "Name of the FASTA file")

	# Parse the arguments
	return parser.parse_args()

# Function to parse fasta
def parse_fasta():
	return SeqIO.read(args.fasta, "fasta")

# Function to parse gff
def parse_gff:():
	with open(args.gff, "r") as gff_file:
    reader = csv.reader(gff_file, delimiter = "\t")
    for line in reader:
        if line[2] == "CDS":
        
            # Define start and end positions
            organism   = line[0].replace(" ", "_")
            start      = int(line[3])
            end        = int(line[4])
            strand     = line[6]
            attributes = line[8]
            
            # Print rounded output
            feature_gc = gc([start-1:end])
            
            # Extract gene name
            match = re.search("Gene\s+(\S+)\s", attributes)
            gene_name = match.group(1)
            
            # print FASTA format
            print(">" + organism + "_" + gene_name)
            print(feature_seq)
            # print(attributes)
            # print(feature_gc)
            # gc = (g_count + c_count)/len(substring))
            # gc_round = round(gc, 2)
            # print (gc_round)
            # print("{0:.2f}".format (GC))
	
# Function to calculate GC content
def gc(sequence):
	g_count = sequence.count("G")
    c_count = sequence.count("C")
	gc = (g_count + c_count)/len(sequence))
	gc_round = round(gc, 2)

# Last function to use all of these things
def main():
	genome_sequence = parse_fasta()
	parse_gff(genome_sequence.seq)
	
# Call get_args before calling main
args = get_args()
	
# Execute the program by calling main
if __name__ == "__main__":
	main()





