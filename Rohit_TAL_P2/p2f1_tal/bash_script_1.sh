x3dna_utils cp_std BDNA
for i in {1..57};
do
	emDNA-cli \
	--x3DNA-bp-step-params-input=p2f1_shift${i}.par \
	--DNA-external-model=dimer_optimization.ff \
	--hold-last-bp \
	--frozen-steps=1:13,134:146 \
	--energy-progress \
	--output-name=p2f1_shift${i}_dimer
	mv p2f1_shift${i}_dimer_opt.txt p2f1_shift${i}_dimer_opt.par
	rebuild -atomic p2f1_shift${i}_dimer_opt.par p2f1_shift${i}_dimer_opt.pdb
	mv ref_frames.dat p2f1_shift${i}_dimer_opt.dat

	emDNA-cli \
	--x3DNA-bp-step-params-input=p2f1_shift${i}.par \
	--DNA-external-model=tetramer_optimization.ff \
	--hold-last-bp \
	--frozen-steps=1:13,134:146 \
	--energy-progress \
	--output-name=p2f1_shift${i}_tetramer
	mv p2f1_shift${i}_tetramer_opt.txt p2f1_shift${i}_tetramer_opt.par
	rebuild -atomic p2f1_shift${i}_tetramer_opt.par p2f1_shift${i}_tetramer_opt.pdb
	mv ref_frames.dat p2f1_shift${i}_tetramer_opt.dat
done
rm Atomic*

