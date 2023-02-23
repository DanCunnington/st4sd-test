#! /usr/bin/env python
import os, psutil
process = psutil.Process(os.getpid())
print(process.memory_info().rss)  # in bytes 
print("hello world")
