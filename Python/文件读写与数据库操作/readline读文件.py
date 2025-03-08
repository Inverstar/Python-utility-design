try:
    infile = open("T:\\X\\Python\\文件读写与数据库操作\\t.txt",'r',encoding='utf-8')
    while True:
        datal = infile.readline()
        if datal == "":
            break
        datal = datal.strip()
        print(datal)
    infile.close()
except Exception as e:
    print(e)