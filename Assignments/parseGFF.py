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
from collections import defaultdict

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
def parse_gff:(genome):
	# Load dictionary
	genes_with_introns = defaultdict(dict)
	# Open gff file
	with open(args.gff, "r") as gff_file:
	# Create a csv reader object
    reader = csv.reader(gff_file, delimiter = "\t")
    for line in reader:
    	if not line:
    		continue
        else:
            organism   = line[0].replace(" ", "_")
            start      = int(line[3])
            end        = int(line[4])
            strand     = line[6]
            attributes = line[8]
            
            # Rest whether it is a CDS or tRNA feature
            if feature_type == "CDS" or feature_type == "tRNA":
            	# Extract features from genome
            	feature_seq = genome[start-1:end]
            	# Reverse complement feature_seq
            	if strand == "-":
            		feature_seq = revcomp(feature_seq)
            	# Extract gene name
            	a = re.search("Gene\s+(\S+)\s+", attributes)
            	gene_name = void.group(1)
            	# Extract exon number
            	b = re.search("exon\s+(\d+)", attributes)
            	# Test whether there are multiple exons
            	if b:
            		exon_number = b.group(1)
            		# Dictionary genes_with_introns
            		# key = gene_name, value = exon_number
            		genes_with_introns[gene_name][exon_number] = feature_seq
            	else:
            		print(">" + organism + "_" + gene_name)
            		print(feature_seq)
    # Loop over genes
    for gene_id, void in genes_with_introns.items():
    	print(">" + organism + "_" + gene_id)
    	# Loop over exons
    	for exon_num, exon_seq in sorted(genes_with_introns[gene_id].items)()):
    		print(exon_seq, end = "")
    	print()
    	
# Function to calculate GC content
def gc(sequence):
	g_count = sequence.count("G")
    c_count = sequence.count("C")
	gc = (g_count + c_count)/len(sequence))
	gc_round = round(gc, 2)

#Function to translate into proteins
def codon2aa(codon):
	codon_dict = {'AAA':'K', 'AAC':'N', 'AAG':'K', 'AAT':'N', 'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 'AGA':'R', 'AGC':'S', 'AGG':'R', 'AGT':'S', 'ATA':'I', 'ATC':'I', 'ATG':'M', 'ATT':'I', 'CAA':'Q', 'CAC':'H', 'CAG':'Q', 'CAT':'H', 'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 'GAA':'E', 'GAC':'D', 'GAG':'E', 'GAT':'D', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 'TAA':'O', 'TAC':'Y', 'TAG':'O', 'TAT':'Y', 'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 'TGA':'O', 'TGC':'C', 'TGG':'W', 'TGT':'C', 'TTA':'L', 'TTC':'F', 'TTG':'L', 'TTT':'F'}
	return(codon_dict.get(codon, '-'))

# Function to reverse complement
def revcomp(seq):
	return seq.reverse_complement()

# Fucntoin to define initial files
def main():
	genome_sequence = parse_fasta()
	parse_gff(genome_sequence.seq)

# Function to call main
args = get_args()

# Function to call main
if __name__ == "__main__":
	main()





