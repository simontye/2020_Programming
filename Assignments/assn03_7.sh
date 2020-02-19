#! /bin/bash

### assn03_7.sh

for satan in *.sched
do
	if grep -q "Program Return Code: 0" $satan;
	then
		echo 0
	else
		echo 1
	fi
done > schedule.txt