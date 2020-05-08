# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

gene_lengths = [9410, 3944141, 4442, 105338, 19149, 76779, 126550, 36296, 842, 15981]

res = gene_lengths.copy()
res.sort()
del res[-1] # the last one is the greatest, delete it
del res[0]  # the first one is the least, delete it
plt.boxplot(res)