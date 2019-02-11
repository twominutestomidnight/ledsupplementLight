import os

#os.system("curl http://login:password@192.168.40.39/ISAPI/Event/notification/alertStream > qwe.txt")

#os.system("curl --digest --user login:password 192.168.40.176/ISAPI/Event/triggers > qweqwe.txt")

import requests
from requests.auth import HTTPDigestAuth

url = 'http://192.168.40.176/ISAPI/Event/triggers'
url2 = 'http://192.168.40.176/ISAPI/Event/notification/alertStream'
r = requests.get(url, auth=HTTPDigestAuth('login', 'password'))
print("status : ", r.status_code, " text: ", r.text)
print("==================================== ")
r = requests.get(url2, auth=HTTPDigestAuth('login', 'password'))
