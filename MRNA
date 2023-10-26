//code for the MRNA exercise from Rosalind

AminoAcidSequence = ""
codons = {'F': ['UUU', 'UUC'],
            'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
            'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
            'Y': ['UAU', 'UAC'],
            '*': ['UAA', 'UAG', 'UGA'],
            'C': ['UGU', 'UGC'],
            'W': ['UGG'],
            'P': ['CCU', 'CCC', 'CCA', 'CCG'],
            'H': ['CAU', 'CAC'],
            'Q': ['CAA', 'CAG'],
            'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
            'V': ['GUU', 'GUC', 'GUA', 'GUG'],
            'A': ['GCU', 'GCC', 'GCA', 'GCG'],
            'D': ['GAU', 'GAC'],
            'E': ['GAA', 'GAG'],
            'G': ['GGU', 'GGC', 'GGA', 'GGG'],
            'I': ['AUU', 'AUC', 'AUA'],
            'M': ['AUG'],
            'T': ['ACU', 'ACC', 'ACA', 'ACG'],
            'N': ['AAU', 'AAC'],
            'K': ['AAA', 'AAG']}
possibleRNAs = 1
for aminoacid in AminoAcidSequence:
    possibleRNAs = possibleRNAs * len(codons[aminoacid])
possibleRNAs = possibleRNAs * len(codons["*"])
print(possibleRNAs % 1000000)
