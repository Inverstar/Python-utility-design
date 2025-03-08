import re
import exrex
ipadr = r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])'
ipadr1 = r'((\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.){3}(1\d\d|2[0-4]\d|25[0-5]|[1-9]\d|\d)'
mailbox = r'^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$'
mailbox1 = r'^\w+@[a-zA-Z0-9]+((\.[a-z0-9A-Z]{1,})+)$'
url = '(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?'
for i in range(10):
    k = exrex.getone(ipadr)
    k1 = exrex.getone(ipadr1)
    m = exrex.getone(mailbox)
    u = exrex.getone(url)
    
    print(k,k1,m,u)