import sys
s = sys.stdin.readlines()
goal = [st.replace('\n', '').split(' ') for st in s][-1]
s = [st.replace('\n', '').split(' ') for st in s][0:-1]
graph = {}
key = [item[0] for item in s]
value = [item[1] for item in s]


def ext_dict(d, key, value):
   if key in d:
      if isinstance(d[key], list):
         d[key].append(value)
      else:
         d[key] = [d[key], value]
   else:
      d[key] = [value]


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


for i in range(len(key)):
    ext_dict(graph, key[i], value[i])

a = list(dfs_paths(graph, goal[0], goal[1]))

ans = [len(i) for i in a]
if not a:
    print(-1)
else:
    print(min(ans)-2)
