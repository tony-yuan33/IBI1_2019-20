# -*- coding: utf-8 -*-
import re

with open("SOD2_human.fa") as in_human:
    lines = in_human.readlines()
    human_name, human_seq =  lines[0][1:].rstrip(), lines[1].rstrip()

with open("SOD2_mouse.fa") as in_mouse:
    lines = in_mouse.readlines()
    mouse_name, mouse_seq =  lines[0][1:].rstrip(), lines[1].rstrip()

with open("RandomSeq.fa") as in_human:
    lines = in_human.readlines()
    rand_name, rand_seq =  lines[0][1:].rstrip(), lines[1].rstrip()

blosum62 = {'A':{'A':4,},}
with open("BLOSUM62.txt") as in_blosum62:
    line = in_blosum62.readline().rstrip()
    while line.startswith('#'):
        line = in_blosum62.readline().rstrip()
    
    # line is title now
    titles = re.split(r'\s+', line)

    for line in in_blosum62: # remaining lines
        line = line.rstrip()
        if len(line) > 0 and not line.startswith('#'):
            vector = re.split(r'\s+', line)
            blosum62[vector[0]] = {}
            for i in range(1, len(vector)):
                blosum62[vector[0]][titles[i]] = int(vector[i])

def compare_protein_seq_ungapped(name1, seq1, name2, seq2):
    if len(seq1) == len(seq2):
        score = 0
        identity = 0
        for i in range(len(seq1)):
            score += blosum62.setdefault(seq1[i], '*').setdefault(seq2[i], '*')
            if seq1[i] == seq2[i]:
                identity += 1
    
        print("Comparing " + name1 + " and " + name2)
        print(name1 + ": " + seq1)
        print(name2 + ": " + seq2)
        print("Score by BLOSUM62: " + str(score))
        print("Percentage identity: {:.2%}".format(identity/len(seq1)))

compare_protein_seq_ungapped(human_name, human_seq, mouse_name, mouse_seq)
compare_protein_seq_ungapped(human_name, human_seq, rand_name, rand_seq)
compare_protein_seq_ungapped(mouse_name, mouse_seq, rand_name, rand_seq)