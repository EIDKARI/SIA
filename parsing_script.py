
import os
import xml.etree.ElementTree as ET
import sys
import shutil
import random

try:
    cwd = os.getcwd()
except:
    print('Cannot find current directory')

#Test results directory:
directory_new = cwd + '\\out'
print ('new directory is: ',directory_new)

#list the files in the test result directory
try:
    files = os.listdir(directory_new)
except:
    print('the directory is empty!')
print('Files in the current directory are as follows: ',files)

#Choose a file from the result directory in each run randomly
item = random.choice(files)
print('randomly selected output item is:', item)

##################################################################################
#parse the test xml report
try:
    tree = ET.parse(item)
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

#Get the success percentage
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

success_factor = os.getenv('success_factor')
print ("Success factor is: ",success_factor)


try:
    file = open("test.txt", "w")
except:
    print('Cannot open the file')
try:    
    file.write(success_factor)
except:
    print('Cannot write to the file')
try:
    file.close()
except:
    print('no file to close')
#shutil.copyfile("test.txt", "genfile\\test.txt")