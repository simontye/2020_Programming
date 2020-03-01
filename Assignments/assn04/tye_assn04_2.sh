#!/bin/bash

#PBS -N assn04_2
#PBS -q debug12core
#PBS -j oe
#PBS -m abe
#PBS -M simontye@uark.edu
#PBS -o BLAST.$PBS_assn04_1
#PBS -l nodes=1:ppn=12
#PBS -l walltime=00:00:30:00

cd /storage/simontye/watermelon_files

module load blast/2.6.0+

cat /storage/simontye/watermelon_files/watermelon_nt/*.fasta | makeblastdb -dbtype nucl -out nucl -title nucl

blastn -query watermelon_nt/nad4L.fasta -db nucl &> tye_assn04.2.out