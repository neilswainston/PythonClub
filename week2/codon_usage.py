'''
PythonClub (c) University of Manchester 2018

All rights reserved.

@author: neilswainston
'''
dna_seq1 = 'ACCTGATC'
dna_seq_len = len(dna_seq1)
num_codons = dna_seq_len // 3

codon_dct = {}

for pos in range(num_codons):
    codon = dna_seq1[pos:pos + 3]

    if codon in codon_dct:
        codon_dct[codon] += 1
    else:
        codon_dct[codon] = 1

    pos = pos + 3

print(codon_dct)
