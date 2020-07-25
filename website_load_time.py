#!/bin/bash/env python3

import time
import urllib.request as urllib2

def download_webpage():
    response=urllib2.urlopen("https://www.google.com", timeout=60)
    return response.read()

def elapsed_time():
    t0=time.time()
    webpage=download_webpage()
    t1=time.time()
    print("Elapsed time "+ str(t1-t0))


elapsed_time()