import requests
import os
os.system("")
from bs4 import BeautifulSoup
import webbrowser

while True:
    lnk = "https://en.wikipedia.org/wiki/Special:Random"
    x = requests.get(lnk)
    soup = BeautifulSoup(x.content, 'html.parser')
    headin = soup.find(class_ = "firstHeading").text
    print ("\033[0;32m" + headin + "\033[0m")
    print("Do You wish to view it? (Y/N): ")
    ans = str(input(""))
    if (ans.lower() == "y"):
        url = 'https://en.wikipedia.org/wiki/%s' %headin
        webbrowser.open(url)
        break
    elif (ans.lower() == "n"):
        print("\nOkay\nFinding another article for you...\n")
        continue
    else:
        print("\n\033[91m" + "Invalid Input" + "\033[0m\n")
        continue