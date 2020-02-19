#! /bin/bash

### assn03-1

for satan in {808..8008}; do echo TR-$satan; done

### assn03-2
cd /Users/simontye
nano .bash_profile
alias watermelon="cd ~/Desktop/watermelon_files"
alias example="cd ~/Desktop/example_files"
alias assignments="cd /Users/simontye/Documents/Research/Courses/Programming/Assignments"
alias doctordiatom="cat -r aja.razor.uark.edu:/storage/aja | gzip > doctordiatom.tgz"
alias bloomberg="echo frisky"
alias bootedgeedge="echo empty words, but make them sound nice"
alias biden="echo honestly, I feel bad for the guy"

### assn03-3
cd /Users/simontye/Documents/Courses/Programming/Assignments
scp -r assn/03/gene_trees simontye@razor.uark.edu:/storage/simontye/gene_trees
ssh razor.uark.edu
cd /storage/simontye/gene_trees
ls *.fasta* | wc -l
# 15085

### assn03-4
ls *.tre* | wc -l
# 14640

### assn03-5
ls *.sched* | wc -l
# 15262

### assn03-6
find . -name '*.fasta*' -type f -print | cut -d "_" -f 1 | sort -n > fasta.txt
find . -name '*.tre*' -type f -print | cut -d "_" -f 1 | sort -n > tre.txt
comm -3 fasta.txt tre.txt | wc -l
#445

### assn03-7
#! /bin/bash
for satan in *.sched
do
	if grep -cq "Program Return Code: 0" $satan
	then
		echo 0
	else
		echo 1
	fi
done > schedule.txt

scp assn03_7.sh simontye@razor.uark.edu:/storage/simontye/gene_trees
ssh razor.uark.edu
cd /storage/simontye/gene_trees
./assn03_7.sh
grep "1" schedule.txt | wc -l
# 45

### assn03-8
comm -3 fasta.txt tre.txt | cut -d "/" -f 2 > fasta_masta.txt
while read satan; do echo "write_raxml_job_script.py ${satan}_alignment.fasta > ${satan}_alignment.pbs"; done < fasta_masta.txt


