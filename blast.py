import os
from Bio import SeqIO
def makeblastdb(id,db):
    blastn="makeblastdb.exe -in %s -parse_seqids -hash_index -dbtype %s"%(id,db)#nucl prot
    os.system('cd "G:\\blast-2.7.1+\\bin\\" & %s'%blastn)
#blast类型，数据库名，query序列
def blast(type,db,id,name):
    blastn="%s.exe -task %s -query %s -db %s -out %s-result.txt"%(type,type,id,db,name)#CP1目前全长 QIAO LIANG
    os.system('cd "G:\\blast-2.7.1+\\bin\\" & %s'%blastn)


def get_seq(genome_file,filename):
    dict = SeqIO.to_dict(SeqIO.parse(genome_file, "fasta"))
    f = open("%s.txt" % filename, "w")  # 创建文件
    b=0
    print(dict.keys())
    while b==0:
        a=input("需要抽取序列所在的名称：")  #scaffold  NP_611157.1
        seq_record = dict[a]     # 导出基因序列
        e = str(seq_record.seq)
        print(len(e))
        c=int(input("抽取序列的起始位："))
        d=int(input("抽取序列的末尾位："))
        g=e[c-1:d]                      #导出所抽取的序列
        i = ">%s:%d..%d" % (a, c, d)   #规定的fasta文件格式
        f.write("%s\n%s\n" % (i, g))
        b=int(input("继续输入0结束输入1："))
    f.close()

a=1
while a==1:
    p=input("输入：getseq 、 blastn 、blastp、blastx、tblastn、tblastx or makedb:")
    if p=="blastn" or p=="blastp" or p=="blastx" or p=="tblastn" or p=="tblastx":
        db=input("输入比对数据库：")
        id=input("输入比对query序列名：")
        name=input("输入结果文件名：")
        blast(p,db,id,name)
    elif p =="makedb":
        id=input("输入建库文件名：")
        db = input("建库文件的类型(nucl、prot)：")
        makeblastdb(id,db)
    elif p =="getseq":
        genome_file = input("基因组序列文件名:")
        # print(dict.keys())          #输出所有基因名
        filename = input("想存入文档的名字：")  # 规定输出结果的文件名称 Un.17434
        get_seq(genome_file,filename)
    con=int(input("继续输入0，结束输入1："))
    a+=con
