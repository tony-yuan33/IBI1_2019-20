seq = 'ATGCGACTACGATCGAGGGCCAT'
compl = str.maketrans('ATCG', 'TAGC')
compl_list = list(seq.translate(compl))
compl_list.reverse()
print(''.join(compl_list))
