#!/usr/bin/python

# Forward SNMP traps from DRW HXI OOBM to Monocle
# April 2nd, 2013
# Yibing Wen (ywen@vigilantglobal.com)

import os, sys, socket

#HXI2Monocle('192.2.2.3', 'rfdata', {k:p})

#TODO: do we need this in a function
#TODO: how do we run this?
def HXI2Monocle(monoIP, monoPort, ccitt):
    print("Starting HXI2Monocle")
    JSON = ""
    SERVER = 'Monocle'

    #TODO: what is ccitt? can we embed it in our program?
    ccittSplit = ccitt.split()

    if len(ccittSplit) == 1:
        # print ccitt
        return

    if len(ccittSplit) < 6:
        f = open(os.path.dirname(os.path.realpath(__file__))  +  '/HXI2MonocleError.log', 'a')
        f.write('HXI2Monocle data: wrong size!\n' + str(ccitt) + '\n')
        for d in ccittSplit:
            f.write(str(d) + '\n')
        f.close()
        return

    mac = ccittSplit[0].upper()

    #TODO read from file
    tableDRW = { #MAC must be in UPPERCASE
        '00:30:30:01:C0:65': 'P1 1 US.IL.ATC.3262 ATC East',
        '00:30:30:01:C0:64': 'P1 2.1 US.IL.CPOL.3333WV JLL West',
        '00:30:30:01:C0:59': 'P1 2.2 US.IL.CPOL.3333WV JLL East',
        '00:30:30:01:C0:58': 'P1 3.1 US.IL.DG.3801HL DG West',
        '00:18:31:91:83:A3': 'P1 3.2 US.IL.DG.3801HL DG East',
        '00:18:31:8D:E5:3D': 'P1 4.1 US.IL.LGP.937BD Lagrange West',
        '00:60:35:26:9C:56': 'P1 4.2 US.IL.LGP.937BD Lagrange East',
        '00:18:31:93:37:86': 'P1 5.1 US.IL.AMC.26TH Harding West',
        '00:30:30:01:C0:00': 'P1 5.2 US.IL.AMC.26TH Harding East',
        '00:30:30:01:C0:01': 'P1 6 US.IL.DLR.350E DLR-2 West',
        '00:18:31:8D:F1:77': 'P2 1 US.IL.ATC.3262 ATC East',
        '00:18:31:E0:58:C3': 'P2 2.1 US.IL.CPOL.3333WV JLL West',
        '00:30:30:01:C0:60': 'P2 2.2 US.IL.CPOL.3333WV JLL East',
        '00:30:30:01:C0:61': 'P2 3.1 US.IL.DG.3801HL DG West',
        '00:30:30:01:C0:75': 'P2 3.2 US.IL.DG.3801HL DG East',
        '00:30:30:01:C0:62': 'P2 4.1 US.IL.LGP.937BD Lagrange West',
        '00:30:30:01:C0:36': 'P2 4.2 US.IL.LGP.937BD Lagrange East',
        '00:30:30:01:C0:37': 'P2 5.1 US.IL.AMC.26TH HDG-2 West',
        'BC:6A:29:85:94:CA': 'P2 5.2 US.IL.AMC.26TH HDG-2 East',
        'BC:6A:29:86:35:A4': 'P2 6 US.IL.DLR.350E DLR-2 West',
    }

    # print mac

    #TODO is it tag or stream?
    if mac in tableDRW.keys():
        monoIP = '10.8.35.77'
        monoPort = 31501
        site = tableDRW[mac]
        tag = "DRW-HXI " + site

    # if ccittSplit[0] == '00:60:35:26:9c:8b':
        # print monoIP

    RSSI = ccittSplit[1]
    MMW_Rx = ccittSplit[5]
    NetRx = ccittSplit[6]
    JSON = (  '{'
            '"monitoringDataStreamName": "' + tag + '",'
            '"RSSI": "' + RSSI + '",'
            '"Temp(Celsius)": "' + ccittSplit[2] + '",'
            '"6V Voltage(V)": "' + ccittSplit[3] + '",'
            '"6V Current(mA)": "' + ccittSplit[4] + '",'
            '"MMW Rx": "' + MMW_Rx + '",'
            '"Network Rx": "' + NetRx + '",'
            '"MAC": "' + mac + '",'
            '"message": "' + RSSI + ' ' + MMW_Rx + ' ' + NetRx + '", '
            '"url": "http://monocle/messages?tags=(RFnetwork::' + tag + ')&topics=(timestamp+RSSI+Temp(Celsius)+6V Voltage(V)+6V Current(mA)+MMW Rx+Network Rx+MAC)&title=' + site + '"}')

    #TODO: send message to monitoring via requests
    # initialize a socket, SOCK_DGRAM specifies that this is UDP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
    # connect the socket
    s.connect((monoIP, monoPort))
    # send the command
    s.send(JSON)
    # close the socket
    s.close()
