# -*- coding: utf-8 -*-
import re

input_path = r"C:\Users\canch\Downloads\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_path = r"mito_gene.fa"

with open(input_path, 'r') as in_file, open(output_path, 'w') as out_file:
    # Starts with >... ... ...:...:Mito, a mito gene
    re_mito_gene = re.compile(r'>\S+\s+\S+\s+\S+:\S+:Mito')

    is_mito = False
    for line in in_file:
        if line.startswith('>'): # a header
            if re.match(re_mito_gene, line): # a mito header
                is_mito = True # switch to mito
            else:
                is_mito = False # switch to non-mito

        if is_mito:
            out_file.write(line)
    
    out_file.flush()