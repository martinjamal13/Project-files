import socket 
import os

HOST ="your IP" #"192.168.1.203"
 
def main():
    #create raw socket, bin to public interface
    if os.name == 'nt':
        socket_protocol = socket.IPPROTO_IP
    else:
        socket_protocol = socket.IPPROTO_ICMP

    #set up sniffer with our parameters
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
    sniffer.bind((HOST,0))
    #includes the IP in the header in the capture, set socket optiond
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    #determine if using windows, if so send IOCTL to enable promiscous mode
    if os.name == 'nt':
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    
    #read one packet
    print(sniffer.recvfrom(65565))

    if os.name == 'nt':
        sniffer.ioctl(socket.SIO_RCVALL. socket.RCVALL_OFF)
if __name__ == '__main__':
    main()