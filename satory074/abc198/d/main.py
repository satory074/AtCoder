import collections as cl
import math
from collections import deque

R, X, Y = map(int, input().split())

dist = math.sqrt(X ** 2 + Y ** 2)
print(dist)
