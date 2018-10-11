'''
PythonClub (c) University of Manchester 2018

All rights reserved.

@author: neilswainston
'''

dna_seq1 = 'acGCTtactaACT'
dna_seq_len = len(dna_seq1)
num_codons = dna_seq_len // 3

codon_dct = {}

for pos in range(num_codons):
    print(pos)
    codon = dna_seq1[pos] + dna_seq1[pos + 1] + dna_seq1[pos + 2]
    print(codon)
    pos = pos + 3

    if codon in codon_dct:
        codon_dct[codon] += 1
    else:
        codon_dct[codon] = 1

print(codon_dct)
