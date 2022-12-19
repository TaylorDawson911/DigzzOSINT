import json, requests, socket, sys

import requests
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def ip_lookup(ip):
    url = f"https://ipapi.co/{ip}/json/"
    response = requests.get(url)
    # load the json response
    try:
        data = json.loads(response.text)
        return data
    except:
        return None


def port_lookup(ip, method):
    global ports
    if method == "common":
        ports = [21, 22, 23, 25, 53, 80, 110, 123, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080]
    elif method == "all":
        ports = range(1, 65535)
    try:
        # will scan ports between 1 to 65,535
        for port in ports:
            print(f"{bcolors.OKBLUE}Scanning port {port}{bcolors.ENDC}")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)

            # returns an error indicator
            result = s.connect_ex((ip, port))
            if result == 0:
                print("Port {} is open".format(port))
            s.close()
    except socket.gaierror:
        print(f"{bcolors.FAIL}Hostname Could Not Be Resolved!{bcolors.ENDC}")
        sys.exit()
    except socket.error:
        print(f"{bcolors.FAIL}Server not responding!{bcolors.ENDC}")
        sys.exit()
    return None
