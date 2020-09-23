#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

# imports always go at the top of your code
import requests

def main():
    """Run time code"""
    # create r, which is our request object
    r = requests.get("http://api.open-notify.org/astros.json")

    # display the methods available to our new object
    print( dir(r) )
main()

