seq = 'ATGCGACTACGATCGAGGGCCAT'

print(seq[::-1].translate(str.maketrans('ATCG', 'TAGC')))
