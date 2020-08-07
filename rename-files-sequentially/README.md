Rename filename Sequentially
============================

Basically this script will go through all the files sorted alphabetically
in the provided source directory. Then it will rename and append a 
number to the end of the filenames and move to the destination
directory.

**NOTE:**  
This script will ignore ```.DS_Store``` file. To change or modify files
to ignore, modify the ```IGNORE_FILENAMES``` list to customize which files
you want the script to ignore. Must be exact filenames.  

When the script is executed, it will ask for the following input:  
* Source directory containing the files you want to rename and/or move.  
* Destination directory where you want to move the files to, you can
input the source directory if you like.  
* Filename prefix, the name you want to use before the numbers.
* Starting sequence number, sequence number you want start from.
* Number digits for the sequence number, if the number is greater than
the number of digits of the sequence number, then ```0``` are appended to
the front.

**EXAMPLE:**  
**Filename Prefix:** RAW-IMAGE-  
**Starting Sequence Number:** 1  
**Number of digits for Sequence Number:** 4  
**Resulting filenames:**  
RAW-IMAGE-0001  
RAW-IMAGE-0002  
...  
RAW-IMAGE-0010  
...  
RAW-IMAGE-0100  
...  

**EXAMPLE:**  
**Filename Prefix:** RAW-IMAGE-  
**Starting Sequence Number:** 1  
**Number of digits for Sequence Number:** 2  
**Resulting filenames:**  
RAW-IMAGE-01  
RAW-IMAGE-02  
...  
RAW-IMAGE-10  
...  
RAW-IMAGE-100  
...  
