#Write a function analyse_dna(sequence) that defines an inner function gc_content()
#to calculate GC% . The outer function should print whether the given DNA is AT rich
#or GC rich sequence.


def analyze_dna(seq):
    def gc_content():
        gc = sum(1 for base in seq.upper() if base in "GC")
        return gc / len(seq) * 100
    gc=gc_content()
    if gc > 50: kind = "GC rich"
    elif gc < 50: kind = "AT rich"
    else: kind = "balanced with exactly 50% GC"
    print(f"The GC content is {gc:.2f}% and hence the sequence is {kind}")

analyze_dna(input("Enter DNA sequence to be analyzed: "))


#use generator function