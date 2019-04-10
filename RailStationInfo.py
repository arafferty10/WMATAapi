########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

#Library to beautify JSON data
import pprint
pp = pprint.PrettyPrinter(indent=1)

#Import API Key from key.txt
keys_file = open("keys.txt")
lines = keys_file.readlines()
apiKey = lines[0].rstrip()

headers = {
    # Request headers
    'api_key': apiKey
}

params = urllib.parse.urlencode({
    # Request parameters
    # Enter Line Code Here
    'LineCode': 'OR',
})

try:
    conn = http.client.HTTPSConnection('api.wmata.com')
    conn.request("GET", "/Rail.svc/json/jStations?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    #Using Pretty Printer Here
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
