# (c)2011 Deri Taufan - deritaufan@gmail.com
# This script will add list of computers to a group
# 


import requests
import xml.etree.ElementTree as ET
import csv

jamfURL = "https://your_jamf_url.jamfcloud.com/"
# cred here is based on bash command printf 'username:password' | iconv -t ISO-8859-1 | base64 -i -
cred = "xxx"

groupID = '232' # Group ID
apiGroupURL = "/JSSResource/computergroups/id/" + groupID
apiComputer = "/JSSResource/computers/match/"

with open('emails.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        email = row[0]
        print(email)
        r = requests.get(jamfURL + apiComputer + email, headers = headers)
        xmlResponse = ET.fromstring(r.text)
        
        for computer in xmlResponse.findall('computer'):
            id = computer.find('id').text
            name = computer.find('name').text
            print("%s - %s" % (id, name))
            payload = "<computer_group><computer_additions><computer><name>" + name + "</name></computer></computer_additions></computer_group>"
            rq = requests.put(jamfURL + apiGroupURL, headers=headers, data=payload)
