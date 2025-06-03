from BA11Utils import * 


def dfs(curr, target_spectrum, graph, mass_path, label_path) -> bool:
    """
    Depth First Search to find a path in the graph that matches the spectrum.
    """
    curr_mass, curr_label = curr

    # if we current mass is in the path, i.e., we have a cycle, return
    if curr_mass in mass_path :
        return False

    mass_path.append(curr_mass)
    label_path.append(curr_label)

    if curr_mass in graph:      
        # do recursion.
        for next_node in graph[curr_mass]:
            if dfs(next_node, target_spectrum, graph, mass_path, label_path):
                return True
    else: # this is total mass, we intentially leave it out of the graph, so we reached the end
        spectrum = generate_spectrum_from_peptide(label_path, residue2mass)
        # if the spectrum is equal to the original spectrum, we found a solution
        if spectrum == target_spectrum:
            global peptide
            peptide = "".join(label_path[1:])
            return True

    # done recurion, remove from path & mark as visited
    del mass_path[-1]
    del label_path[-1]
    return False


residue2mass, mass2ressidue = parse_aa_masses()

masses = parse_masses_from_file("TestData/rosalind_ba11b.txt")

# build a graph from the masses
G = build_graph_from_masses(masses, mass2ressidue)

# get the spectrum from the masses
# the spectrum is the set of all masses except 0
spectrum0 = set(masses)
spectrum0.remove(0)

mass_path = []
label_path = []

peptide = None

# start the DFS from the root node (0, None)
res = dfs(('0', None), spectrum0, G, mass_path, label_path)

if res:
    print("we decoded the spectrum:") 
    print(peptide)
else:
    print("we could not decode the spectrum")