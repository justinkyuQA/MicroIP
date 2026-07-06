import socket

def show():

    print()
    print("MicroIP")
    print("=" * 40)

    hostname = socket.gethostname()

    try:
        addresses = socket.getaddrinfo(hostname, None)

        seen = set()

        print("Hostname:", hostname)
        print()

        for info in addresses:

            addr = info[4][0]

            if addr in seen:
                continue

            seen.add(addr)

            family = "IPv6" if ":" in addr else "IPv4"

            print(f"{family:<6} {addr}")

    except Exception as e:

        print(e)
