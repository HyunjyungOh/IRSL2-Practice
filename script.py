import math
import os
import sys

import requests

# sort import
print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


# shift + alt +f : format document


r = requests.get("https://coreyms.com")
print(r.status_code)
