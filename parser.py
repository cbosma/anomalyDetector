      #!/usr/bin/env python

import dpkt, socket, struct
import datetime
import socket
import numpy as np

#Convert the ip address to a value
#Uses the method from https://infowaves.eu/tutorials/iptonumber.php
#Not needed as of 5/7/2016 but keeping around just in case.
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
            srcOctOne = int(ip_to_str(ip.src).split('.')[0])
            srcOctTwo = int(ip_to_str(ip.src).split('.')[1])
            srcOctThree = int(ip_to_str(ip.src).split('.')[2])
            srcOctFour = int(ip_to_str(ip.src).split('.')[3])
            dstOctOne = int(ip_to_str(ip.dst).split('.')[0])
            dstOctTwo = int(ip_to_str(ip.dst).split('.')[1])
            dstOctThree = int(ip_to_str(ip.dst).split('.')[2])
            dstOctFour = int(ip_to_str(ip.dst).split('.')[3])
            ttl = ip.ttl
            length = ip.len           
            
            #Build a row and insert the row into the array.
            row = [srcOctOne, srcOctTwo, srcOctThree, srcOctFour, dstOctOne, dstOctTwo, dstOctThree, dstOctFour, length, ttl]
            thisArray.append(row)
            output = np.matrix(thisArray)
            
            
    np.savetxt(matrixFile, output, fmt="%i")
    return
