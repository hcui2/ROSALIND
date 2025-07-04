import collections
from BA11Utils import parse_aa_masses

"""
input: 
0 0 0 4 -2 -3 -1 -7 6 5 3 2 1 9 3 -8 0 3 1 2 1 0
output: 
XZZXX
"""

# Parse amino acid masses
residue2mass, mass2residue = parse_aa_masses()

# read in spectral vector and build a graph
with open("TestData/rosalind_ba11e.txt") as f:
    spectral_vector = f.readline()
    spectral_vector = [int(m) for m in spectral_vector.strip().split()]
spectral_vector.insert(0, 0)


spectrum_graph = collections.defaultdict(list)
in_degrees = {idx : 0 for idx, amplitude in enumerate(spectral_vector)}
node2plist = collections.defaultdict(list )

for idx, amplitude in enumerate(spectral_vector):
    for j in range(idx+1, len(spectral_vector) ):
        if (j - idx) in mass2residue.keys():
            spectrum_graph[idx].append(j)
            in_degrees[j] += 1
            node2plist[j].append(idx)

node2weight = {idx : amplitude for idx, amplitude in enumerate(spectral_vector)}

# do topo sort 
# BA5N 
def topo_sort():
    res = []
    dq = collections.deque([k for k in in_degrees if in_degrees[k] == 0])
    while dq:
        node = dq.popleft()
        res.append(node)

        if node in spectrum_graph:
            for e in spectrum_graph[node]:
                in_degrees[e] -= 1
                if in_degrees[e] == 0:
                    dq.append(e)
                    del in_degrees[e]
    return res

sorted_list = topo_sort()


# do dynamic programming 
# similar to BA5D 
def max_node_weight_path_in_DAG(sorted_list, source, sink):
    node2parent = {}
    dp_weight = {}

    for n in sorted_list:
        dp_weight[n] = float('-inf')

    dp_weight[source] = 0
    for n in sorted_list:
        for p in node2plist[n]:
            if dp_weight[p] + node2weight[n] > dp_weight[n]:
                dp_weight[n] = dp_weight[p] + node2weight[n]
                node2parent[n] = p

    path = []
    peptide = []
    t = sink
    while t in node2parent:
        path.insert(0, t)
        peptide.insert(0, mass2residue[t - node2parent[t]])
        t = node2parent[t]
    path.insert(0, source)

    path = [str(p) for p in path]
    return ("".join(peptide), '->'.join(path))

peptide, path = max_node_weight_path_in_DAG(sorted_list, 0 , len(spectral_vector)-1)
print(peptide)
print(path)


