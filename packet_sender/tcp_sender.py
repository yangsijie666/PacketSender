import socket


BYTE_SIZE = b'a'


class TcpSender(object):

    def __init__(self, dst_ip, dst_port=None, src_port=None, length=1):
        # Information of targets

        self.dst_ip = dst_ip
        self.dst_port = dst_port
        self.src_port = src_port
        self.tcp_data = BYTE_SIZE * length

    def send_tcp(self):
        # Send tcp message.
        if self.dst_port:
            while True:
                tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    if self.src_port:
                        tcp_socket.bind(('', self.src_port))
                    tcp_socket.connect((self.dst_ip, self.dst_port))
                except:
                    pass
                else:
                    tcp_socket.send(self.tcp_data)
                tcp_socket.close()

        else:
            dst_port = 1
            while True:
                if dst_port == 65536:
                    dst_port = 1
                tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    if self.src_port:
                        tcp_socket.bind(('', self.src_port))
                    tcp_socket.connect((self.dst_ip, dst_port))
                    dst_port += 1
                except:
                    pass
                else:
                    tcp_socket.send(self.tcp_data)
                tcp_socket.close()
