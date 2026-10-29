# word frequency

paragraph="Translesion translesion DNA synthesis (TLS) is a conserved damage-tolerance pathway that enables the replication machinery to traverse template lesions that would otherwise stall high-fidelity polymerases. Specialised Y-family polymerases, notably polymerases η and κ, possess enlarged active sites that accommodate distorted templates and catalyse nucleotide insertion opposite a broad spectrum of DNA adducts. Recruitment of these polymerases is governed by post-translational modification of the sliding clamp proliferating cell nuclear antigen (PCNA), principally monoubiquitination by the E3 ligase RAD18. While TLS prevents lethal replication fork collapse, its inherently low fidelity can introduce mutations, with implications for carcinogenesis, chemoresistance and ageing. "
counts={}
for word in paragraph.lower().split():
    word=word.strip(".,!?;:()")
    counts[word] = counts.get(word, 0) + 1

print(counts)
print()
print("The words in the paragraph and their count: ")
for key, value in sorted(counts.items()):
    print(f"{key} :{value}")

max_occ=0
for count in counts.values():
    if count > max_occ: max_occ = count
for key, value in counts.items():
    if value == max_occ: print(f'The word "{key}" occurs {value} times in the given paragraph.')
