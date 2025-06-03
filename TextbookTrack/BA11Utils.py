"""
Utilities for BA11 Textbook Track
"""

def parse_aa_masses():
    """
    Parses the amino acid masses from a file and returns two dictionaries:
    residue2mass and mass2residue.
    """
    residue2mass = {}
    mass2ressidue = {}
    with open("amino_acid_masses.txt") as f:
        for line in f:
            l = line.split('\t')
            residue = l[0]
            mass = int(float(l[-1]))
            residue2mass[residue] = mass
            mass2ressidue[mass] = residue
    return residue2mass, mass2ressidue

def parse_masses_from_file(filename):
    """
    Parses a list of masses from a file.
    """
    with open(filename) as f:
        masses = f.readline()
        masses = [int(m) for m in masses.strip().split()]
    return masses


