import socket

Server_Ip = "localhost"
Server_Port = 12345

Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Socket.connect((Server_Ip, Server_Port))

print('ex ) twice://sana/height')
address = input('주소를 입력하세요 : ')

Socket.send(address.encode())
data = Socket.recv(65535)

info = str(data.decode())

data, name, wh = info.split('/')

if name != "noname":
    if name == "nayeon" and wh == "w":
        print('나연의 몸무게는 '+data+'입니다.')
    elif name == "nayeon" and wh == "h":
        print('나연의 키는 '+data+'입니다.')
    if name == "jeongyeon" and wh == "w":
        print('정연의 몸무게는 '+data+'입니다.')
    elif name == "jeongyeon" and wh == "h":
        print('정연의 키는 '+data+'입니다.')
    if name == "momo" and wh == "w":
        print('모모의 몸무게는 '+data+'입니다.')
    elif name == "momo" and wh == "h":
        print('모모의 키는 '+data+'입니다.')
    if name == "sana" and wh == "w":
        print('사나의 몸무게는 '+data+'입니다.')
    elif name == "sana" and wh == "h":
        print('사나의 키는 '+data+'입니다.')
    if name == "jihyo" and wh == "w":
        print('지효의 몸무게는 '+data+'입니다.')
    elif name == "jihyo" and wh == "h":
        print('지효의 키는 '+data+'입니다.')
    if name == "mina" and wh == "w":
        print('미나의 몸무게는 '+data+'입니다.')
    elif name == "mina" and wh == "h":
        print('미나의 키는 '+data+'입니다.')
    if name == "dahyun" and wh == "w":
        print('다현의 몸무게는 '+data+'입니다.')
    elif name == "dahyun" and wh == "h":
        print('다현의 키는 '+data+'입니다.')
    if name == "chaeyoung" and wh == "w":
        print('채영의 몸무게는 '+data+'입니다.')
    elif name == "chaeyoung" and wh == "h":
        print('채영의 키는 '+data+'입니다.')
    if name == "tzuyu" and wh == "w":
        print('쯔위의 몸무게는 '+data+'입니다.')
    elif name == "tzuyu" and wh == "h":
        print('쯔위의 키는 '+data+'입니다.')



    if name == "nodata":
        print('찾을 수 없는 정보입니다.')
else:
    print('없는멤버입니다.')