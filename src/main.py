import sys
from packet.packet import Packet

def main():
    Packet().load(
        args=sys.argv[1::]
    )

if __name__ == "__main__":
    main()