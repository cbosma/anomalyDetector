#!/usr/bin/env python

import dpkt, pcap, struct, socket, os
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


#Takes an input pcap, parses out the goodies and the whatnots and plops it into a matrix file.
#It also returns an list called jsonList that will be used to feed Kibana
def pcapToMatrix(filename):
    inFile = open(filename, 'rw')
    dataMatrix = open(os.path.splitext(filename)[0] + 'Matrix.txt' , 'w+')
    pcap = dpkt.pcap.Reader(inFile)
    thisArray = []
# For each packet in the pcap process the contents
    for ts, buf in pcap:
   
        # Unpack the Ethernet frame (mac src/dst, ethertype)
        eth = dpkt.ethernet.Ethernet(buf)

        # Make sure the Ethernet frame contains an IetP packet
        if eth.type == dpkt.ethernet.ETH_TYPE_IP:
            # Now unpack the data within the Ethernet frame (the IP packet)
            # Pulling out src, dst, length, fragment info, TTL, and Protocol
            ip = eth.data
            try:
                srcPort = ip.data.sport
                dstPort = ip.data.dport
            except AttributeError:
                srcPort = 0
                dstPort = 0            
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
            row = [srcOctOne, srcOctTwo, srcOctThree, srcOctFour, dstOctOne, dstOctTwo, dstOctThree, dstOctFour, srcPort, dstPort, length, ttl]
            thisArray.append(row)
            output = np.matrix(thisArray)
            
    np.savetxt(dataMatrix, output, fmt="%i")