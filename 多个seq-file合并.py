c=input("物种文件：")
d=input("query_seq_file_位置:")
f=open(c,"r+")      #基因名文件
n=int(input("物种数目："))
f3=open("%s\\hebing_seq.txt"%d,"w")
for index in range(n):
    line = next(f)
    lines=line.rstrip()
    print(lines)
    f1=open("%s\\%s"%(d,lines),"r")
####处理序列之间的分隔
    for a in f1:
        if a[-1]=="\n":
           f3.write("%s"%a)
        else:
            f3.write("%s\n" % a)
'''物种文件：C:\\Users\ASUS\Desktop\Mayetiola-destructor-gxx\Anopheles-gambiae\list.txt
query_seq_file_位置:C:\\Users\ASUS\Desktop\Mayetiola-destructor-gxx\Anopheles-gambiae
db_file_位置:G:\\blast-2.7.1+\\bin\Chironomus-tentans.fna
result_位置:C:\\Users\ASUS\Desktop\Mayetiola-destructor-gxx\Anopheles-gambiae
物种数目：21'''