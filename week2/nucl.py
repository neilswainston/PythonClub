dna_seq1 = 'ACCT  GATC'

a_count = 0
c_count = 0
g_count = 0
t_count = 0
valid_count = 0

for nucl in dna_seq1:
    if nucl == 'G':
        g_count += 1
        valid_count += 1
    elif nucl == 'C':
        c_count += 1
        valid_count += 1
    elif nucl == 'A':
        a_count += 1
        valid_count += 1
    elif nucl == 'T':
        t_count += 1
        valid_count += 1

print(float(a_count) / valid_count)
print(float(c_count) / valid_count)
print(float(g_count) / valid_count)
print(float(t_count) / valid_count)
