# 💀 Omni-Flyconsole v7.0
**Advanced Network Security & Exploitation Framework**

Omni-Flyconsole is a multi-module security framework designed for advanced network analysis and penetration testing. Built specifically for Termux environments, it provides a powerful set of tools for both rooted and non-rooted Android devices.

## 🚀 Features
- **Scanner/Port**: Real-world socket-based port scanning to identify open services.
- **Exploit/Phishing**: Automated phishing engine with a built-in PHP server and credential logging.
- **Defense/Honeypot**: Intrusion detection system that logs unauthorized connection attempts.
- **Extreme/Broadcast Hijack**: SSDP protocol discovery for identifying SmartTVs and casting devices on a network.
- **Advanced UI**: Metasploit-style console interface for a professional user experience.

## 🛠 Installation
Run the following commands in Termux to install and launch the tool:

```bash
# Clone the repository
git clone [https://github.com/zxmoon76-sys/Omni-Flyconsole.git](https://github.com/zxmoon76-sys/Omni-Flyconsole.git)

# Navigate to the directory
cd Omni-Flyconsole

# Install required packages
pkg install python php -y

# Launch the framework
python omni.py

📖 Usage Guide
​Start the Tool: Run python omni.py to initialize the framework.
​List Modules: Type list to view all available attack and defense modules.
​Select a Module: Use the use command (e.g., use 2 or use exploit/phishing).
​Configure Options: Set your target IP or Port using the set command:
​set target 192.168.0.1
​set port 8080
​Execute: Type run to start the selected module with real-world logic.
​Go Back: Type back to return to the main menu.
​⚠️ Disclaimer
​This tool is developed for Educational Purposes Only. Any unauthorized use of this tool against third-party systems is illegal and strictly prohibited. The developer is not responsible for any misuse or damage caused by this framework.
​Developed by: Mamun ⚡
