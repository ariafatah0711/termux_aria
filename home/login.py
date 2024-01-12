import os, sys, time
import getpass

x = "aria"
y = "123"

print('\033[1;93m')
print('\033[1;36m<===============\033[1;37m{\033[1;34mWELCOME TO\033[1;37m}\033[1;36m===============> ')
print("\033[1;93m")
print("\033[1;34m<<<<<<<<<<<<<\033[1;37m{\033[1;36mTERMUX INDONESIA\033[1;37m}\033[1;34m>>>>>>>>>>>>>") 
print("\033[1;93m")
print("\033[1;36m<~~~~~~~~~~~~~~\033[1;37m[\033[1;34m-USER LOGIN-\033[1;37m]\033[1;36m~~~~~~~~~~~~~~>")
print("\033[1;93m")

def login():
    os.system("")
    user = raw_input("\33[1;37musername : \033[1;30m")
    pasw = getpass.getpass("\33[1;37mpassword : \033[1;30m")
    if user == x and pasw == y:
         print "\n\033[1;32mwait a minute..."
         time.sleep(2)
         print "\n\33[1;32mAccess grented"
         time.sleep(2)
         sys.exit
    else:
         print "\n\033[1;32mwait a minute..."
         time.sleep(2)
         print "\n\033[1;31mAccess Denied\n"
         time.sleep(2)
         login()

if __name__ == "__main__":
             login()
