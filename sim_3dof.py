import matplotlib.pyplot as plt
import numpy as np



n = 50
accum = 0.5
temp = 0.0
for i in range(n):
    accum = 1.0/(accum + 1)
    print(accum)
