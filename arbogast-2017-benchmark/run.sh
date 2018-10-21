#!/bin/bash

# global refinement:
filename="convergence_results_new"
echo "writing $filename..."
rm $filename
echo "# DoFs L_2_error_velocity L_2_error_fluid_pressure L_2_error_compaction_pressure" >> $filename
for r in "2" "3" "4" "5"
	do
	cp 1d_arbogast_test.prm temp.prm
	echo "refinement $r:"
	echo "subsection Mesh refinement" >>temp.prm
	echo "  set Initial global refinement = $r" >> temp.prm
	echo "end" >> temp.prm
	./aspect temp.prm | gawk '/Errors/ {print $3,$5,$7,$9}' | sed 's/,//g' >> $filename
	grep Solving output/log.txt
	rm -f temp.prm
done

