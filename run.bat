echo "jenkins node is connected"
cd %CD%
if exist %CD%\genfile\ rmdir /s /q %CD%\genfile\
mkdir genfile
+++++++++++++++++
cd %CD%\genfile
rem create a new jenkins artifact
copy nul > jenkins_file.txt
echo This file has been created by jenkins! > jenkins_file.txt
