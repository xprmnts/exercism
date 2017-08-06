def dna_rna(x):
    """function that just returns a single rna nucleotide based on input"""
    return {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'
    }[x]

def to_rna(dna):
    rna = ''  # create empty string
    for nuc in dna:  # check nucleotide & replace using dna_rna(), add to rna
        if(nuc in 'GCTA'):
            rna += dna_rna(nuc)
        else:
            return ''
    return rna
