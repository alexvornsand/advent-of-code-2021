packets = open('day-16.txt', 'r').read()

packets = 'D2FE28'


def parseCode(packets, partTwo=False):
    def bitDecode(bits):
        return(sum([int(bits[::-1][x]) * (2 ** x) for x in range(len(bits))]))

    def evaluatePacket(packet):
        version = packet[0]
        packet = packet[1]
        if packet == []:
            print(version)
        else:
            version += bitDecode(packet[:3])
            typeID = bitDecode(packet[3:6])
            if typeID != 4:
                if packet[6] == '0':
                    length = bitDecode(packet[7:22])
                    subpackets = packet[22:(22 + length)]
                    packetResults = evaluatePacket([version, subpackets])
                    version += packetResults[0]
                    remainingBits = packet[(22 + length):]
                else:
                    numberOfSubpackets = bitDecode(packet[7:18])
                    for i in range(numberOfSubpackets):
                        packet = packet[19:]
                        packetResults = evaluatePacket([version, packet])
                        version += packetResults[0]
                        remainingBits = packetResults[1]
                        packet = remainingBits
            else:
                literalBits = []
                bitIndex = 7
                while True:
                    if packet[bitIndex] == '1':
                        literalBits += packet[(bitIndex + 1):(bitIndex + 5)]
                        bitIndex += 5
                    else:
                        literalBits += packet[(bitIndex + 1):(bitIndex + 5)]
                        bitIndex += 5
                        break
                remainingBits = packet[bitIndex:]
            return(evaluatePacket([version, remainingBits]))
    binRepresentation = [bit for h in packets if h
                         != '\n' for bit in (bin(int(h, 16))[2:]).zfill(4)]
    evaluatePacket([0, binRepresentation])


parseCode(packets)
