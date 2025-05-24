residue2mass = {}
mass2ressidue = {}
with open("amino_acid_masses.txt") as f:
    for line in f:
        l = line.split('\t')
        residue = l[0]
        mass = int(float(l[-1]))
        residue2mass[residue] = mass
        mass2ressidue[mass] = residue

with open("TestData/rosalind_ba11a.txt") as f:
    masses = f.readline()
    masses = [int(m) for m in masses.strip().split()]

res = []
masses.insert(0, 0)
for i in range(0, len(masses) -1 ):
    for j in range(i+1, len(masses)):
        if (masses[j] - masses[i]) in mass2ressidue.keys():
            print(str(masses[i]) + '->' + str(masses[j]) + ":" + mass2ressidue[masses[j] - masses[i]])