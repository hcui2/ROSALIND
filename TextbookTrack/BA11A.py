from BA11Utils import *

# parse the amino acid masses
residue2mass, mass2ressidue = parse_aa_masses()

# read the masses from the input file
masses = parse_masses_from_file("TestData/rosalind_ba11a.txt")

res = []
masses.insert(0, 0)
for i in range(0, len(masses) -1 ):
    for j in range(i+1, len(masses)):
        if (masses[j] - masses[i]) in mass2ressidue.keys():
            print(str(masses[i]) + '->' + str(masses[j]) + ":" + mass2ressidue[masses[j] - masses[i]])