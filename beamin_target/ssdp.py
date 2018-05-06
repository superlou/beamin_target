import socket
import struct
import json


def parse_ssdp_request(data):
    data = data.strip()

    method, data = data.split('\r\n', 1)
    response = {}

    try:
        for line in data.split('\r\n'):
            tokens = line.split(':', 1)
            response[tokens[0]] = tokens[1].strip()
    except Exception:
        method = None
        response = {}

    return method, response


def handle_request(sock, addr, method, response, config):
    if ('M-SEARCH' in method) and (response['ST'] == 'beamin_target:control'):
        config['hostname'] = socket.gethostname()
        outbound = json.dumps(config)
        sock.sendto(outbound.encode(), addr)


def worker(config):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
    mreq = struct.pack('4sl', socket.inet_aton('239.255.255.250'), socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    sock.bind(("", 1900))

    while True:
        data, addr = sock.recvfrom(1024)
        data = data.decode()
        method, response = parse_ssdp_request(data)
        if method:
            handle_request(sock, addr, method, response, config)
