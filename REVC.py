string = "CTGATTCTTAGCGCAACAACGGTTACGGGTGAGCTTAGCAATGAGTTAAACCGCCATTCTTCCACAAGGGAACTTGAGATTCCACTGTCCCCTACTAGAGGGTCAATGACCTTGTTTTTCTTAAGCCTCTTACCCAGCAAGTCTTGATCTGTACGGGAAGGTCAATCAGAGATCTACCTATAGTCTCGTACCCCCTAAAGGTTGGACGATACTAGTAGGAACCTAAAGCTCGACCCTTGGACCGCACCCGCTCCAGATGGTAAACTTAGTATTGTAGATTTAATGGCATGCTGTTCGAAACATACGGACGGTCTGGGACACAGACTTTGACTGGATAGTGGGTGAAGCCTAGATACCCTTAGCCACGACCCTCCGAAAATTATAGTAACCGGCCCGCCTCTCCGTCATTACAAAGATCCGGTTGTTGGGTTCTGGCTTCTTCCTTTTTCGAAGAGACGCCTGACTTTGTAATCGACCTGCAAGTAGCGGTGTCTGACCTAAAGGAAGATGGAAATGTAGAGGTATCGTACTGGCTAGATTACCCCCTTCTTGAGGGCCATCGTCGGCCTGGGTCACAACGTTACATCTGACTCAGCGTTCACGGGCCTGATTTGCCCTTAGACGTCGTGTTGAGAAAGTATTACTCAGACAGTGCGTGGAAACACCGGGACTATGTGCTTGAGCCGTGAAGCGGATTGCCACGAGAGGCTTGCATCCCCTCTAAATAGCCATTATAACATATCGTTTTCTCTCTTGCTTGTGGACGAACAGACAAATGTTGTGGGTGATCCTCCAACTGTTCGCTACAGTAGCGTATCAATTGCTCTCTCTAATTTCCCGGACGATAGAAGTAATAGAGAATGAGTA"
newstring = ""
for base in string:
    if base == "A":
        newstring += "T"
    if base == "T":
        newstring += "A"
    if base == "C":
        newstring += "G"
    if base == "G":
        newstring += "C"
actualstrand = newstring[::-1]

print(actualstrand)
