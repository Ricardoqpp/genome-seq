import os
import xlwt
db_wz=input("输入比对数据库所在目录：")
db_name=input("输入比对数据库的文件名：")
id_wz=input("输入比对query序列所在目录：")
id_name=input("输入比对query序列名：")
blastn="tblastn.exe -task tblastn -query %s\%s -db %s\%s -out %s\%s-%s-result.txt"%(id_wz,id_name,db_wz,db_name,id_wz,id_name,db_name)#CP1目前全长 QIAO LIANG
os.system('cd "G:\\blast-2.7.1+\\bin\\" & %s'%blastn)
f = open("%s\%s-%s-result.txt"%(id_wz,id_name,db_name),"r")
file = xlwt.Workbook()  # 新建一个excel文件  blastp tblastn

f1=f.readlines()
all={}
query_list=[]
###删除所有“\n”
while '\n' in f1:
    f1.remove('\n')
#print(f1)
################

###查看有多少个query序列
for a in f1:
    if a[:6] == "Query=":
        query_list.append(a)
all=0
#print(query_list)
################

#####查看每条query序列有多少个匹配上的scaffold
weiz=[]
for del1 in f1:
    if del1[0] == ">":
        all += 1
weiz.append(all)
for a1 in range(len(query_list)).__reversed__():
    m = 0
    n=0
    for del1 in f1:
        if del1[0] == ">":
            m += 1
        if del1[:43] == "Sequences producing significant alignments:":
            n += 1
            if n == a1 + 1:
                break
    weiz.append(m)
weiz.reverse()
query_wei={}
for a1 in range(len(query_list)):
    query_wei[a1+1]=weiz[a1+1]-weiz[a1]
#print(query_wei)
################

###提取每个query比对结果信息的前端
pdq={}
for a1 in range(len(query_list)).__reversed__():
    n=0
    f2=[]
    for del1 in f1:
        f2.append(del1)
        if del1[:43] == "Sequences producing significant alignments:":
            n+=1
            if n == a1+1:
                break
        continue
    pdq[a1+1]=f2
#print(pdq)
#for a in pdq[1]:
#    print(a)
##########

###提取每个query比对结果信息的后端
pdh={}
m=0
for a1 in weiz:
    n=0
    f2=[]

    for del1 in f1:
        if del1[0] == ">":
            n+=1
            if n == a1+1:
                break
        f2.append(del1)
    m+=1
    pdh[m]=f2
#print(pdh.keys())
#for a in pdh[1]:
#    print(a)
##########

###query_id与比对信息构成字典
message={}
for a4 in range(len(query_list)):
    for a in pdq[a4+1]:
        pdh[a4+1].remove(a)
#    for a in pdh[a4+1]:
#        print(a)
    message[query_list[a4]]=pdh[a4+1]
#print(message)
##########

###简化query_id与比对信息构成字典
jh_message={}
for id in message.keys():
    each={}
    for me in message[id]:
        c1 = me.split("    ")
#        print(c1[0],c1[-1])
        each[c1[0]]=c1[-1]

    jh_message[id]=each
#print(jh_message)


####################################写入Excel表中######################################
table = file.add_sheet("text")  # 新建一个sheet
for a4 in range(len(query_list)):
    table.write(a4,0,query_list[a4])
    print(query_list[a4])
    div=jh_message[query_list[a4]]
    n=0
    for me in div.keys():
        if float(div[me]) < 0.00001:
            n+=1
            print(me,div[me])
            table.write(a4,n, "%s--%s"%(me,div[me]))
#    dict1=eval(jh_message[id])
#    for mer in jh_message[id]:
#        print(mer)
#eval(mer)转换字符串为字典
#        if int(eval(mer)[mer]) <1:
#            print(eval(mer)[mer])
file.save("%s\%s-%s-result.xls"%(id_wz,id_name,db_name))
'''
输入比对数据库所在目录：G:\blast-2.7.1+\bin\按蚊scaffolds
输入比对数据库的文件名：Anopheles-darlingi.fa  Phlebotomus-papatasi.fna   Danaus-plexippus.fa
输入比对query序列所在目录：C:\\Users\ASUS\Desktop\\resilin-数据整理\共线性\共线性详细比对信息
输入比对query序列名：Drosophila-melanogaster_seq.txt   Anopheles-gambiae_seq.txt
Clunio-marinus_seq.txt  Anopheles-sinensis_seq.txt  Anopheles-sinensis_2367seq.txt
输入比对数据库所在目录：G:\blast-2.7.1+\bin\resilin\果蝇数据库
输入比对数据库的文件名：Drosophila_melanogaster_protein.faa   Drosophila_melanogaster_genomic.fna
输入比对query序列所在目录：C:\\Users\ASUS\Desktop\resilin-数据整理\所有目所有序列整理
输入比对query序列名：所有最佳序列集.txt
输入比对数据库所在目录：G:\blast-2.7.1+\bin
输入比对数据库的文件名：Anopheles.gene.pep
输入比对query序列所在目录：C:\\Users\ASUS\Desktop\resilin-数据整理\所有目所有序列整理\长角亚目\断裂
输入比对query序列名：dip-all-cpr152.txt
'''