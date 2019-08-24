
"""
Command line script
Input:
	Interface
	MAC
Output:
	None
Function:
	Change the MAC address of the computer which runs this script
"""
import optparse
import subprocess
import re

def getOptions():
	parser = optparse.OptionParser()
	parser.add_option("-i","--interface",dest="interface",help="Interface to change its MAC address")
	parser.add_option("-m","--mac",dest="new_mac", help="New MAC address")
	options,parameters = parser.parse_args()
	if not options.interface:
		parser.error("Please specify a interface")
	elif not options.new_mac:
		parser.error("Please specify a new MAC") 
	return options

def changeMAC(interface,mad_addr):
	subprocess.call("ifconfig {:} down".format(interface),shell=True)
	subprocess.call("ifconfig {:} hw ether {:}".format(interface,mac_addr),shell=True)
	subprocess.call("ifconfig {:} up".format(interface,mac_addr),shell=True)

if __name__ == "__main__":
	options = getOptions()
	interface = options.interface
	mac_addr = options.new_mac
	changeMAC(interface,mac_addr)
	ifconfigResult = subprocess.check_output(["ifconfig",interface]).decode('utf-8')
	pattern = re.compile(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w')
	result = re.search(pattern ,ifconfigResult)
	if mac_addr == result.group(0):
		print("The mac address has successfully been changed to {:}".format(mac_addr))
	else:
		print("MAC address changing failed")