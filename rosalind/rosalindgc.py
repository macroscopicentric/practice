fasta = """
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
"""

dna = fasta.split(">")
dna.pop(0)

perHighest = 0
name = ''

for n in dna:
    content = n.count("C") + n.count("G")
    total = n.count("A") + n.count("C") + n.count("G") + n.count("T")
    percent = (float(content) / float(total)) * 100
    if percent > perHighest:
        perHighest = percent
        name = n[0:13]

print name
print perHighest