########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

#Import API Key from key.txt
keys_file = open("keys.txt")
lines = keys_file.readlines()
apiKey = lines[0].rstrip()

headers = {
    # Request headers
    'api_key': apiKey,
}

params = urllib.parse.urlencode({
    # Request parameters
    'FromStationCode': 'K07',   #K07 - Dunn Loring
    'ToStationCode': 'C02',     #C02 - McPherson Square
})

try:
    conn = http.client.HTTPSConnection('api.wmata.com')
    conn.request("GET", "/Rail.svc/json/jSrcStationToDstStationInfo?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
