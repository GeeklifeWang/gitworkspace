import socket, time

#tcp_server
buf = 10
tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.bind(('127.0.0.1', 8888))
tcp_server.listen(5)
print 'Start Server, Wait for connect...'
while True:
    tcp_client, addr = tcp_server.accept()
    tcp_client.setblocking(0)
    print 'Get Connect From %s:%d ' % (addr[0], addr[1])
    data, alldata = '', ''
    while True:
        try:
            data = tcp_client.recv(buf)
        except socket.error:
            break
        else:
            alldata += data
    print 'Receive data: %s ' % alldata
    tcp_client.send('[%s] Your Send: %s ' % (time.ctime(), alldata))
    tcp_client.close()
    if alldata == 'break':
        tcp_server.close()
        print 'Server need to quit '
        break
    print '---------Done----------'
'''
#udp_server
buf = 1024
udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server.bind(('127.0.0.1', 8888))
print 'Start Server, Wait for connect...'
addr, data, alldata = '', '', ''
while True:
    data, addr = udp_server.recvfrom(buf)
    print 'Get Connect From %s:%d ' % (addr[0], addr[1])
    print 'Receive data: %s ' % data
    udp_server.sendto('[%s] Your Send: %s ' % (time.ctime(), data), addr)

    if alldata == 'break':
        udp_server.close()
        print 'Server need to quit '
        break
    print '---------Done----------'
'''