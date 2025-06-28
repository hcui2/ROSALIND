from BA11Utils import parse_aa_masses

residue2mass, mass2ressidue = parse_aa_masses()

# Read the peptide sequence from the file and generate the peptide vector
with open("TestData/rosalind_ba11c.txt") as f:
    peptide = next(f)
    res = ""
    for r in peptide.strip():
        res += " 0" * (residue2mass[r]-1) + " 1"

print(res.strip())