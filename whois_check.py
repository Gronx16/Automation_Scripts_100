#!/bin/bash/env python3

from subprocess import check_output
website=input("Enter domain name (eg. google.com): ")
print()
try:
    whois_output=list((check_output("whois {}".format(website), shell=True).decode("UTF-8")).splitlines())
    cat=0
    for ch in whois_output:
        if "Domain Name" in ch:
            cat+=1
            if cat>1:
                break 
            print(ch)
        elif "Registry Domain ID" in ch:
            print(ch)
        elif "Registrant Organization" in ch:
            print(ch)
        elif "Registrar URL" in ch:
            print(ch)
        elif "Creation Date" in ch:
            print(ch)
        elif "Registry Expiry Date" in ch:
            print(ch)
        elif "Name Server" in ch:
            print(ch)   
except Exception as ex:
    print("Enter the correct domain name")
    print()
finally:
    print("\n\n")
    print("Thanks for using the script")


print("-------------------------------------------------------------------------------------------------")
