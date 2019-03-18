from sender import Sender
import argparse
import sys


def get_args():

    parser = argparse.ArgumentParser(description='Packet sender.')
    parser.add_argument('type', help='type: tcp or udp')
    parser.add_argument('dst_ip', help='ip address of destination')
    parser.add_argument('--sport', metavar='src_port', type=int, help='port of source')
    parser.add_argument('--dport', metavar='dst_port', type=int, help='port of destination')
    parser.add_argument('--plen', metavar='length', type=int, help='length of packet (bytes)')

    return parser.parse_args()


def main():
    args = get_args()
    sender = Sender(type=args.type,
                    dst_ip=args.dst_ip,
                    dst_port=args.dport,
                    src_port=args.sport,
                    length=args.plen or 1)
    sender.send_data()


if __name__ == '__main__':
    sys.exit(main())
