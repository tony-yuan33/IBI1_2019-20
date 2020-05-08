# -*- coding: utf-8 -*-
import matplotlib.pyplot as plot

dna = "ATGCTTCAGAAAGGTCTTACG"

freq_tab = {'A':0, 'T':0, 'C':0, 'G':0}
for base in dna:
    freq_tab[base] += 1

plot.pie(freq_tab.values(), labels=freq_tab.keys(), autopct="%1.1f%%")