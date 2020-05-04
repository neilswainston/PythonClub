'''
PythonClub (c) University of Manchester 2018

All rights reserved.

@author: neilswainston
'''
dna_seq1 = 'ACCTGATC'
num_codons = len(dna_seq1) // 3

codon_dct = {}

for pos in range(0, num_codons * 3, 3):
    codon = dna_seq1[pos:pos + 3]

    if codon in codon_dct:
        codon_dct[codon] += 1
    else:
        codon_dct[codon] = 1

print(codon_dct)
