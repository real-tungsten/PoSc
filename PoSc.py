import os

RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
BLUE   = "\033[94m"
CYAN   = "\033[96m"
WHITE  = "\033[97m"
RESET  = "\033[0m"
 
logo = r"""
`7MM'"'Mq.               .M'"'bgd          
  MM   `MM.             ,MI    "Y          
  MM   ,M9 ,pW"Wq.      `MMb.      ,p6"bo  
  MMmmdM9 6W'   `Wb       `YMMNq. 6M'  OO  
  MM      8M     M8     .     `MM 8M       
  MM      YA.   ,A9     Mb     dM YM.    , 
.JMML.     `Ybmd9'      P"Ybmmd"   YMbmd'  
                                           
"""
print(RED+logo+RESET)

print(f"{GREEN}*==* BY: YUVRAJ CHAUHAN *==*{RESET}")
print(f"{BLUE}============================{RESET}")
print(f"{GREEN}real-tungsten (Github) | 0fficial.yuvraj (Instagram (Main Id)){RESET}")
print(f"{BLUE}==============================================================={RESET}\n \n")

print(f"{YELLOW}Is script ko please root ma chalaya (This Script is run on Root){RESET}")
print(f"{BLUE}================================================================={RESET}\n")
print(f"{YELLOW}##Namasta (Hi / Welcome)##{RESET}")
print(f"{BLUE}Ya tool bas educational purpose ka leya bana gaya h !! (This tool is only for educational purpose !!){RESET}\n")
print(f"{RED}[1]NMAP{RESET}")
print(f"{RED}[*]RustScan (Comming Soon){RESET}\n")
choise_a = input(f"{GREEN}Option Chuno ?? (Choose The Option ?){RESET}").strip()
if choise_a == "1":
    print(f"{CYAN}\n[**]Apna Linux Distro Chuno?? (Choose Your Distro??)[**]")
    print(f"{YELLOW}[1]Debian-based (Ubuntu, Kali Linux, Linux Mint, Debian, Pop!_OS){RESET}")
    print(f"{RED}[2]Red Hat-based (Fedora, RHEL, CentOS, AlmaLinux){RESET}")
    print(f"{GREEN}[3]Arch-based (Arch Linux, Manjaro, Garuda Linux){RESET}")
    print(f"{YELLOW}[4]openSUSE (Leap / Tumbleweed){RESET}")
    print(f"{CYAN}[5]Turmax{RESET}")
    choise_aa = input(f"{BLUE}Apna Linux Distro Chuno ? (Choose Your Linux Distro ?){RESET}").strip()
    if choise_aa == "1":
        print(f"{RED}Wait karo Nmap install/setup ho raha h (Wait while nmap setup or install{RESET}")
        os.system("sudo apt install nmap -y")

    if choise_aa == "2":
        print(f"{RED}Wait karo Nmap install/setup ho raha h (Wait while nmap setup or install{RESET}")
        os.system("sudo dnf install nmap -y")

    if choise_aa == "3":
        print(f"{RED}Wait karo Nmap install/setup ho raha h (Wait while nmap setup or install{RESET}")
        os.system("sudo pacman -S nmap -y")

    if choise_aa == "4":
        print(f"{RED}Wait karo Nmap install/setup ho raha h (Wait while nmap setup or install{RESET}")
        os.system("sudo zypper install nmap -y")

    if choise_aa == "5":
        print(f"{RED}Wait karo Nmap install/setup ho raha h (Wait while nmap setup or install{RESET}")
        os.system("pkg install nmap -y")

else:
    print(f"{RED} !!Shai Option Chuno !!  (!! Choose Write Option !!){RESET}")



ip = input(f"\n{RED}Ip dalo (Enter Victim Ip): {RESET}").strip()

print(f"\n{YELLOW}[1]Saadha Mode(Normal Mode){RESET}                                       {RED}[2]Ravan Mode(God Mode){RESET}")
choise_b = input(f"\n{BLUE}Apna option chuno(1/2) !! (Chose Option(1/2)!!){RESET}").strip()
if choise_b == "1":
    print(f"\n{GREEN}[1]Host Discovery (Ping Scan){RESET}")
    print(f"{GREEN}[2]TCP SYN Scan (Stealth Scan){RESET}")
    print(f"{GREEN}[3]TCP Connect Scan{RESET}")
    print(f"{GREEN}[4]UDP Scan{RESET}")
    print(f"{GREEN}[5]Service Version Detection{RESET}")
    print(f"{GREEN}[6]OS Detection{RESET}")
    print(f"{GREEN}[7]Aggressive Scan{RESET}")
    print(f"{GREEN}[8]Script Scan (NSE){RESET}")
else:
    print(f"\n[!!] {RED}Note-{RESET}{YELLOW}Option 13 kam nahi kar raha h (option 13 is not working){RESET} [!!]")
    print(f"\n               {RED}[2]{RESET}")
    print(f"{BLUE}+[**#*#**]+{RESET}{RED}RAVAN MODE{RESET}{BLUE}+[**#*#**]+{RESET}")
    print(f"{RED}=================================")
    print(f"\n{GREEN}[11]Decoy Scan{RESET}")
    print(f"{GREEN}[12]Packet Fragmentation{RESET}")
    print(f"{GREEN}[13]Idle / Zombie Scan{RESET}")
    print(f"{GREEN}[14]FIN Scan{RESET}")
    print(f"{GREEN}[15]Xmas Scan{RESET}")
    print(f"{GREEN}[16]Null Scan{RESET}")
    print(f"{GREEN}[17]ACK Scanning{RESET}")
    print(f"{GREEN}[18]Source Port Spoofing{RESET}")
    print(f"{GREEN}[19]Vulnerability Assessment{RESET}")
    print(f"{GREEN}[20]Fast Scan Mode{RESET}")
option_choise = input(f"{RED}Apna option chuno !! (Chose Option(!!){RESET}").strip()
if option_choise == "1":
    os.system(f"nmap -Pn {ip}")

if option_choise == "2":
   os.system(f"nmap -sS {ip}")

if option_choise == "3":
   os.system(f"nmap -sT {ip}")

if option_choise == "4":
   os.system(f"nmap -sU {ip}")

if option_choise == "5":
   os.system(f"nmap -sV {ip}")

if option_choise == "6":
   os.system(f"nmap -O {ip}")

if option_choise == "7":
   os.system(f"nmap -A {ip}")

if option_choise == "8":
   os.system(f"nmap -sC {ip}")

if option_choise == "9":
   print(f"{YELLOW}!! More option comming soon. Please select 1-8 !!")

if option_choise == "10":
   print(f"!! More option comming soon. Please select 1-8 !!{RESET}")


if option_choise == "11":
   os.system(f"nmap -D RND:10 {ip}")

if option_choise == "12":
   os.system(f"nmap -f {ip}")

if option_choise == "13":
   print(f"{RED}\n!![ERROR]!!{RESET} {YELLOW}Sorry! This option is Not working in this time. Please select other option.For select other option please Run one more time script{RESET} {RED}!![ERROR]!!{RESET}")

if option_choise == "14":
   os.system(f"nmap -sF {ip}")

if option_choise == "15":
   os.system(f"nmap -sX {ip}")

if option_choise == "16":
   os.system(f"nmap -sN {ip}")

if option_choise == "17":
   os.system(f"nmap -sA {ip}")

if option_choise == "18":
   os.system(f"nmap -g 53 {ip}")

if option_choise == "19":
   os.system(f"nmap --script vuln {ip}")

if option_choise == "20":
   os.system(f"nmap -F -T4 {ip}")

print(f"\n{BLUE}                                                            !! Thanks For Running This Script. !!{RESET}\n")
print(f"{GREEN}BY: Yuvraj Chauhan | Student of Class 9 | Instagram ID - 0fficial.yuvraj ( Link here: https://www.instagram.com/0fficial.yuvraj/ ) | Github - real.tungsten{RESET}")
print(f"{YELLOW}============================================================================================================================================================{RESET}")