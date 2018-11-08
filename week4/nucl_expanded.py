dna_seq1 = 'ACC'

nucl_count = {'A': 0,
              'C': 0,
              'G': 0,
              'T': 0}

# Iterate through each nucleotide in turn:
for nucl in dna_seq1:
    # Print current state of nucl_count dictionary:
    print('Dictionary at start of loop: ' + str(nucl_count))

    # Print current value of nucl:
    print('Current nucl: ' + nucl)

    # Print current count of nucl from dictionary:
    current_count_of_nucl = nucl_count[nucl]
    print('Current count of ' + nucl + ': ' + str(current_count_of_nucl))

    # Update count of nucl:
    new_count_of_nucl = current_count_of_nucl + 1
    print('Updated count of ' + nucl + ': ' + str(new_count_of_nucl))

    # Update dictionary with new count for nucl:
    nucl_count[nucl] = new_count_of_nucl

    # Print updated state of nucl_count dictionary:
    print('Dictionary at end of loop: ' + str(nucl_count))

    # Print new line:
    print()


# Print final nucleotide counts using the 'items' method to iterate
# through dictionaries:
for key, value in nucl_count.items():
    print(str(key) + ' ' + str(value))
