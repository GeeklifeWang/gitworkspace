import socket

host = '127.0.0.1'
port = 8888
buf = 1024
address = (host, port)

#tcp
while True:
    send = raw_input('Send Data:')
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client.connect_ex(address)
    tcp_client.send(send)
    get = ''
    while True:
        receive = tcp_client.recv(buf)
        if receive:
            get += receive
        else:
            break
    print get
    tcp_client.close()
'''
#udp
while True:
    send = raw_input('Send Data:')
    udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_client.sendto(send, address)
    get, receive = '', ''
    receive, addr = udp_client.recvfrom(1024)
    print receive
    udp_client.close()
'''