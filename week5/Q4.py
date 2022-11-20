from sys import argv
from urllib.request import urlopen
from urllib.error import *
try:
    lnk= urlopen(argv[1])
except IndexError:
    print(f"Url not found and {IndexError}")
except HTTPError:
    print(f"HTTP error{HTTPError}")
except URLError:
    print(f"Page not found! {URLError}")
else:
    print("Got it!")