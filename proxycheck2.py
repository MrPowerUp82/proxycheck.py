import socket
import time
import requests
print("As proxies devem estar assim na lista -> 192.168.1.1:8080") 
file=input("Lista das proxies-> ")
arq=open("{}".format(file), 'r').readlines()
file2=input("Nome da lista de saida-> ")
for line in arq:
    l=line.strip()
    l=str(l)
    ipon=l
    l=l.split(':')
    ip=str(l[0])
    port=int(l[1])
    try:
        time.sleep(0.5)
        ps=socket.socket()
        ps.connect((ip,port))
        print(ip,port,"ON") 
        ps.close()
        arq2=open("{}".format(file2),'a')
        arq2.write('{}\n'.format(ipon))
        arq2.close()
    except socket.error:
        print(ip,port,"OFF")

for line in openproxy:
    arq2.write("{}\n".format(line))

arq2.close()
