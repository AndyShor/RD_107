This folder is a case folder used for launch from sea level (ambient pressure 100kPa).
For varying flight stages  replace boundary and initial conditions related to ambient pressure accordingly in /0/p and /system/setFieldsDict.
To do so copy default boundary conditions from /0/default, edit them, edit /system/setFieldsDict 
then run usual 
$ blockMesh
$ setFields
$ rhoCentralFoam

For running on AWS use attached shell script (modify s3 bucket and local folder names) that will copy the data to an s3 bucket and terminate your spot instance once the simulation is complete, it will save you a few coins.
