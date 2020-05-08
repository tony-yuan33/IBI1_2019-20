# -*- coding: utf-8 -*-
import re

input_path = r"C:\Users\canch\Downloads\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_path = r"mito_gene.fa"

with open(input_path, 'r') as in_file, open(output_path, 'w') as out_file:
    # Starts with >... ... ...:...:Mito, a mito gene.
    re_mito_gene = re.compile(r'>\S+\s+\S+\s+\S+:\S+:Mito')

    # The idea is to traverse all lines in the input. A line can be either a header or part of base sequence.
    # Either way, if the line is part of a mito gene, it must be written. Consequently, we used a sentinel
    # variable `is_mito` to keep track of this status and decide whether the current line is part of some
    # mito gene. In pseudo code, this is:
    #
    ## for line in in_file:
    ##     if `changed to a new mito gene`:
    ##         is_mito = True
    ##
    ##     if `changed to a new non-mito gene`:
    ##         is_mito = False
    ##
    ##     if is_mito:
    ##         `write line`

    is_mito = False
    for line in in_file:
        if line.startswith('>'): # a header, state may be changed
            if re.match(re_mito_gene, line): # a mito header
                is_mito = True # switch to mito
            else:
                is_mito = False # switch to non-mito

        if is_mito:
            out_file.write(line)
    
    out_file.flush()