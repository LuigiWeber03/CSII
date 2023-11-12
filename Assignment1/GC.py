//code for the GC exercise from Rosalind
from Bio import SeqIO
def calculate_gc_content(dna_sequence):
    gc_count = dna_sequence.count('G') + dna_sequence.count('C')
    total_bases = len(dna_sequence)
    gc_content = (gc_count / total_bases) * 100
    return gc_content

def find_sequence_with_highest_gc(fasta_file):
    highest_gc = 0
    highest_gc_id = ""

    for record in SeqIO.parse(fasta_file, "fasta"):
        gc_content = calculate_gc_content(record.seq)
        if gc_content > highest_gc:
            highest_gc = gc_content
            highest_gc_id = record.id

    return highest_gc_id, highest_gc

fasta_file = "rosalind_gc (1).txt"

highest_gc_id, highest_gc = find_sequence_with_highest_gc(fasta_file)

print(highest_gc_id)
print("{:.6f}".format(highest_gc))
