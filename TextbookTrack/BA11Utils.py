"""
Utilities for BA11 Textbook Track
"""
import collections 

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


def build_graph_from_masses(masses, mass2ressidue):
    """
    Builds a graph from the given masses and mass-to-residue mapping.
    the graph is represented as a dictionary where keys are mass strings
    and values are lists of tuples (next_mass, residue).
    """
    graph = collections.defaultdict(list)
    masses.insert(0, 0)
    for i in range(0, len(masses) -1 ):
        for j in range(i+1, len(masses)):
            if (masses[j] - masses[i]) in mass2ressidue.keys():
                graph[str(masses[i])].append((str(masses[j]), mass2ressidue[masses[j] - masses[i]]))
    return graph


def generate_spectrum_from_peptide(peptide, residue2mass):
    """
    Generates the spectrum from a given peptide sequence.
    The spectrum is the set of all prefix and suffix masses (excluding duplicates).
    """
    peptide = peptide[peptide[0] is None:] # remove None
    spectrum = set()
    for i in range(1, len(peptide)+1):
        prefix = peptide[:i]
        suffix = peptide[-i:]
        spectrum.add(sum([residue2mass[r] for r in prefix]))
        spectrum.add(sum([residue2mass[r] for r in suffix]))

    return spectrum