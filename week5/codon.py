seqs = []

seqs_file = open('seqs.txt')

for line in seqs_file:
    seqs.append(line.strip())

seqs_file.close()

print(seqs)

for seq in seqs:
    # Get number of codons using integer division:
    num_of_codons = len(seq) // 3
    print(num_of_codons)

    # Initialise an empty dictionary with which to count codons:
    codon_count = {}

    # Generate range / "list" of codon start indexes:
    codon_indexes = range(0, num_of_codons * 3, 3)
    print(list(codon_indexes))

    # Loop through the codon indexes, and use the 'slice' notation to extract
    # codons from the sequence:
    for codon_index in codon_indexes:
        print(codon_index)
        codon = seq[codon_index:codon_index + 3]
        print(codon)
        
        if 'N' in codon:
            continue

        # How do we count these with our empty dictionary?
        # Hint: take a look at the 'in' operator on Slide 7 of Week 4's slides.
        if codon in codon_count:
            codon_count[codon] += 1
        else:
            codon_count[codon] = 1

        print(codon_count)
