
import os
import xml.etree.ElementTree as ET
import sys
import shutil

tree = ET.parse('output.xml')
#root = tree.getroot()
search_pass = tree.findall(".//teststep/.[@result='pass']")
length = len(search_pass)
#some print outputs
print ("length of the list of pass:\n")
print (length)
print ("search pass list :\n")
print (search_pass)
search_fail = tree.findall(".//teststep/.[@result='na']")
length_fail = len(search_fail)
#some print outputs
print ("length of the list of fail:\n")
print (length_fail)
print ("search fail list :\n")
print (search_fail)
percentage_success = (length/(length+length_fail))*100
print ("Success percentage is: ", percentage_success, "%")

# Set environment variables
string_perc = str(percentage_success)
os.environ['Percentage_of_success'] = string_perc
test = os.getenv('Percentage_of_success')
print ("!!!!!!!!!!!!!!!!!!!!!!!",test)

#Define a criteria of 60% for success
if percentage_success >= 60:    
    os.environ['success_factor'] = "true"
else:
   os.environ['success_factor'] = "false" 

test1 = os.getenv('success_factor')
print ("++++++++++++++++",test1)


sys.stdout = open("test.txt", "w")
print(test1)
sys.stdout.close()

shutil.move("test.txt","genfile\\test.txt" )
print ("moved results into genfile")