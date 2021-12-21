echo "jenkins node is connected"
cd %CD%
mkdir genfile
%gen_file%=%CD%\genfile
cd %gen_file%
rem create a new jenkins artifact
copy nul > jenkins_file.txt
echo This file has been created by jenkins! > jenkins_file.txt