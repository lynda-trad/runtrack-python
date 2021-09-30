from os.path import exists
import xml.etree.ElementTree as ET
import re

filename = 'domains.xml'

if exists(filename):
    file = open(filename)
    line = file.read()
    count = re.findall("domain", line)
    print("There is ", len(count), "extensions.")

else:
    print("File does not exist.")