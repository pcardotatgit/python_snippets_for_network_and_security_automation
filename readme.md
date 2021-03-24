# ASA HTTPS API EXAMPLE

This script is an example of interaction with a Cisco ASA thru what we call HTTPS APIs

What does it mean ?

When the ASA HTTP Server is enabled ( and it is when you manage the ASA thru ASDM ) then you can send cli commands to the ASA thru https requests.

You can do this with your browser. For example :

	https://{ ASA_IP_Address }/admin/exec/show version

or 

	https://{ ASA_IP_Address }/admin/exec/conf+term/hostname CISCO_ASA

This script reads the <b>cli_commands.cfg</b> file which contains a set of cli commands you want to send to your ASA. And send all of them to the device.

CLI commands are the ASA CLI commands. And you must type them in the file in the same order as you would type them into a SSH session with the ASA.
