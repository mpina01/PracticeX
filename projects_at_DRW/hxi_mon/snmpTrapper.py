# import os, socket, sys, thread, logging
import os, socket, sys, _thread
from pysnmp.carrier.asynsock.dispatch import AsynsockDispatcher
from pysnmp.carrier.asynsock.dgram import udp, udp6
from pyasn1.codec.ber import decoder
from pysnmp.proto import api

monoIP = '10.10.23.30'
monoPort = 31750

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
from HXI2Monocle import HXI2Monocle

def cbFun(transportDispatcher, transportDomain, transportAddress, wholeMsg):
    print("Starting cbFun")
    global monoIP, monoPort
    while wholeMsg:
        msgVer = int(api.decodeMessageVersion(wholeMsg))
        if msgVer in api.protoModules:
            pMod = api.protoModules[msgVer]
        else:
            print('Unsupported SNMP version %s' % msgVer)
            return
        reqMsg, wholeMsg = decoder.decode(
            wholeMsg, asn1Spec=pMod.Message(),
        )
        reqPDU = pMod.apiMessage.getPDU(reqMsg)
        if reqPDU.isSameTypeWith(pMod.TrapPDU()):
            if msgVer == api.protoVersion1:
                srcOID = str(pMod.apiTrapPDU.getEnterprise(reqPDU))
                varBinds = pMod.apiTrapPDU.getVarBindList(reqPDU)
            else:
                srcOID = str(pMod.apiPDU.getEnterprise(reqPDU))
                varBinds = pMod.apiPDU.getVarBindList(reqPDU)
            for oid, val in varBinds:
                ccitt = str(val.getComponentByPosition(0)[1])
            
        if srcOID == '1.2':
            if skip == [True]:
                continue
            _thread.start_new_thread(HXI2Monocle.HXI2Monocle, (monoIP, monoPort, ccitt))
        else:
            print(srcOID)

print("Making transport dispatcher")
transportDispatcher = AsynsockDispatcher()
transportDispatcher.registerRecvCbFun(cbFun)
print("ready to registerTransport")
# UDP/IPv4
transportDispatcher.registerTransport(
    udp.domainName, udp.UdpSocketTransport().openServerMode(('0.0.0.0', 162))
)
print("Gone")
transportDispatcher.jobStarted(1)
print("start job")


try:
    # Dispatcher will never finish as job#1 never reaches zero
    print("try")
    transportDispatcher.runDispatcher()
    print("tried")
except:
    print("except")
    transportDispatcher.closeDispatcher()
    raise

