//code for the HAMM exercise from Rosalind
Seq1 = ""
Seq2 = ""
HAMMdistance = 0 
for character in range(len(Seq1)):
    if Seq1[character] != Seq2[character]:
        HAMMdistance += 1
print(HAMMdistance)

