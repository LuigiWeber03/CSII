'''
from Bio import SeqIO
from Bio.Seq import Seq 

DNAstring = []
introns = []
sequences = []
fas = "rosalind_splc.txt"
for record in SeqIO.parse(fas ,"fasta"):
    sequences.append(str(record.seq))
DNAstring = sequences[0]
introns = sequences[1:]
for intron in introns:
    DNAstring.replace(intron, "")
translatable = Seq(DNAstring)
Protein= translatable.translate()
print(Protein)
'''

from Bio import SeqIO

coding_table = {
    'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S', 
    'TTT': 'F', 'TTC': 'F',
    'TTA': 'L', 'TTG': 'L', 'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
    'TAT': 'Y', 'TAC': 'Y',
    'TGT': 'C', 'TGC': 'C',
    'TGG': 'W', 
    'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'CAT': 'H', 'CAC': 'H',
    'CAA': 'Q', 'CAG': 'Q',
    'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R', 'AGG': 'R',
    'ATT': 'I', 'ATC': 'I', 'ATA': 'I',
    'ATG': 'M', 
    'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 
    'AAT': 'N', 'AAC': 'N', 
    'AAA': 'K', 'AAG': 'K',
    'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
    'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'GAT': 'D', 'GAC': 'D',
    'GAA': 'E', 'GAG': 'E',
    'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
    'TAA': 'end', 'TAG': 'end', 'TGA': 'end'
}


def RNA_splicing(dna_string, introns):
    for intron in introns:
        dna_string = dna_string.replace(intron, "")
    protein_string  = ""
    for i in range(0, len(dna_string)-2, 3):
        if coding_table[dna_string[i:i+3]] == "end":
            break
        protein_string += coding_table[dna_string[i:i+3]]
    return protein_string
fa = "rosalind_splc.txt"
seq_string = []
seq_name = []
for seq_record  in SeqIO.parse(fa,'fasta'):
    seq_name.append(str(seq_record.name))
    seq_string.append(str(seq_record.seq))

dna_string, introns = seq_string[0], seq_string[1:]
rna_string = RNA_splicing(dna_string, introns)
print(rna_string)