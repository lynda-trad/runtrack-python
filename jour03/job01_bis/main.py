from os.path import exists
import xml.etree.ElementTree as ET
import re

filename = 'domains.xml'

if exists(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    print(root)
    print(root.attrib)

    for x in root[0]:
        print(x.text)

    #for elem in root:
    #    for subelem in elem:
    #        print(subelem.text)

#    count = re.findall(".", )
#    print("There is ", count.len, "extensions.")

else:
    print("File does not exist.")

# Créer un programme qui parcourt le contenu du fichier “domains.xml” et qui
# compte le nombre d’extension de domain qui s’y trouvent (.com, .net, etc
# ...).