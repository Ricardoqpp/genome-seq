from Bio import SeqIO
from Bio.Seq import Seq
GFF_name=input("GFF 文件名:")
dictgene = {}
dictgene1 = {}
fxdictgene1 = {}
f1 = open(GFF_name, "r+")
dict = SeqIO.to_dict(SeqIO.parse("Anopheles.genome.fa", "fasta"))
print(dict.keys())
wz=input("scaffold:")
for fo in f1.readlines():  # 读取出指定片段上所有基因
    # print(fo)
    parts = fo.split()
    if parts[0] == wz and parts[2] == "mRNA":
        dictgene[parts[3]] = fo  # 保存进字典dictgene
    else:
        continue
#print(dictgene)
listgene = []
listgene2 = []
for key in dictgene:
    # print(key)
    listgene = listgene + [int(key)]
#print(listgene)
listgene1 = sorted(listgene)
#print(listgene1)
for keys in listgene1:
    a = dictgene[str(keys)]
    # print(a)
    listgene2 = listgene2 + [a]  #gene信息列表   CVRI01000012.1  Clunio-marinus_genomic.gff
# print(listgene2)
n = 0
for genexx in listgene2:
    n += 1
    keys1 = "gene%d" % n
    dictgene1[keys1] = genexx
print(dictgene1)
print(len(dictgene1.keys()))
for key1 in dictgene1.keys():  # 建立反向字典
    a1 = dictgene1[key1]
    fxdictgene1[a1] = key1
#print(fxdictgene1)

genename1=input("查询的位置1:")
genename2=input("查询的位置2:")
for dene in dictgene1.keys():
    parts = dictgene1[dene].split()
    begin = parts[3]
    last = parts[4]
    if genename1<begin<genename2 and genename1<last<genename2:
        print(dictgene1[dene])
    else:
        continue


#scaffold:Chromosome UNKN
#GFF 文件名:Anopheles-gambiae-PEST_BASEFEATURES_AgamP4.12.gff3