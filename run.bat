echo "jenkins node is connected"
cd %CD%
if exist %CD%\genfile\ rmdir /s /q %CD%\genfile\
mkdir genfile
cd %CD%\genfile
rem create a new jenkins artifact
copy nul > jenkins_file.txt
echo Test 1 = SUCCESS \n Test 2 = SUCCESS \n Test 3 = SUCCESS \n Test 4 = SUCCESS \n Test 5 = FAIL  > jenkins_file.txt
