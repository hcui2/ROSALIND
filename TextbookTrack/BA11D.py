from BA11Utils import parse_aa_masses

residue2mass, mass2residue = parse_aa_masses()

# Read the peptide vector from the file
with open("TestData/rosalind_ba11d.txt") as f:
    p_vector = f.readline()
    p_vector = [int(m) for m in p_vector.strip().split()]

# Initialize lists to store mass and residue
mass_list = []
residue_list = []
for i,v in enumerate(p_vector):
    if v == 1:
        mass = i+1
        if not mass_list:
            residue_list.append(mass2residue[mass])
        else:
            residue_list.append(mass2residue[mass-mass_list[-1]])
        mass_list.append(mass)

print("".join(residue_list))