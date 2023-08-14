import xml.etree.ElementTree as ET
import os
import csv

ex2 = open('Ex2.csv','w')
writer = csv.writer(ex2,delimiter=';')

for files in os.listdir():
    csvwrite = []
    if files.endswith('.xml'):
       
        filexml = ET.parse(files)
        root = filexml.getroot()
        for child in root:
            for i in child.findall('Items'):
                for childi in i:
                    input = childi.find('inputSymbol')
                    if input is not None and input.text == '_pdg_list':
                        value = childi.find('value').text
                        csvwrite.append(value)
    if csvwrite:
        csvwrite.insert(0,os.path.abspath(files))
        writer.writerow(csvwrite)        

    
     