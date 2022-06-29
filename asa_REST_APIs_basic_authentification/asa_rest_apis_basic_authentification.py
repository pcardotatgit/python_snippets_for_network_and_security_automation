import requests

server = "https://192.168.100.10"

username = "admin"
if len(sys.argv) > 1:
  username = sys.argv[1]

password = "password"
if len(sys.argv) > 2:
  password = sys.argv[2]

r = None
headers = {'Content-Type': 'application/json'}
api_path = "/api/monitoring/clock"        # param
auth_url = server + api_path
r = requests.get(auth_url, headers=headers, auth=requests.auth.HTTPBasicAuth(username,password), verify=False)

