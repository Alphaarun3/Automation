########################## Program starts ##############################

import subprocess
from pyfiglet import print_figlet
import pyfiglet
############Color and font style for the tool name####################
colors="188;19;254"
print_figlet("Auto-Nmap Scanner ", font="slant", colors=colors)
print("Author: ArunKumar R \n")
########Getting Input##########


print("-#"*60)
print("\t\t\t Scans Can Perform using Nmap")
print("-#"*60)
print()
print("\t\t\t1---> Version Scan")
print("\t\t\t2---> regular All Scan")
print("\t\t\t3---> Os finger print Scan")
print("\t\t\t4---> SSL Sweet 32 Scan ")
print("\t\t\t5---> SSL Poodle Attack Scan ")
print("\t\t\t6---> Smb user name enumeration Scan ")
print("\t\t\t7---> aggresive scan ")
print("\t\t\t8---> Vuln Script Scan")
print()
print("Enter the Ip Address Or Host name: ")
Host = input()
print("Entert the type of scan to execute  : ")
n = int(input())


####### simple functionality code ########

def version_scan():
    subprocess.call(" nmap -sV " +Host , shell=True)

def regular_scan():
    subprocess.call(" nmap -T4 -sV -sT -sC -O " +Host , shell=True)
def Os_finger_print():
    subprocess.call(" nmap -O " +Host , shell=True)

def ssl_sweet_32():
    subprocess.call(" nmap -sV --script ssl-enum-ciphers -p 443 " +Host , shell=True)

def ssl_poodle_attack():
    subprocess.call(" nmap -sV --version-light --script ssl-poodle -p 443 " +Host, shell=True)

def smb_username_enum():
    subprocess.call(" nmap -sV --script smb-enum-users.nse -p445 " +Host , shell=True)

def aggresive_scan():
    subprocess.call(" nmap -A " +Host , shell=True)
def general_vuln():
    subprocess.call(" nmap --script vuln " +Host, shell=True)



######### Decision making statement ################


if n == 1:
    version_scan()

elif n == 2:
    regular_scan()

elif n == 3:
    Os_finger_print()

elif n == 4:
    ssl_sweet_32()

elif n == 5:
    ssl_poodle_attack()

elif n == 6:
    smb_username_enum()

elif n == 7:
    aggresive_scan()

elif n == 8:
    general_vuln()


else:
    print("Again run the script to choose any one option")


########################## Program ends here ############################33
