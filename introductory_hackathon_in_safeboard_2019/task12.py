import sys
s = sys.stdin.readlines()
arr = [st.replace('\n', '') for st in s]

size = int(arr[0])
example = arr[1:]
example = [el.split(" ") for el in example]

lable = [[0 for _ in range(size)] for _ in range(size)]

for i in range(size):
 for j in range(size):
  if example[i][j] != "?":
   example[i][j] = int(example[i][j])


def Labeling(img, labels):
 for y in range(size):
  for x in range(size):
   Fill(img, labels, x, y)


def Fill(img, labels, x, y, pred=0):
  if (labels[x][y] == 0) and (img[x][y] != 0):
    if img[x][y] != "?":
     labels[x][y] = img[x][y]
    else:
     labels[x][y] = int(pred/2)
    if x > 0:
        Fill(img, labels, x - 1, y, labels[x][y])
    if x < size - 1:
        Fill(img, labels, x + 1, y, labels[x][y])
    if y > 0:
        Fill(img, labels, x, y - 1, labels[x][y])
    if y < size - 1:
        Fill(img, labels, x, y + 1, labels[x][y])


Labeling(example, lable)

for el in lable:
 for e in el:
  print(e, end=" ")
 print()
