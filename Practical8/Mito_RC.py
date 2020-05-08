# -*- coding: utf-8 -*-
import re

filename = input("Input the name of the fasta file to be generated:")
with open("mito_gene.fa", 'r') as mito_file, open(filename, 'w') as out_file:
    trans = str.maketrans('ATCG', 'TAGC')
    re_name = re.compile(r'>\S+\s+\S+\s+\S+\s+gene:(\S+)\s+')

    lines = mito_file.readlines()
    i, n = 0, len(lines)
    while i < n:
        res = re.match(re_name, lines[i].rstrip())
        out_file.write(res.group(1) + ' ')
        i += 1

        seq = ''
        while i < n and not lines[i].startswith('>'):
            seq += lines[i].rstrip()
            i += 1
        
        out_file.write(str(len(seq)))
        out_file.write('\n')
        out_file.write(seq[::-1].translate(trans))
        out_file.write('\n')
    
    out_file.flush()