dna_seq1 = 'ACC'

nucl_count = {'A': 0,
              'C': 0,
              'G': 0,
              'T': 0}

for nucl in dna_seq1:
    nucl_count[nucl] += 1


for key, value in nucl_count.items():
    print(str(key) + ' ' + str(value))
