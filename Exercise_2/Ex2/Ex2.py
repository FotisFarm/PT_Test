import xml.etree.ElementTree as ET
import os
import csv

ex2 = open('Ex2.csv','w')
writer = csv.writer(ex2,delimiter=';')

#Search for xml files in this directory
for files in os.listdir():
    csvwrite = []
    if files.endswith('.xml'):
       
       #Iterate through elements to find those with tag: 'inputSymbol'
        filexml = ET.parse(files)
        root = filexml.getroot()
        for child in root:
            for items in child.findall('Items'):
                #'inputSymbol' elements are children of 'Item' elements, who are children of 'Items' elements 
                for item in items:
                    input = item.find('inputSymbol')
                    if input is not None and input.text == '_pdg_list':
                        
                        for value in (item.find('value').text).split(','):
                            csvwrite.append(value)
    if csvwrite:
        csvwrite.insert(0,os.path.abspath(files))
        writer.writerow(csvwrite)        

    
     