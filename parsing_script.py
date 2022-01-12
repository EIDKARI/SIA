
import os
import xml.etree.ElementTree as ET
import sys
import shutil

#parse the test xml report
try:
    tree = ET.parse('output.xml')
except:
    print('Cannot open the file specified, or the file doesnot exist')
#search for the pattern pass, and save all findings in a list
try:
    search_pass = tree.findall(".//teststep/.[@result='pass']")
except:
    print('Cannot find string')
length = len(search_pass)
#some print outputs for debugging
print ("length of the list of pass:\n")
print (length)
print ("search pass list :\n")
print (search_pass)
#search for the pattern fail, and save all findings in a list
try:
    search_fail = tree.findall(".//teststep/.[@result='na']")
except:
    print('Cannot open the file specified, or the file doesnot exist')
length_fail = len(search_fail)
#some print outputs
print ("length of the list of fail:\n")
print (length_fail)
print ("search fail list :\n")
print (search_fail)
percentage_success = (length/(length+length_fail))*100
print ("Success percentage is: ", percentage_success, "%")

# Set environment variables
#string_perc = str(percentage_success)
#os.environ['Percentage_of_success'] = string_perc
#test = os.getenv('Percentage_of_success')
#print ("!!!!!!!!!!!!!!!!!!!!!!!",test)

#Define a criteria of 60% for success
if percentage_success >= 60:    
    os.environ['success_factor'] = "true"
else:
   os.environ['success_factor'] = "false" 

test1 = os.getenv('success_factor')
print ("Success factor is: ",test1)


try:
    file = open("test.txt", "w")
except:
    print('Cannot open the file')
try:    
    file.write(test1)
except:
    print('Cannot write to the file')
try:
    file.close()
except:
    print('no file to close')
#shutil.copyfile("test.txt", "genfile\\test.txt")