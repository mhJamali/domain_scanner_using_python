import requests
import socket
import json

# the domain to scan for subdomains
domain = "rdandx.com"

# read all subdomains
file = open("subdomains.txt")
# read all content
content = file.read()
# split by new lines
subdomains = content.splitlines()
my_list = []

for subdomain in subdomains:
    # construct the url
    url = f"http://{subdomain}.{domain}"
    try:
        # if this raises an ERROR, that means the subdomain does not exist
        requests.get(url)
    except requests.ConnectionError:
        # if the subdomain does not exist, just pass, print nothing
        pass
    else:
        print("[+] Discovered subdomain:", url)
        my_list.insert(0, url)
        my_list.insert(1, domain)

        resolved_ip = socket.gethostbyname(domain)
        my_list.insert(2, resolved_ip)
        print(domain + " | " + resolved_ip)
        try:
            r = requests.head(url)
            http_code = r.status_code
            my_list.insert(3, http_code)
            print(http_code)
            # prints the int of the status code. Find more at httpstatusrappers.com :)
        except requests.ConnectionError:
            print("failed to connect")
print(my_list)

# json output response
print(json.dumps(my_list))
