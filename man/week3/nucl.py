'''
PythonClub (c) University of Manchester 2018

All rights reserved.

@author: neilswainston
'''
dna_seq1 = 'ACCTGATC'

nucl_count = {'A': 0,
              'C': 0,
              'G': 0,
              'T': 0}

for nucl in dna_seq1:
    nucl_count[nucl] += 1


for key, value in nucl_count.items():
    print(str(key) + ' ' + str(value / len(dna_seq1)))

print('%GC ' + str((nucl_count['C'] + nucl_count['G']) / len(dna_seq1) * 100))
