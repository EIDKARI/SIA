echo "jenkins node is connected"
rem remove old artifacts from the node
rm jenkins_file.txt
rem create a new jenkins artifact
copy nul > jenkins_file.txt
echo This file has been created by jenkins! > jenkins_file.txt