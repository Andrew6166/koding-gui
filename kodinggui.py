#!/usr/bin/python
import os
import getpass
import sys

def redraw():
    
    os.system(['clear','cls'][os.name == 'nt'])
    
    print """\
    
     **                   ** **                                    **
    /**                  /**//            *****     *****         // 
    /**  **  ******      /** ** *******  **///**   **///** **   ** **
    /** **  **////**  ******/**//**///**/**  /**  /**  /**/**  /**/**
    /****  /**   /** **///**/** /**  /**//******  //******/**  /**/**
    /**/** /**   /**/**  /**/** /**  /** /////**   /////**/**  /**/**
    /**//**//****** //******/** ***  /**  *****     ***** //******/**
    //  //  //////   ////// // ///   //  /////     /////   ////// //    Version 1.0
    
    """


redraw()

def mainmenu():
    print """\
    
    (1) Services
    (2) Setup FTP
    (3) Setup Webmin
    (^C) Quit
    
    """

def services():
	print """\
				
	(1) Start
	(2) Stop
	(3) Restart
	(4) Main menu
	"""

x = 0

while x is not "q" or x is not "Q":
	try:
		redraw()
		mainmenu()
		x = raw_input("Choose an Option. ")
		
		if int(x) == 1:
			redraw()
			print """\
			
			(1) Apache
			(2) FTP
			(3) Webmin
			
			"""
			b = raw_input("Choose an Option. ")
			if int(b) == 1:
				services()
				
				a = int(raw_input("Choose an option. "))
				
				if a == 1:
					os.system("sudo service apache2 start")
				elif a == 2:
					os.system("sudo service apache2 stop")
				elif a == 3:
					os.system("sudo service apache2 restart")
			elif int(b) == 2:
				services()
				
				a = int(raw_input("Choose an option. "))
				
				if a == 1:
					os.system("sudo service proftpd start")
				elif a == 2:
					os.system("sudo service proftpd stop")
				elif a == 3:
					os.system("sudo service proftpd restart")
			elif int(b) == 3:
				services()
				
				a = int(raw_input("Choose an option. "))
				
				if a == 1:
					os.system("sudo service webmin start")
				elif a == 2:
					os.system("sudo service webmin stop")
				elif a == 3:
					os.system("sudo service webmin restart")
		elif int(x) == 2:
			os.system("sudo apt-get install proftpd")
			os.system("sudo passwd " + str(getpass.getuser()))
		elif int(x) == 3:
			os.system("wget http://prdownloads.sourceforge.net/webadmin/webmin_1.710_all.deb")
			os.system("sudo dpkg -i webmin_1.710_all.deb")
			os.system("sudo apt-get -f install")
			os.system("sudo dpkg -i webmin_1.710_all.deb")
			os.system("rm webmin_1.710_all.deb")
	except KeyboardInterrupt:
		print
		sys.exit()
