def convert_mask(ip):
	'''
	convert all mask formated  x.x.x.x  into  /x  ( ex: 255.255.255.0  => /24 )
	'''
	ip=ip.strip()
	liste=[]
	liste=ip.split(" ")
	address=liste[0]
	if len(liste)>1:
		netmask=liste[1]
		newmask=sum(bin(int(x)).count('1') for x in netmask.split('.'))
		new_adress=address+'/'+str(newmask)
	else:
		new_adress=address
	return(new_adress)