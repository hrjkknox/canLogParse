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
	packetArray = _formatPacketList(leadingZero, id, dataLength, data, tr, timeStamp)
	packetTuple = tuple(packetArray)

	return packetTuple

# Formats the packet into a nice format
def _formatPacket(leadingZero, id, dataLength, data, tr, timeStamp, outputFormat="2dArray"):
	if outputFormat == "dict":
		# Construct a dictionary with all of the data
		output = _formatPacketDict(leadingZero, id, dataLength, data, tr, timeStamp)
	elif outputFormat == "2dArray":
		# Construct an array with all of the data
		output = _formatPacketList(leadingZero, id, dataLength, data, tr, timeStamp)
	elif outputFormat == "tupleArray":
		# Construct a tuple with all of the data
		output = _formatPacketTuple(leadingZero, id, dataLength, data, tr, timeStamp)
	
	return output

def importCanData(file, outputFormat="2dArray"):
	# Get the raw CAN data and split it
	rawCanData = _fileToList(file)
	# The output array
	output = []

	# Loop through every packet logged
	for rawPacket in rawCanData:
		# Split the packet into its contents
		packet = rawPacket.split()

		# There's always a "logging stopped" line at the end
		if packet[0] == "Logging":
			continue
		
		# The leading zero at the start of the packet
		leadingZero = packet[0]
		# The ID of the packet
		id = packet[1]
		# The length of the actual data
		dataLength = int(packet[2])
		# The actual bytes of data
		data = _extractDataFromPacket(packet)
		# The transmit/receive byte
		tr = packet[-1]
		# The timestamp of the packet
		timeStamp = float(packet[-2])

		# Format the output as requested
		formattedPacket = _formatPacket(leadingZero, id, dataLength, data, tr, timeStamp, outputFormat=outputFormat)
		output.append(formattedPacket)

	return output