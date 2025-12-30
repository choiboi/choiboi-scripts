Delete Missing Files From Set
=============================

If you have two sets of folders with the same file naming sequence (regardless of file type). Then you  
go through the one folder and delete some files. This script will delete those files in the other set  
of files. This script assumes that it has similar prefix filename sequence. Ignores file extension types. 

**NOTE:**  
This script will ignore ```.DS_Store``` file. To change or modify files
to ignore, modify the ```IGNORE_FILENAMES``` list to customize which files
you want the script to ignore. Must be exact filenames.  


**EXAMPLE:**  
Folder 1:
- file_01.jpg
- file_04.jpg
- file_05.jpg
- file_10.jpg
- file_12.jpg
- file_15.jpg
- file_16.jpg

Folder 2:
- file_01.png
- file_02.png
- file_03.png
- file_04.png
- file_05.png
- file_06.png
- file_07.png
- file_08.png
- file_09.png
- file_10.png
- file_11.png
- file_12.png
- file_13.png
- file_14.png
- file_15.png
- file_16.png

If you enter directory to Folder 1 for first question `Main directory:`.  
If you enter firectory to Folder 2 for second question `Directory to mimic main directory:` then you will get the following result.

Folder 2(result):  
- file_01.png
- file_04.png
- file_05.png
- file_10.png
- file_12.png
- file_15.png
- file_16.png
