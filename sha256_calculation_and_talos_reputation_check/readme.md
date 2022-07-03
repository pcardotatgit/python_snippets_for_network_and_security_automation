# Create a sha256 list 

The goal of this script is to calculate the sha256 of all the files that will be put into the **files_to_check**.

Why do we have to do that... For querying Cisco Talos for file reputations, thanks the SecureX Ribbon plugin. Are the files arey known and which one is malicious.

Specificaly when we browse the INTERNET and we download a lot of files 

## how to use this ?

First of all, a good practice is to surf on the INTERNET from a sandbox or from a endpoint your are not afraid to infect. ( A raspberry PI for example )

Into this endpoint create a folder named **check_file_reputation** and copy the python script into it.

In this **check_file_reputation** folder create a subdirectory named **files_to_check**.

The goal is to store all the binaries you could download from the Internet into this subfolder.

Don't hesistate to modify the script in order to point to the endpoint default **download** folder.

Then, regularly, run the **1-create_a_sha256_list.py** script.

This one will create a resulting file that is an hhtml file named index.html in the **check_file_reputation** directory

And it will run a web server that listen on port 8888.

Then from another endpoint launch a browser and open http://your_sandbox_ip:8888

Then you will see the sha256 list in the page and you can start the Browser's SecureX Ribbon plugin and the mailicious files will appear after a few seconds.