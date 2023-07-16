import ipaddress


def ipChecker(address):
    try:
        addr = ipaddress.ip_address(address)
        if isinstance(addr, ipaddress.IPv4Address):
            print(address + " is a valid IPv4 Address")
        elif isinstance(addr, ipaddress.IPv6Address):
            print(address + " is a valid IPv6 Address")
    except ValueError:
        print(address + " is an invalid IP address")


if __name__ == '__main__':
    ip = input("Enter IP Address: ")
    ipChecker(ip)