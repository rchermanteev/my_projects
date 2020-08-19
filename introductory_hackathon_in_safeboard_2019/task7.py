from itertools import chain, groupby

import sys
s = sys.stdin.readlines()
arr = [tuple(st.replace('\n', '').split(" ")) for st in s]
E = [tuple([int(el) for el in el_tuple]) for el_tuple in arr]

graph = {}
for k, it in groupby(sorted(E), key=lambda x: x[0]):
    graph[k] = {e for _, e in it}

sub_graph = {}
while True:
    vertex_set = set(graph).intersection(chain.from_iterable(graph.values()))
    sub_graph = {k: vertex_set & vs for k, vs in graph.items()
                 if k in vertex_set and vertex_set & vs}

    if sub_graph == graph:
        break
    else:
        graph = sub_graph

print("FALSE" if graph else "TRUE")
