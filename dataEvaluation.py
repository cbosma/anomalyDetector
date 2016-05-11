#!/usr/bin/env python

import os, dpkt, datetime, json
from parser import pcapToMatrix
from parser import mac_addr, ip_to_str
from euclideanDistance import euclidean_distance
from cosineDistance import cosine_similarity
from averageKnown import averageKnownMatrix
from minkowskiDistance import minkowski_distance

def dataEval(trainingPcap, testPcap):
    
    #Create matrix files from the pcaps
    pcapToMatrix(trainingPcap)
    pcapToMatrix(testPcap)
    
    #Open all the needed files
    jsonFile = os.path.splitext(trainingPcap)[0] + '.json'
    jsonFile = open(jsonFile, 'a')
    trainingMatrix = os.path.splitext(trainingPcap)[0] + 'Matrix.txt'
    testMatrix = os.path.splitext(testPcap)[0] + 'Matrix.txt'      
    thisArray = []
    #Get the average list of values for the training pcap.
    averageKnownList = averageKnownMatrix(trainingMatrix)
    testPcap = open(testPcap, 'rw')
    pcap = dpkt.pcap.Reader(testPcap)
  
    # For each packet in the pcap process the contents
    for timestamp, buf in pcap:
   
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
            try:
                srcPort = ip.data.sport
                dstPort = ip.data.dport
            except AttributeError:
                srcPort = 0
                dstPort = 0
            srcOctOne = int(ip_to_str(ip.src).split('.')[0])
            srcOctTwo = int(ip_to_str(ip.src).split('.')[1])
            srcOctThree = int(ip_to_str(ip.src).split('.')[2])
            srcOctFour = int(ip_to_str(ip.src).split('.')[3])
            dstOctOne = int(ip_to_str(ip.dst).split('.')[0])
            dstOctTwo = int(ip_to_str(ip.dst).split('.')[1])
            dstOctThree = int(ip_to_str(ip.dst).split('.')[2])
            dstOctFour = int(ip_to_str(ip.dst).split('.')[3])            
            do_not_fragment = bool(ip.off & dpkt.ip.IP_DF)
            more_fragments = bool(ip.off & dpkt.ip.IP_MF)
            fragment_offset = ip.off & dpkt.ip.IP_OFFMASK
            ttl = ip.ttl
            length = ip.len
            
            row = [int(srcOctOne), srcOctTwo, srcOctThree, srcOctFour, dstOctOne, dstOctTwo, dstOctThree, dstOctFour, srcPort, dstPort, length, ttl]

            
            #Create a list for each iteration of the name and it's value. This will later be turned into a dict.
            jsonList = ['Timestamp', ts, 'Source Mac', sourceMac, 'Destination Mac', destMac,'Type', ethType, 'Source IP', ip_to_str(ip.src),
                        'Source Port', srcPort, 'Destination Port', dstPort, 'Destination IP', ip_to_str(ip.dst), 'Length', length,
                         'Time to live', ttl, 'Do not fragment', do_not_fragment, 'More fragments', more_fragments, 'Fragment Offset', fragment_offset]
            
            #Make calls to the create the average from the training matrix then, feed it into the distance functions.
            jsonList.append('Euclidean Distance')
            jsonList.append(euclidean_distance(averageKnownList,row))
            jsonList.append('Cosine Distance')
            jsonList.append(cosine_similarity(averageKnownList,row))
            jsonList.append('Minkowski Distance')
            jsonList.append(minkowski_distance(averageKnownList,row, 3))
            jsonDict = dict(jsonList[i:i+2] for i in range(0, len(jsonList), 2))
            json.dump(jsonDict, jsonFile)