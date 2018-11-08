seq = 'ATGCGAT'
num_of_codons = len(seq) // 3
print(num_of_codons)

codon_count = {}

codon_indexes = range(0, num_of_codons * 3, 3)

print(list(codon_indexes))

for codon_index in codon_indexes:
  print(codon_index)
  codon = seq[codon_index:codon_index+3]
  print(codon)
  print(codon_count)

