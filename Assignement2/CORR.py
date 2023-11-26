from Bio import SeqIO

def hamming_distance(s1, s2):
    return sum([1 if s1[i]!=s2[i] else 0 for i in range(len(s1))])

def error_correct(reads):
    corrections = []
    correct_reads, incorrect_reads = [], []
    reverse_pattern={"A": "T", "T": "A", "C": "G", "G": "C"}

    for r in reads:
        reverse_r = "".join([reverse_pattern[i] for i in r[::-1]])
        if reads.count(r) + reads.count(reverse_r) >= 2:
            correct_reads.append(r)
        else:
            incorrect_reads.append(r)

    for ir in incorrect_reads:
        for cr in correct_reads:
            reverse_cr = "".join([reverse_pattern[i] for i in cr[::-1]])
            if hamming_distance(ir, cr) == 1:
                corrections.append((ir, cr))
                break
            if hamming_distance(ir, reverse_cr) == 1:
                corrections.append((ir, reverse_cr))
                break

    return corrections


seq_name = []
seq_string = []
fa = ""
for seq_record in SeqIO.parse(fa,'fasta'):
    seq_name.append(str(seq_record.name))
    seq_string.append(str(seq_record.seq))
corrections = error_correct(seq_string)
for ir, cr in corrections:
    print("{}->{}".format(ir, cr))
