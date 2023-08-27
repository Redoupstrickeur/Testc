import os,platform
os.system('git pull')
os.system('touch proxies.txt')
MANI=platform.architecture()[0]

if MANI=="64bit":

	

	print('\n \033[1;32m [×] \033[1;33mSorry Bro Your Device 64bit \n \033[1;32m [√] \033[1;31mThis Tool 64Bits Device Not Supported')

elif MANI=="32bit":

	

    __import__("REDOUPSHACK")
