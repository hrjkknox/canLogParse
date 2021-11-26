def _fileToList(file):
	with open(file) as readFile:
		lines = readFile.readlines()
	return lines

# Takes a part-formed packet array and returns the data
def _extractDataFromPacket(packet):
	dataLength = int(packet[2])
	# Remove all non-data bytes
	# I know this is janky, but I'm doing this quickly
	packet.pop(0)
	packet.pop(0)
	packet.pop(0)
	packet.pop(-1)
	packet.pop(-1)
	
	# Convert the array of strings to an array of bytes
	dataArray = []
	for i in packet:
		dataArray.append(bytes.fromhex(i))

	return dataArray

# Turns the packet into a nice dictionary
def _formatPacketDict(leadingZero, id, dataLength, data, tr, timeStamp):
	outputDict = {}
	outputDict["leadingZero"] = leadingZero
	outputDict["id"] = id
	outputDict["dataLength"] = dataLength
	outputDict["data"] = data
	outputDict["T/R"] = tr
	outputDict["timeStamp"] = timeStamp

	return outputDict

# Turns the data into a nice list
def _formatPacketList(leadingZero, id, dataLength, data, tr, timeStamp):
	outputArr = []
	outputArr.append(leadingZero)
	outputArr.append(id)
	outputArr.append(dataLength)
	outputArr.append(data)
	outputArr.append(tr)
	outputArr.append(timeStamp)

	return outputArr

# Turns the data into a nice tuple
def _formatPacketTuple(leadingZero, id, dataLength, data, tr, timeStamp):
	packetArray = formatPacketList(leadingZero, id, dataLength, data, tr, timeStamp)
	packetTuple = tuple(packetArray)

	return packetTuple

