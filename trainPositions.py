########### Python 3.2 #############
#Train Position Snippet from WMATA API
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
})

try:
    conn = http.client.HTTPSConnection('api.wmata.com')
    conn.request("GET", "/TrainPositions/TrainPositions?contentType={contentType}&%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
