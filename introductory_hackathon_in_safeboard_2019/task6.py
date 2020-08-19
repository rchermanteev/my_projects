import sys
s = sys.stdin.readlines()
arr = [st.replace('\n', '') for st in s]

size = int(arr[0])
example = arr[1:]
example = [el.split(" ") for el in example]

lable = [[0 for _ in range(size)] for _ in range(size)]

for i in range(size):
 for j in range(size):
  example[i][j] = int(example[i][j])


def Labeling(img, labels):
 L = 1
 for y in range(size):
  for x in range(size):
   L += 1
   Fill(img, labels, x, y, L)


def Fill(img, labels, x, y, L):
  if (labels[x][y] == 0) and (img[x][y] == 1):
    labels[x][y] = L
    if x > 0:
        Fill(img, labels, x - 1, y, L)
    if x < size - 1:
        Fill(img, labels, x + 1, y, L)
    if y > 0:
        Fill(img, labels, x, y - 1, L)
    if y < size - 1:
        Fill(img, labels, x, y + 1, L)


Labeling(example, lable)

new_arr = []

for i in range(size):
 for j in range(size):
  new_arr.append(lable[i][j])

print(len(set(new_arr) - {0}))
