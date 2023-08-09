# Description  
In the folder XMLS you will find some xml files.  
You'll need export to a csv file a list of the xml's fullpath that contains the tag `inputSymbol` with value `<_pdg_list>`. Get the value of the `<value>` tag and append it on the same line.
You may use any scripting language or python

## More explanation
The csv file should look like this:
```
C:\SomePath\xmlFileName1.xml;_pdg_1;_pdg_2
C:\SomePath\xmlFileName2.xml;_pdg_1;_pdg_2;_pdg_3
C:\SomePath\xmlFileName5.xml;_pdg_1
```  

- where: 
  - xmlFileName#.xml = xml file name
  - _pdg_x = the value of the *_pdg_list* tag


## Instructions
Run the `generate_random_folders.ps1` script to generate a random folder-file sample structure to work with.

## Deliverable
The solution script and the csv file.
