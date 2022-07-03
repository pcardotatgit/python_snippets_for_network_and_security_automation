#!/usr/bin/python3
import http.server
from crayons import *
import os 
import hashlib

def sha256(filename):
    sha256_hash = hashlib.sha256()
    filename="./files_to_check/"+filename
    with open(filename,"rb") as f:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
        resultat=sha256_hash.hexdigest()
    return(resultat)
    

def start_web():
    PORT = 8888
    server_address = ("", PORT)
    server = http.server.HTTPServer
    handler = http.server.CGIHTTPRequestHandler
    print("Starting on port :", PORT ," open : http:8888//{server_address}/index.html")    
    httpd = server(server_address, handler)
    httpd.serve_forever()
    
    
if __name__=='__main__':   
    files =[file for file in os.listdir('./files_to_check')]
    with open('index.html','w') as fichier:
        fichier.write("<html><body><ul>")
        print()
        for file in files:
            sha=sha256(file)
            print(green(sha,bold=True))
            fichier.write(f"<li>{sha}</li>")
        fichier.write(f"<li><b> Ajout&eacute; manuellement par Patrick : 54c0cd40ea153f2b8cdc27c1b1baf96d77505807bda9979f2ba9ccb7ff0db3ed en plien milieu d'un paragraphe . Ca pourrait des logs !!</></li>")            
        fichier.write("</ul></body></html>")
    start_web()