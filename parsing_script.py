import os
import xml.etree.ElementTree as ET
import sys
import shutil
import random
import json

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
item_new ='out\\' + item
try:
    tree = ET.parse(item_new)
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
#######################################################
#Move the tests amount and the tests failed to json objects
data_set1 = {"key":"TESTSTEPS_AMOUNT", "value1":[length + length_fail]}
data_set2 = {"key":"TESTSTEPS_FAILED", "value2":[length_fail]}
json_dump1 = json.dumps(data_set1)
json_dump2 = json.dumps(data_set2)
json_object1 = json.loads(json_dump1)
json_object2 = json.loads(json_dump2)
#Parse the json object class strings and remove extra characters from prefix and suffix locations
Test_steps_amount =str(json_object1["value1"])
Test_STEPS_FAILED =str(json_object2["value2"])
Test_steps_amount1=Test_steps_amount.removeprefix('[')
Test_steps_amount_FINAL=Test_steps_amount1.removesuffix(']')
Test_STEPS_FAILED1=Test_STEPS_FAILED.removeprefix('[')
Test_STEPS_FAILED_FINAL=Test_STEPS_FAILED1.removesuffix(']')
#Save the json results in text files .. these will be stashed, unstashed, and saved to local variables in jenkins pipelines world
try:
    file = open("output_test.txt", "w")
except:
    print('Cannot open the file')
try:    
    file.write(Test_steps_amount_FINAL)
except:
    print('Cannot write to the file')
try:
    file.close()
except:
    print('no file to close')
try:
    file = open("output_test1.txt", "w")
except:
    print('Cannot open the file')
try:    
    file.write(Test_STEPS_FAILED_FINAL)
except:
    print('Cannot write to the file')
try:
    file.close()
except:
    print('no file to close')
