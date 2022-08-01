while 1>0:
	url= input("url>>")
	name= input("filename>>")
	import os
	os.system("curl "+url+" -o "+name)
