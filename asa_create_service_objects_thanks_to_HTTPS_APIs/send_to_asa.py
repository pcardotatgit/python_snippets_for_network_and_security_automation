import requests
from pprint import pprint
username="admin"
password="password"
server="https://192.168.200.10"

input(' Let s execute a show version just to check if the ASA REST API is alive. Press Enter :' )
api_auth_path = "/admin/exec/show version"
auth_url = server + api_auth_path
r = requests.get(auth_url, auth=(username,password), verify=False)
pprint(r.text)
input(' If Connexion to ASA is Ok . type Enter ' )

input('Now let s read the cli_commands.txt file and send all command within it one after the other, to the ASA, Press Enter :')

line_content = []
with open('cli_commands.txt') as inputfile:
	for line in inputfile:
		if line[0] == "#" or line.strip() == "Site":
			pass
		else:
			line_content.append(line.strip())

# loop through all content
i=0
command=""
for content in line_content:
	print (content)		
	if i==0:
		command=command+"/"+content
		api_auth_path = "/admin/exec/conf+t/"+command
		auth_url = server + api_auth_path
		r = requests.get(auth_url, auth=(username,password), verify=False)
		pprint(r.text)
		i+=1
	else:
		command=command+"/"+content
		api_auth_path = "/admin/exec/conf+t/"+command
		auth_url = server + api_auth_path
		r = requests.get(auth_url, auth=(username,password), verify=False)
		pprint(r.text)
		command=""
		i=0

input(' Let s do a Write memory now')
api_auth_path = "/admin/exec/write mem"
auth_url = server + api_auth_path
#r = requests.get(auth_url, auth=(username,password), verify=False)
#pprint(r.text)



