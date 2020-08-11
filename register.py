
import json, configparser, sys
import requests,random
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter


#####################################################################################
######   SET_GLOBAL_PARAMETRES()  initializes all global variables            #######
#####################################################################################
global PARAMS
PARAMS=dict()

"""
def load_app_info(configfilelocation="./APP_INFO_DATA.ini"):
	global PARAMS
	try:
		application_information=configparser.ConfigParser()
		application_information.read("./APP_INFO_DATA.ini")
		PARAMS['APP_NAME'] = application_information['APP_INFO']['APP_NAME']
		PARAMS['APP_SOFT_VERSION'] = application_information['APP_INFO']['APP_SOFT_VERSION']
		PARAMS['APP_DESCRIPTION'] = application_information['APP_INFO']['APP_DESCRIPTION']
		PARAMS['APP_PROVIDER'] = application_information['APP_INFO']['APP_PROVIDER']
		PARAMS['VENDOR_ID'] = application_information['APP_INFO']['VENDOR_ID']
		PARAMS['MEMORY'] = application_information['APP_INFO']['MEMORY']
		PARAMS['STORAGE'] = application_information['APP_INFO']['STORAGE']
		PARAMS['LATENCY'] = application_information['APP_INFO']['LATENCY']
		PARAMS['BANDWIDTH'] = application_information['APP_INFO']['BANDWIDTH']
	except Exception as e:
		print("Could NOT open the APP_INFO_DATA File. Details: " +str(e))

"""

def data_to_send_post_traffic_register():
	global sys
	global PARAMS
	DATA_TO_SEND={
	"appName": str(sys.argv[7]),
	"appDId" :str(sys.argv[1]),
	"appInstanceId" :str(sys.argv[2]),
	"trafficRuleId": "TrafficRule"+ str(random.randint(1,1000)),
  	"filterType": "FLOW",
  	"priority": 1,
  	"trafficFilter": 
  		[
			{
	  			"srcAddress": ["192.168.1.1"],
	  			"dstAddress": ["192.168.1.1"],
	  			"srcPort": ["8080"],
	  			"dstPort": ["8080"],
	  			"protocol": ["?"],
	  			"token": ["?"],
	  			"srcTunnelAddress": ["?"],
	  			"tgtTunnelAddress": ["?"],
	  			"srcTunnelPort": ["?"],
	  			"dstTunnelPort": ["?"],
	  			"qCI": 1,
	  			"dSCP": 0,
	  			"tC": 1
			}
  		],
  	"action": "DROP",
  	"dstInterface": 
  		{
			"interfaceType": "TUNNEL",
			"tunnelInfo": 
				{
	  				"tunnelType": "GTP_U",
	  				"tunnelDstAddress": "?",
	  				"tunnelSrcAddress": "?"
				},
			"srcMacAddress": "02-00-00-00-00-00",
			"dstMacAddress": "02-00-00-00-00-00",
			"dstIpAddress": "192.0.2.0"
  		},
  	"state": "ACTIVE"
	}
	return DATA_TO_SEND


def POST_TRAFFIC():
	global sys
	DATA_TO_SEND= data_to_send_post_traffic_register()
	DATA_TO_SEND_JSON= json.dumps(DATA_TO_SEND)

	header = {"Content-type": "application/json"}
	r = requests.post(str(sys.argv[3])+":"+str(sys.argv[4]) +"/" + str(sys.argv[5]), json=DATA_TO_SEND_JSON, headers=header)
	print(r.text)


def data_to_send_post_dns_register():
	global sys
	DATA_TO_SEND={"ipAddressType": "IP_V6", "appName": str(sys.argv[7]), "domainName": "www.example.com", "state": "ACTIVE", "dnsRuleId": "dnsRule"+str(random.randint(1,10000)), "ttl": "?", "ipAddress": "192.0.2.0", "appDId": str(sys.argv[1])}
	return DATA_TO_SEND


def POST_DNS():
	global sys
	DATA_TO_SEND= data_to_send_post_dns_register()
	DATA_TO_SEND_JSON= json.dumps(DATA_TO_SEND)

	header = {"Content-type": "application/json"}
	r = requests.post(str(sys.argv[3])+":"+str(sys.argv[4]) +"/" + str(sys.argv[6]), json=DATA_TO_SEND_JSON, headers=header)
	print(r.text)





if __name__== "__main__":
	#load_app_info()
	POST_TRAFFIC()
	POST_DNS()
	#PUT()
	#DELETE()
