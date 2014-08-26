codon_table = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}

def parse_rna(rna):

    temp_codon=""
    codons=[]

    for i,base in enumerate(rna):
        if i>0 and i%3==0:
            if temp_codon in ['UAA', 'UGA', 'UAG']:
                return codons
            codons.append(temp_codon)
            temp_codon=""
        temp_codon+=base

    return codons


def rna_to_protein(rna_string='AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'):
    codons = parse_rna(rna_string)
    return ''.join([codon_table[codon] for codon in codons])

if __name__ == '__main__':
    print rna_to_protein('AUGAGCCAAAUCGCACCCACCGUGUCUUUACCAACAGUGUUCCGUGUGAUGAAGCUAAGACGGCCGGCGAGAAGGGGGCCAGCAGCUUCUUCAAGCGUCGACGGUGAAUUUACUAUAAUCUGUGCUGUAGGUCGACCUUUGGAAGCCUUUCGAACAGGUACCAUACGUCGCUCACCCUCACGAAUAUCGGUAGCGUAUAAACAGUACCGGGCUAUGAUCGAGCUCGCACGUUUUCAGGCAGUACUGGGGUACUUAGUCUCUCCCAACCGCGGGCCGAAUAGAGUAGAAAUUCAAUUCGAAACGCAGCCGGAUCGUGUCUCUACUUCUUUAAGCGUAAAGAGUUACCAGCCGCUUCGUAGAUACCUUAUAUCGGGUCCAAGCAUCGUGGGCCCACAAAUGCGCAACUACUCACGUUUCGGGGGUAUACGGCGCAUGUUUCUAAAUAUCGUUUGUUUCAUCCUAAAGCAUAGCGAAUCGGAGCGCGAUCAGGUACAGGGAAAUCGUAGGAUUGAUAGCGCCAAGGAAAGCCCAAAAAAAUUAGGAUUACAUUUGGGACCACGAGGAUCAACCAUUCAUCAAUGGCGUUCUCGCACUCGUAACCACAAAAGGCUAGGAACUUUGCGUGGUGUCGCACUGGUACUAGUAUGCACCAUCGUGCGUUGGACAGCAAUAACGCCCGGCUGUUGUACUCCUGAGCUAGCUGGCGCCGAGGAUACAGCCAGUUUCGUGGGAGAUGGAGUAGGUAUUUAUCGGGCAAACUCAACUUUACAGGGUCUAGGACGGAGCUGGGGGUAUCUUUCCAAUGUCCCCGGAGACCAAGCAACCGGUGAUUUUCGCCUCGAAGCGGUAACCCGGUGGCUAUUGCGCUAUAACUACCACAAGUGGUUCACGGUGCCGUUCGCAUUGGCACGGCCUGUAGUAGGUUCCCAGUUAAACCCGAAACAGAUCACCCAGCAGGACAGGGCGGGUGUCAUCCCGAUAUUUCAUGAUAGAUUUACACCACCUGGUCUCGCGAAGGGCUUAUCGUGUAAAGUAAACCAAGUUAUCGGUAGCACUUACAACAAAAGAGACCGGAGUAGUCGACUAUUGAACCGUUCACUUGGGAGACGUCAGACGACUUCCCCAUAUAAGGCACUGGUGGGUUGUGUGGCUACAGGGGUCGUUUUCCUCGCAAUGGCCUACGGGCACACCGAGGACGGCCAAAAUGGGUUUAGAUUGCCCUCAGUGCGAAGAAUUACGUGGCUCGGACGUGAAUUCCCCCCGAAGACAAGGAAAUGUACUGGAACUCGCCACUUCAAUACAGGCAUGAAAGACCUCACCCCAAUUGGGCGGUUGCUGCCCGUCGUCCCACUCAUACCAAAGCUGGGUGCCUACGCAGAUACUCUCUUCCUGCUGGCCUGCAGGAACAUUCAGGCGUGGUUGAGGCAGACUACUUUAUGCGCGUCUCGGCUAUAUAAAAAGACCCAAUCCAGGCCGUGCGUCAGACUACCUUAUAGCAACCGAACAGGCAGCGUAGCCAACUCACACCACCUACAAGACUUGAAUUACAACCUACCUGCCUGGAAUAUCGCUGGAAAUAAAUUCUCCGAACUAAGGAAACAUGUUCAUAAUCAUAGUGAAACCUAUGACGCCAAGCCACCCGGACCGCCUUUAUCAGAGAAGCUACCGCAGGUAGAAAUUGAUGGGCAGAAUUGUCAGACACAUUAUGGACAUCUGUACCCUCCGGAUGUCUCGUUCUUGCUAAGACCUACGGAAGCCUCAGCAGUGCAAACCGAUGAUCAGCUGUAUGUCCAUCCGAUUAAUCCCCGCGUCAGCCUCCAGACUAGGCUUUCGUCCUGUCGACUCAAAUUUGAAAACAGGUGGCGUUUGCGAAAAGUGUCCUGUCUGUCCUUGAAAUCCUGCUUAUUUCCACAUUCUGAACACCUGCGAAACCUCUCCGGGUAUACGACUCCUGAGAGUCCACGGGAUCGCGAACCUGAUCCUCCCAGGUUGGGUCCUACAAUCACAGUGCACACCAUUUUGAGAGAGCCUCAGACCUGCGCAGUGGAAGUAUCAAUCCUUCGCAGAAUUCUCUCUUGUCGUGGUGACUCCCGGCGGACCGUCUUAACGUUAAAGGCGACGCCGACCCAGCCCUCCGGGUCGGCCACUGGAAUUAAGAUGAUCUGGGUAAGUGGGGGUGCUCGGUUGGUGCUUUCGGGAAUGCGGCCGAAGCUCUGCUCCACCUUUGUUCUUUGUAGGCAUCGUUUCCGCCGUCACACUUCGAUCGUCAGGCAGCAGAGGUAUGGCUGCAGCAAUAUACUGAAACGUCCGGACAAGGACAGCUGUUAUUAUAUAUGGGACAAAAUGUAUUCCCCUUUGUCAUUAUUUCCCCAGUUGGGGAAGCUCUCAUCGUCCAGUCAGUCCGUUGGACCUAGUGCCGCUAUCCUGUGUUCCAGUUGUAAGUCUCAUAUACAUACCCCGCUGUACACCGCCAGCGAUGUUAUGUACGACUCUACUUAUUACAACUCUGACACGCCUGAAACAUUGUACCGACGACCCCGGUUAGACCAUCCGUCCCAUCGGGUAUCAAGUACUGUAGCCAGACGAAAAAUUGUAAUUGCAGAGCACGGGUACGUGACCCUGCGAAAUACUUACUACCGUCGUACCAGUAAUGACAAUCUCAUAUUAGCUCGGGUACGAAUCGUCGCGCAAACUGUCUGUCAGUCUCGGCCCAGUUACGCAUUACCAUCUCCCUCAACACUGUGUUCUAGCGUGCGGUCUCAUGUUAGCGUUAAUCCUGACGAACAAGUUAAGGUCUUCGUGGCAUUUAGCACGGGUGUGAGAUUAAUUGUGGCUGGGCUUCGCGUCAGAUUAAUCCGACUCCUACGCGGAGCAGUCAGGCUAGUUAUAAUUCGGAUGUGUUUUCCCAUGUCAAAACGUGCACACCUUUUAAUGAGUAUCUCUACACACUAUGAGCAGAUCGCGCGGAGUGUGACACCCAUAUGGCCUAUGUCAAGUCCUUCGGACAAGGAAAUGCGAGGAGCUCUGGCGUACUCACCCGCUGGGGACUGGGUACCCCCUACAUGUGCAUCAAAUUGCGCUUAUCGGUGUGAUAAACUUAUUAAUGGCGGAAUCCGGCAUGAACAUCGAGGCCGUACUCUAGAAAAGCACGCUAAACUGAAAAGCCCUGAGUCUCCGCGCGCUGUCCGGCGCACGCGAGCAUGGGAACUUGUGACCUUCACUGGGGAUAAAAUUUAUGAUCUGCCAUUCUUCACCGGCGGCGAGGAAGCAGAGCUCCGACUAUCCGGCGUGAUGUUACUGCGGGCGCGCACAACCGGUUCGUGGUCGCCGAUAUAUAGAUAUUACGGUGUCCAAAACGAAGGCUAUCUAACUUCUCUCGGGGCCACCUGCAUACACACCGUUCACUCCUUGUCUCCGGAUUACAGAAGAAUAACUCGUUGUAACGAGGCGCGACAACGACUGCAGCCCGACGUACGACACGCUAUUCAGGUCUUUCACCUCAUAUCUGACGUACACAAUUUUUGCUACUUGCACCAGGCGGGACGUGAUCGGAUGGUCAGACGUCGGGUACAUGAUGCCAAGUUUGACACGCGUUGCUGCGGUUACUUUGAGUCUCGGACGUUGCUGAUAUCGGGUUCAGUCUAUACCCACGAAUGUUGUCAGUUUAUCCAGGAUAUGACUCUGGAUUUGUGCCUACAGAUAGUCAUUAAUUAUCGUGAAGGGCCAACACCAGAACGCAGAAAAUGUCCACCAAAGCGCAACGGUCUGACGGAAUCAACCCUCGGCGUCACGUCUAGAAACCAAUCUCCGUGUCCUUCCGUAGUAAGUAGAAGUCCACGGAUGAAAACGUUUUCCUACCCGCAUAUCCGCGCUCACCACGAGCAGGGCUUCCGAACGCAUUGUGGAACCAGGUAUCUGAGCCCAGUACGUAUGCCCUUCUACUGGGUUGUCAUUUCUAGCAUUCUGAGCUUCUACGGCAGGUUAUAUUACUCAGCCUGGCCUGUGGUGAUUGGACGUGAUGAAAAGAUUAUCGAUGUGACCCCCCCACAUCUAUCCGAUUUCCUUUGGACUUGGCUUAAGUCGCCAUGCUUCGAGAGCCGCGAGAUCACACCAGGAGGGCCGGCACGUCGGCUUGAAGAUGCGUGUUUCAUUCUGGAAAGCAAGAGCUCCCAUGUCUUCCUCAAAUCACACCGAGCGCUACUCUUAGGUGUCGGUAAUGGCGGCGAACAUAAAGCAGGAUCGAUUGCCCUAGAGCGUAGGAUUCGAAACCUGCCGAUAUAUGACCUUUCUGUCUUAAGACAAUUCUUCUGCACGGCAAAUAGAGUACGGAGGGCUAAGCCCCAGGAUGUGGAUGUUAUUCACGGCCCCGGACGACGGCGUGCCCAACAAAGCGUCCUGCAUUCGUCUGGGCCUGACCCAGCGCCGAUGCUCGAAGGGGUGUUAGGGACACUUAUUUCGCCGGGAAAUGGAAACACGUAUUGCCGGUCCCUGAAGCUUUUAGCGGCUCCCGACAUCACUCUCGACAUCUGGGUUUUUGGGGUGGGGUCCAAGGCUCGUCUUUCACUACUUAUCAUAGAGAGCCAGGAUGAUUCCCACUCCCCGGCGGGAAGAGCAGCUAUUAAGACUGUUCAAUGCUUCAUUGGCGGUGUUGAUCGAGUCAGUACAAGCAGAGCUUAUGCGUCCCGGACUGCCAUGGUACUAAAUUAUGGAUGUCAGUUAUUAAAAAUUCACCAUUCCCUCCGGCGGCCGAUGCCAGCAGACCCUCAACAUAACCAUGGCGACGGCUGGUUCUCCCUGUUCCCGCCUGGUACAGCGAUGACAUCGGCCACUGUCUAUGUCUUUCAUCUAGAUUAUGGCCUCUUAGUUAUGAGGAUUGAAUAUGAGUGCGAAAACGAACGGUUCGUAAAGAUCGUAGCCAUACAGUCGGGAGAACAGUGCCAACCACCUGUGAUUGUGUACUUUGCAAAAGCUAAAUCUCGAAGUCAAAGUCUGAGCUCCGCGACAAUGACUUAUUCCUGUAAGACGGGCUCCCGGAAGUCUGGACACCGCUGGGAUGACAGUGAAGGCUCGUACCAUUACCUAACGUCUAUACGCAAACCUGGUGUGGCCCAAGAGAACGAGCAUUCAAACCCAAAAAGAGACGGACCCGGUAUGGACUAUAGACUCCCCUACUACGUCUCAAUCCACAUCCUAACAAACCAUACAAAAGCGAACGGGGCUGAGCUGCGCGAUCUACGGUCCGGAUACACCAGAAACCAUCAUGGUUUCCGUUGCAAUAUUUACGAUUACCUAUAUGCAGAGGUAGUUGCCUUCCCGGUGCUGAUUUCGGACUCCCAAGACGCCGCGUUAGGGGCUCCUGUGGGACCCCGAGCGCAGGCGGUAGCAUGCGUAUCAUCUAAUCUGAGGCUCCUUGUAGAUUCCGGACAUGAUAGAACACUUCAGCUCUUGGAGGUAUUAGCCCGAUCGCGGGACAUUUAUGUCGCCGACUCGCUCAUGUCCCUCAGGAACACCUAUGACACUUGUGGCUACCCUGUGUCGAGGGCGAAGUGUUCUUCUGUGCAGGUAGACUACUUGUGUGGACAUGCACGUUAUCAUAGAGAAGCACUCGUAGUACCUAUGGUGUCGUCGAGAGGCGGUGACCUUUCCGUAUCUUUGAACCACACGAACGCCUUGGAACAUCACACUCUCCGAUCCACUUUAAUUGGGGAACGUAGGUUCCAAGUCAGCGUUAUUGCCAACCUAAUGUACACUUGCCGGUCGUGGAAAGACCGCUAUGAGAUGGGCUCUUGUGUAUCCCCCCCCUCUGCCGGUAUUUCCACAGCUAAAGGAGAAAUCUAUCGACAAGAGGUGUUAGGUGAGGCAUCUAAUAGAAUACGACGUACUUCGGUAGGUAGUGAAGCUGAAUGGAUAGAGAUCUACAAGCGUGUUUUUUGGCUAAUCCGUACCCCUCCAGCGACUCUAGCAUUUAUCUCCACAACCCGAGAAAGGCAGACUCCGUUCACAAACAUGACCCCCGUUGCCUUACUUCGGUCCAACGGGCGAGCAAUGGCCAUAUUGAAAUUCCUCAUGUGUCGAACGCCCAAUGUUUUUGCCACGUGGAAGUUAGAAGUGAGUAAAGAGGCCCCGGCUCGUAUCAGGGAACUGUGGGACAUUGCCUUAUCGCACCGCGCGUCUAUCGUCGGUUGUUCACAGCUUCAGGUUCUAAUGAUAACUUGUGUGUUGUUUAUGAAGUUCCCAGCAAACCGAUUGCUAACAGAUAGCGUCCACAGUGUGUGGGGCCUUUGUUUAAUAGUUCCACAAAAACCGACUCCUCUCUUAUGUCGGGGCUUGAUGAUCAUUGGAGCUGUUUAUAAGCCCCCUAAUUCUCGCCUGAGGUGGAAGUUUGCCACGAGCCGGGCGCGAGGUGACAGGUCCAUUCUCUUCGGUGGAAAAGGGCUUGAGUGUACCUCAUUUGGCUCUCCAGGGCCCACCGAAUCCAGAGGGGAUGUCGGGCCGGCCGUAAUUAGAGAAAUGGCACCGAACGACGUCAUCGUGUGUGCAAAGUACAUAUGGAUGAGUCCCUUGCUGAACCCAACGAUCCACCUGGAGGAAUGUCUGCCCCUACCUCCUUCCCAAUUGCAGCCGGAGCCUCUCGGCGGGACUUAUAUUUCGCGAGAUAAAACGACGGCAACGAAAUCGGUGUCAAGCCUAGUAUGGGGCAGGGCUGUAGAGCCGAUUUAUGGCGCACUUGGAAUAUACCUGACAGUGGGACCAAACGGACGUGUGUGUCAGUGUCGUAUGGGUGGGUGGGCUACCGUCGUAACCACAGAGCCGGCGUUCGUCUUGUCCCGCACUACUGUGCAGUCUGGGGAGGGCUUGGCAUACGAGGUAAUAUGUUGCGCAGUUUCCGCGAGUACGCAAAGAUGGAAGAAUAUGCGCCUUAAACCACGCAUUUCAGAUGAAGACAAGCAUCGUGGCAGGGCGAGUAGUAGCAUGGCCAGCGCGACUUUGGCAGGUACCAUUGCCCUCCAUCGUAUGAAGCACCGCCUUGCCAUGAAUACCACAAUCCGUGCGGCUGCAUUUAAGGGUUAUUACAGGAAGUGCUUCGGGGAGGGGAGACAACUGUUUCAGGAUCUAGCAUACCUUCCGCCGUACGCGUGCAUCAGGAUAAAAUUCACUUGCCAACUGCGCCGCAAUCUGGUAGCAAACAGGGCCCGACACCAAGGGUGCCUAACGGAGCGGGACUCGAAUUUCGCCCGCGUGAGUGACGGCUCACCCGCAUCGCUUAUUGUCUCUGGCCGCUGCUCUAUGGCAUUACGUCGCUAUCUGAUUCUAAUGCACAGUACAGUGCCUUGGAUCGAACGGGGGUCGGGACCCGGAGGGAACGAUGUGAGAAAACCCGGCCUGAUUCGUUGUUCACCUGCUUGCUGCAUAGCGUUGAAUAAUCGACGGUAUCUCCUUCACAUUUCUCCGGAACCUAGAGUAUGGUCCCGGCCGUGUGGUGAAGUCAUCGGAACAAGUACCCUCGUCGGCUGCGUAAAACUAGUCACCUAUCCGACAACCAAAAAAAAAGCCGUGUUAAGUUUACGUGACGAUUGGACUCCACUUGCUCGGCCCCACACAGAUGUGCAGCCGCUGAUUCGCCGCAUUGUGGAUGUCGCGUGCGGACGCGUGCAAACAGGCUUCCUUUGCCAUAUAGGCUGGCAGGUUAAGACUCAGCGUGAUAGGCUUUGGAGUCGGAUGUAUUGUUCGAAGGUUGGGCCUCGGAGAAUUACUGAAUCGGCCAGCUUACGAGCCAUUCAGGUCCUUACAGAUAUUCCUACAACCCUCAAACAGCUACGCGAUAGUCUAAUUAGAGAGCAAGGCGAUUCAAGCUACGGUCCCUCUCUCGGCUUGCUGAGGCACCCUCGAGAAUGCAGACUAACAAACCGUGAGUACGUGUCCGGUACCCAUCGACAAACGGGGGAGGUGGGCGGACCCCCAGUUAGUAGCGAAGUCGGAAGGAUGGCACUAAUCACGAACAAUGGAGGUGGAAUCCUCUUCUGCUAUAGCCUUUAUCAUGGAGCUUUAGAGAACCGUUUAUUUAGUCGCGGGUGCCAACAUUCAUCGUCGACAUCGGCCACUGAAACAUUAUCUCGGGAUGUUUCGUCGCGGAGUCGCGUAACGAAGCCAGGACCCUAG')

