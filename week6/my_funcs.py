def greeting(name):
    print('Hello ' + name)


greeting('Bob')
greeting('Doris')


def power(val, exponent=2):
    my_power = val ** exponent
    return my_power


res = power(5, 2)
print(res)

res = power(5, 3)
print(res)

res = power(6)
print(res)


def read_file(filename):
    seqs = []

    my_file = open(filename, 'r')

    for curr_line in my_file:
        my_line = curr_line.strip()
        seqs.append(my_line)

    my_file.close()

    return seqs


my_seqs = read_file('seqs.txt')
print(my_seqs)

for seq in my_seqs:
    calc_codon_usage(seq)
