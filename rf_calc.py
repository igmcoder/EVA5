import math

# size of image
img_size = 28
# layers in k-p-s
layers = list([ [3, 1, 1], [3, 1, 1], [2, 0, 2],
                [3, 1, 1], [3, 1, 1], [2, 0, 2],
                [3, 0, 1], [3, 0, 1], [3, 0, 1]
              ])

# initialization
n = img_size
r = 1
j = 1
start = 0.5

# loop over layers to determine Receptive Field
for l in layers:
    k, p, s = l
    print(f'{k}-{p}-{s}')

    n = math.floor((n + 2*p - k) / s) + 1
    r = r + (k - 1) * j
    start = start + ((k - 1)/2 - p) * j
    j = j * s

    print(f'n: {n}, j: {j}, r: {r}, start: {start}')

