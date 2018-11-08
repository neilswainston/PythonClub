dna_seq1 = 'ACCG'

count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

for nucl in dna_seq1:
  print(count[nucl])
  count[nucl] = count[nucl] + 1

print(count)
