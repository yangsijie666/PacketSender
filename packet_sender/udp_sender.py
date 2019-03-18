import socket


BYTE_SIZE = b'a'


class UdpSender(object):

    def __init__(self, dst_ip, dst_port=None, src_port=None, length=1):
        # Information of targets

        self.dst_ip = dst_ip
        self.dst_port = dst_port
        self.src_port = src_port
        self.udp_data = BYTE_SIZE * length

    def send_udp(self):
        # Send udp message
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        if self.src_port:
            udp_socket.bind(('', self.src_port))

        if self.dst_port:
            while True:
                udp_socket.sendto(self.udp_data, (self.dst_ip, self.dst_port))
        else:
            while True:
                dst_port = 1
                if dst_port == 65536:
                    dst_port = 1
                udp_socket.sendto(self.udp_data, (self.dst_ip, dst_port))
                dst_port += 1
