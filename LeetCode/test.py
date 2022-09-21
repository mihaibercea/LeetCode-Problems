import pyshark

cap = pyshark.FileCapture('C:\Work\TLS doc\msvacation.pcapng')

print(cap)

packet = cap[3]

print(packet)
print(packet.ipv6.src)