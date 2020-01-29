from Bio import SeqIO
from Bio.Seq import Seq
tiqu_listfile=input("基因list文件：")
file_naem=input("蛋白或者基因序列文件：")
dictgene = {}
dictgene1 = {}
fxdictgene1 = {}
dict = SeqIO.to_dict(SeqIO.parse(file_naem, "fasta"))
print(dict.keys())
f2 = open(tiqu_listfile, "r+")
n=0
for a in f2:
    print(dict[a])
    fo2 = open("%s%s"%(file_naem,n), "w")
    fo2.write(dict[a])
    fo2.close()
