import socket
import select
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# if len(sys.argv) != 3:
#     print ("Correct usage: script, IP address, port number")
if len(sys.argv) != 4:
    print("Correct usage: script, IP address, port number")
    exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
name = sys.argv[3]
server.connect((IP_address, Port))



sockets_list = [socket.socket(), server]
read_sockets,write_socket, error_socket = select.select(sockets_list, [], [])
while True:
    for socks in read_sockets:
        #print("reading sockets")
        if socks == server:
            text = socks.recv(2048).decode('utf-8')
            print(text)
            #message = sys.stdin.readline()
            #server.send(message.encode('utf-8'))
            #sys.stdout.write("<You>")
            #prompt = 'Write your message: '
            #message = sys.stdin.readline(prompt)
            while True:
                message = input("Write your message: ")
                spacing = ': '
                server.send(sys.argv[3].encode('utf-8')+spacing.encode('utf-8')+ message.encode('utf-8'))
                sys.stdout.write("<You> ")
                sys.stdout.write(message)
                print()
        # sys.stdout.flush()
sys.stdout.flush()
server.close()
server.close()
