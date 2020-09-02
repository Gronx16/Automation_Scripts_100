#!/bin/bash/env python3

import subprocess
thrashold=5
lst=subprocess.check_output(['df','-k'])
lst1=(lst.splitlines())
for i in lst1[1:]:
    col=(i.decode("UTF-8")).split()
    use_percent=col[4]
    use_percent=use_percent.replace('%','')
    if int(use_percent)>thrashold:
        print("Value of %s is grater and it is %s"%(col[0],col[4]))
