########### Python 3.2 #############
#Real Time Rail Prediction Snippet from WMATA API
#https://developer.wmata.com/docs/services/547636a6f9182302184cda78/operations/547636a6f918230da855363f

import http.client, urllib.request, urllib.parse, urllib.error, base64

#Library to beautify JSON data
import pprint
pp = pprint.PrettyPrinter(indent=4)

#Import API Key from key.txt
keys_file = open("keys.txt")
lines = keys_file.readlines()
apiKey = lines[0].rstrip()

headers = {
    # Request headers
    'api_key': apiKey,
}

params = urllib.parse.urlencode({
})

try:
    conn = http.client.HTTPSConnection('api.wmata.com')
    conn.request("GET", "/StationPrediction.svc/json/GetPrediction/K07?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    pp.pprint(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
