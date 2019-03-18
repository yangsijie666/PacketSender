from tcp_sender import TcpSender
from udp_sender import UdpSender


class Sender(object):

    def __init__(self, type, dst_ip, dst_port=None, src_port=None, length=1):
        self.type = type
        self.dst_ip = dst_ip
        self.dst_port =dst_port
        self.src_port = src_port
        self.len = length

    def send_data(self):
        if self.type.lower() == 'tcp':
            tcp_sender = TcpSender(dst_ip=self.dst_ip,
                                   dst_port=self.dst_port,
                                   src_port=self.src_port,
                                   length=self.len)
            tcp_sender.send_tcp()
        elif self.type.lower() == 'udp':
            udp_sender = UdpSender(dst_ip=self.dst_ip,
                                   dst_port = self.dst_port,
                                   src_port=self.src_port,
                                   length=self.len)
            udp_sender.send_udp()
        else:
            raise Exception('TYPE ERROR!')
