dna_seq1 = 'ACCTGATC'

gc_count = 0

for nucl in dna_seq1:
    if nucl == 'G' or nucl == 'C':
        gc_count += 1

print(gc_count / len(dna_seq1))
