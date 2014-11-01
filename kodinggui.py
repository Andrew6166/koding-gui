#!/usr/bin/python
import os
import getpass

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
    
    (1) Apache
    (2) Setup FTP
    (3) Setup Webmin
    (^C) Quit
    
    """

x = 0

while x is not "q" or x is not "Q":
    mainmenu()
    x = raw_input("Choose an Option. ")
    
    if int(x) == 1:
        print """\
        
        (1) Start
        (2) Stop
        (3) Restart
        (4) Main menu
        
        """
        
        a = int(raw_input("Choose an option. "))
        
        if a == 1:
            os.system("sudo service apache start")
        elif a == 2:
            os.system("sudo service apache stop")
        elif a == 3:
            os.system("sudo service apache restart")
    elif int(x) == 2:
        os.system("sudo apt-get install proftpd")
        os.system("sudo passwd " + str(getpass.getuser()))
    elif int(x) == 3:
        os.system("wget http://prdownloads.sourceforge.net/webadmin/webmin_1.710_all.deb")
        os.system("sudo dpkg -i webmin_1.710_all.deb")
        os.system("sudo apt-get -f install")
        os.system("sudo dpkg -i webmin_1.710_all.deb")
        os.system("rm webmin_1.710_all.deb")

