from Bio import SeqIO
genome_file=input("基因组序列文件名:")
dict = SeqIO.to_dict(SeqIO.parse(genome_file,"fasta"))
print(dict.keys())          #输出所有基因名
b=0
while b==0:
    a=input("需要抽取序列所在的名称：")  #scaffold
    c=int(input("抽取序列的起始位："))
    d=int(input("抽取序列的末尾位："))
    seq_record = dict[a]     # 导出基因序列
    e = str(seq_record.seq)
    g=e[c-1:d]                      #导出所抽取的序列
    i = ">%s:%d..%d" % (a, c, d)   #规定的fasta文件格式 Mayetiola_destructor_genomic.fasta
    print(i)
    print(g)
    b=int(input("继续输入0结束输入1："))
