      #!/usr/bin/env python

import dpkt, socket, struct
import datetime
import socket
import numpy as np

#Convert the ip address to a value
#Uses the method from https://infowaves.eu/tutorials/iptonumber.php
def ipToNumber(ip):
    packedIP = socket.inet_aton(ip)
    return struct.unpack("!L", packedIP)[0]

#Convert MAC to string
def mac_addr(address):
    return ':'.join('%02x' % ord(b) for b in address)

#Convert IP to string
def ip_to_str(address):
    return socket.inet_ntop(socket.AF_INET, address)

def pcapToMatrix(pcapFile, matrixFile):
    inFile = open(pcapFile, 'rw')
    outFile = open(matrixFile, 'w+')
    pcap = dpkt.pcap.Reader(inFile)

    thisArray = []
    count = 0
    
    # For each packet in the pcap process the contents
    for timestamp, buf in pcap:
        count = count +1
    
        # The timestamp in UTC
        ts = str(datetime.datetime.utcfromtimestamp(timestamp))
    
        # Unpack the Ethernet frame (mac src/dst, ethertype)
        eth = dpkt.ethernet.Ethernet(buf)
        sourceMac = mac_addr(eth.src)
        destMac = mac_addr(eth.dst)
        ethType = eth.type
    
        # Make sure the Ethernet frame contains an IetP packet
        if eth.type == dpkt.ethernet.ETH_TYPE_IP:
            # Now unpack the data within the Ethernet frame (the IP packet)
            # Pulling out src, dst, length, fragment info, TTL, and Protocol
            ip = eth.data
        
            do_not_fragment = bool(ip.off & dpkt.ip.IP_DF)
            more_fragments = bool(ip.off & dpkt.ip.IP_MF)
            fragment_offset = ip.off & dpkt.ip.IP_OFFMASK
            srcIP = ipToNumber((ip_to_str(ip.src)))
            destIP = ipToNumber((ip_to_str(ip.dst)))
            ttl = ip.ttl
            length = ip.len           
            
            #Build a row and insert the row into the array.
            row = [srcIP, destIP, length, ttl, do_not_fragment, more_fragments, fragment_offset]
            thisArray.append(row)
            output = np.matrix(thisArray)
            
            
    np.savetxt(matrixFile, output, fmt="%i")
    return
