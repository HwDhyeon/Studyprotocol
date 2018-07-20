import socket

Server_Ip = "0.0.0.0"
Server_Port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((Server_Ip, Server_Port))
server_socket.listen(0)

client_socket, addr = server_socket.accept()

data = client_socket.recv(65535)

information = str(data.decode()[8:])
name, weihei = information.split('/')

if name == "nayeon":
    if weihei == "weight":
        data = "48/nayeon/w"
    elif weihei == "height":
        data = "163/nayeon/h"
    else:
        data = "-1/nodata/-1"

elif name == "jeongyeon":
    if weihei == "weight":
        data = "49/jeongyeon/w"
    elif weihei == "height":
        data = "167/jeongyeon/h"
    else:
        data = "-1/nodata/-1"
        
elif name == "momo":
    if weihei == "weight":
        data = "46/momo/w"
    elif weihei == "height":
        data = "161/momo/h"
    else:
        data = "-1/nodata/-1"

elif name == "sana":
    if weihei == "weight/w":
        data = "45/sana/w"
    elif weihei == "height/h":
        data = "162/sana/h"
    else:
        data = "-1/nodata/-1"

elif name == "jihyo":
    if weihei == "weight":
        data = "46/jihyo/w"
    elif weihei == "height":
        data = "160/jihyo/h"
    else:
        data = "-1/nodata/-1"
        
elif name == "mina":
    if weihei == "weight":
        data = "46/mina/w"
    elif weihei == "height":
        data = "163/mina/h"
    else:
        data = "-1/nodata/-1"
                
elif name == "dahyun":
    if weihei == "weight":
        data = "48/dahyun/w"
    elif weihei == "height":
        data = "159/dahyun/h"
    else:
        data = "-1/nodata/-1"

elif name == "chaeyoung":
    if weihei == "weight":
        data = "47/chaeyoung/w"
    elif weihei == "height":
        data = "159/chaeyoung/h"
    else:
        data = "-1/nodata/-1"
        
elif name == "tzuyu":
    if weihei == "weight":
        data = "51/tzuyu/w"
    elif weihei == "height":
        data = "170/tzuyu/h"
    else:
        data = "-1/nodata/-1"

else:
    data = "-1/noname/-1"


client_socket.send(data.encode())

