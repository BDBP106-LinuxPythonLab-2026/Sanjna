#extract codons

seq="AAATGGGCGCGCGCGATGAGATCGAGGTCA"
L=[]
def orf (n):
    for i in seq:
        codon=(seq[n-1:n+2])
        if len(codon)==3:L.append(codon)
        n+=3
    print("The codons are: ", L)
orf(int(input("Enter reading frame: ")))





