def web():
    while True:
        os.system("tput setaf 7")
        print("\t\tConfiguring Web Server\n")
        os.system('tput setaf 7')
        print(" 1. Check the Web Server Software Install or Not
2. If not, Then Install Web Server Software
3. Check status, Web Service Start or Not
4. If not. Then Start the Web Service
5. Create File which is you want to show the Client
6. Check list of how many files we have :
7. To view website
")

        x = input("Enter Choice: ")
        if int(x)==1:
            os.system("dnf list httpd")
        elif int(2)==2:
            os.system("dnf install httpd")
        elif int(x)==3:
            os.system("systemctl status httpd")
        elif int(x)==4:
            os.system("systemctl start httpd")
        elif int(x)==5:
            file = input(" File name: ")
            os.system("gedit {}".format(f))
        elif int(x)==6:
            os.system("ls /var/www/html")
        elif int(x)==7:
            i=input("Enter url to see website")
            import webbrowser
            webbrowser.open("x")
        else:
            os.system("tput setaf 1")
            print("Invalid Option")